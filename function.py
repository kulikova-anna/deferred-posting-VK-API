#В этом файле ничего не трогаем
#Дополнительные функции используемые в проекте

import datetime
import os
import requests

import calendar
import locale

import contentplan

#Функция для корректного чтения текстовых файлов
def text_in_txt(url):
    with open(url, encoding='utf-8') as f:
        text = f.read()
    return text
#print(text_in_txt(r'D:\Python\VK_post\month\Книги\книги_1\Текстовый документ.txt'))

#Функция для перевода времени в формат unix(в секундах)___запасная, в программе не используется
def data_unix_str(datetime_string):
    datetime_obj = datetime.datetime.strptime(datetime_string, "%Y-%m-%d %H:%M:%S")
    unix_timestamp = datetime_obj.timestamp()
    return unix_timestamp
#data_unix_str("2025-01-28 12:00:00")

#Функция для перевода времени в формат unix(в секундах), который используется в ВК API
def data_unix(datetime_obj):
    unix_timestamp = datetime_obj.timestamp()
    return unix_timestamp
#data_unix(datetime.datetime(2025, 2, 5, 12, 30, 0))

# Формируем данные параметров для сохранения картинки на сервере
def params_img(photo,image,target_group_id):
    request = requests.post(photo['upload_url'], files={'photo': open(image, "rb")})
    params = {'server': request.json()['server'],
              'photo': request.json()['photo'],
              'hash': request.json()['hash'],
              'group_id': target_group_id}
    return params


#Функция для определения даты публикации поздравительных постов по их названию (соответствует дню публикации)
def name_day(f,minute):
    filename = os.path.splitext(f)[0]
    data = datetime.datetime(contentplan.now_year, contentplan.now_month, int(filename), 8, int(minute), 0)
    return data


#Функция для перевода месяца из числового формата в текстовый
def month_now_and_next():
    locale.setlocale(category=locale.LC_ALL, locale="Russian")
    month_now = calendar.month_name[contentplan.now_month]
    month_next = calendar.month_name[contentplan.now_month+1]
    return month_now,month_next

#Функция, которая выведет все ссылки по тэгу с новой строки
def iteration(all_tag, tag):
    try:
        return "\n".join(all_tag[tag])
    except:
        pass