import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.exc
import telebot
import config
import search_parser as sp
from search_parser import word_info, word_list
import time


knownUsers = []
userStep = {}
msg = None

def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text' or "pinned_message":
            # print the sent message to the console and save to file
            t = time.localtime()
            current_time = time.strftime("%d %b %Y %H:%M:%S", t)
            print(str(current_time) + " " + str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + str(m.text))
            new_user = User(user_id=m.chat.id, username=m.chat.username, first_name=m.chat.first_name, last_name=m.chat.last_name)
            exists = User.query.get(new_user.user_id)
            if exists is None:
                db.session.add(new_user)
                db.session.commit()
                del new_user
            else:
                del new_user




bot = telebot.TeleBot(config.TOKEN)
bot.set_update_listener(listener)



server = Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = config.db_url
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
server.config["SESSION_PERMANENT"] = False
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
server.config["SESSION_TYPE"] = "filesystem"
db = SQLAlchemy(server)
db.init_app(server)

class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=True )
    first_name = db.Column(db.String, unique=False, nullable=True)
    last_name = db.Column(db.String, unique=False, nullable=True)




@bot.message_handler(commands=['start'])
def start_message(message):
    cid = message.chat.id
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Azərbaycan 🇦🇿', callback_data="az"))
    markup.add(telebot.types.InlineKeyboardButton(text='Русский 🇷🇺', callback_data="ru"))
    markup.add(telebot.types.InlineKeyboardButton(text='English 🇺🇸', callback_data="en"))
    if cid not in knownUsers:
        knownUsers.append(cid)
        userStep[cid] = ""
        global msg
        msg = bot.send_message(cid, text=config.Lang_chose_az, reply_markup=markup)
    else:
         bot.send_message(cid, text=config.Query_handler["fa_{}".format(userStep[cid])])
    



@bot.message_handler(commands=["lang", "🌎"])
def change_lang(m):
    cid = m.chat.id
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Azərbaycan 🇦🇿', callback_data="az"))
    markup.add(telebot.types.InlineKeyboardButton(text='Русский 🇷🇺', callback_data="ru"))
    markup.add(telebot.types.InlineKeyboardButton(text='English 🇺🇸', callback_data="en"))
    if cid not in knownUsers:
        knownUsers.append(cid)
    global msg
    msg = bot.send_message(cid, text=config.Lang_chose_az, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text=config.Query_handler["hello_msg"])
    first_answer = ''
    if call.data == 'az':
        cd = call.data
        userStep.update({call.message.chat.id: cd})
        first_answer = config.Query_handler["fa_az"]
    elif call.data == 'ru':
        cd = call.data
        userStep.update({call.message.chat.id: cd})
        first_answer = config.Query_handler["fa_ru"]
    elif call.data == 'en':
        cd = call.data
        userStep.update({call.message.chat.id: cd})
        first_answer = config.Query_handler["fa_en"]
        global msg
    bot.edit_message_text(text=first_answer , chat_id=msg.chat.id, message_id=msg.message_id)
    msg = None
    # bot.send_message(call.message.chat.id, first_answer)



@bot.message_handler(func=lambda message: True)
def word_search(message):
    cid = message.chat.id
    if cid not in knownUsers:
        knownUsers.append(cid)
        userStep.update({cid:""})
        bot.send_message(message.chat.id, text=config.lang_not_chsn)
        #"New user detected, who hasn't used \"/start\" yet"
    else:
        cd = userStep[cid]
        if str(message.text) == "None" or cd not in sp.lang_list:
            bot.send_sticker(message.chat.id, config.none_text["none_scr_id"])
            bot.send_message(message.chat.id, text=config.lang_not_chsn)
        else:
            second_answer = sp.dict_search(word=message.text, lang= cd)
            if second_answer == "Word_Not_Found":
                second_answer = config.No_Word[("no_{}".format(cd))]
                bot.send_message(message.chat.id, second_answer)
            else:
                bot.send_message(message.chat.id, "{0} {1}".format(config.Yes_Word["yes_{}".format(cd)] , message.text))
                for element in second_answer:
                    bot.send_message(message.chat.id, "<b>" + element.dict_name + "</b>", parse_mode="HTML")
                    if len(element.w_info) > 4096:
                        for x in range(0, len(element.w_info), 4096):
                            bot.send_message(message.chat.id, element.w_info[x:x + 4096])
                    else:
                        bot.send_message(message.chat.id, element.w_info)
                bot.send_message(message.chat.id, text= config.New_Word[("new_{}".format(cd))])
                word_list.clear()
                cd = ""



@server.route('/' + config.TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://bilbotweb-2.herokuapp.com/' + config.TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


# bot.polling() #for local testing