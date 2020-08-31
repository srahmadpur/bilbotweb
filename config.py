

#Bot token
TOKEN = "1067624262:AAH9TFrJnoFw-wYH3qmc800Gfr6cdiPuFyE" #Prod Token
#TOKEN = "900555854:AAHN0C6be0zGVU8wlzJQnH7z_xc_y1AOcFc" #Test token

db_url = "postgres://ksiewdkynreeke:02661f9c7b99af0aab8d5dc5c50ec7388a8325ea0f85cad9254d3501682bcffd@ec2-54-247-122-209.eu-west-1.compute.amazonaws.com:5432/d31n2lplt1q8r6"


#Messages

Lang_chose_az = "🌎Zəhmət olmasa axtarış dilini seçin!"
lang_not_chsn = "🌎Atarış dili seçilməyib! Zəhmət olmasa /lang komandası ilə axtarış dilini seçin!"
no_start = "Zəhmət olmasa ilk öncə /start komandasından istifadə edin!"


none_text = {
    "none_scr_id" : "CAACAgIAAxkBAAILTF5FEjDaUtAO2n0qlhh9ZfDkcv_oAAJFAAMh8AQcVEccChUEGqEYBA"
    }



Query_handler = {
    "hello_msg" : "Bildilçin, Sizin üçün axtarar!" ,
    "fa_az" : "🌎Axtarış dili: Azərbaycan🇦🇿"+ "\n" +"Axtarmaq istədiyiniz sözü daxil edin: ",
    "fa_ru" : "🌎Язык поиска: Русский🇷🇺"+ "\n" +"Введите слово, которое вы хотите найти:" ,
    "fa_en" : "🌎Search language: English🇺🇸"+ "\n" +"Enter the word you want to find:" ,
    "fa_" : lang_not_chsn
}


No_Word = {
    "no_az" : "❌Axtardığınız söz tapılmadı! Yeni sözü daxil edin və ya axtarış dilini dəyişmək üçün /lang komandasından istifadə edin!",
    "no_ru" : "❌Слово, которое вы ищете, не найдено! Введите новое слово или используйте команду /lang чтобы изменить язык поиска.",
    "no_en" : "❌The word you are looking for not found! Enter a new word or use the /lang command to change the language."
    }

Yes_Word = {
    "yes_az" : "⬇️Axtarış nəticələri:",
    "yes_ru" : "⬇️Результаты поиска для:",
    "yes_en" : "⬇️Search results for:"
    }


New_Word = {
    "new_az" : "🔄Yeni sözü daxil edin və ya axtarış dilini dəyişmək üçün /lang komandasından istifadə edin!" ,
    "new_ru" : "🔄Введите новое слово или используйте команду /lang чтобы изменить язык поиска!" ,
    "new_en" : "🔄Enter a new word or use the /lang command to change the search language!"
    }
