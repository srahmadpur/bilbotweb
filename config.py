

#Bot token
TOKEN = "1067624262:AAH9TFrJnoFw-wYH3qmc800Gfr6cdiPuFyE" #testbot token
db_url = "postgres://hcvxqacgcfcwlq:a3b2574c302ae00f0f317dcae258616ef941cf66b6957809a783003e10fd73a2@ec2-54-195-247-108.eu-west-1.compute.amazonaws.com:5432/ddupt842p792lv"


#Messages

Lang_chose_az = "Zəhmət olmasa axtarış dilini seçin!"
lang_not_chsn = "Atarış dili seçilməyib! Zəhmət olmasa /lang komandası ilə axtarış dilini seçin!"
no_start = "Zəhmət olmasa ilk öncə /start komandasından istifadə edin!"


none_text = {
    "none_scr_id" : "CAACAgIAAxkBAAILTF5FEjDaUtAO2n0qlhh9ZfDkcv_oAAJFAAMh8AQcVEccChUEGqEYBA"
    }



Query_handler = {
    "hello_msg" : "Bildilçin, Sizin üçün axtarar!" ,
    "fa_az" : "Axtarmaq istədiyiniz sözü daxil edin:" ,
    "fa_ru" : "Введите слово, которое вы хотите найти:" ,
    "fa_en" : "Enter the word you want to find:" ,
    "fa_" : lang_not_chsn
}


No_Word = {
    "no_az" : "Axtardığınız söz tapılmadı! Yeni sözü daxil edin və ya axtarış dilini dəyişmək üçün /lang komandasından istifadə edin!",
    "no_ru" : "Слово, которое вы ищете, не найдено! Введите новое слово или используйте команду /lang чтобы изменить язык поиска.",
    "no_en" : "The word you are looking for not found! Enter a new word or use the /lang command to change the language."
    }

Yes_Word = {
    "yes_az" : "Axtarış nəticələri:",
    "yes_ru" : "Результаты поиска для:",
    "yes_en" : "Search results for:"
    }


New_Word = {
    "new_az" : "Yeni sözü daxil edin və ya axtarış dilini dəyişmək üçün /lang komandasından istifadə edin!" ,
    "new_ru" : "Введите новое слово или используйте команду /lang чтобы изменить язык поиска!" ,
    "new_en" : "Enter a new word or use the /lang command to change the search language!"
    }
