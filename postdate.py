#В этом файле ничего не трогаем
#Функции для создания списка всех постов, которые надо опубликовать в этом месяце
import os
import datetime

import contentplan
import function

#Функция,которая создает 2 словаря: Изображения {пост:список изображений к нему} и Тексты {пост:текст к нему}
def file_list(directory):
    files = os.listdir(directory)
    image_name = {}
    text_name = {}
    for f in files:
        dir = os.path.join(directory, f)
        fil = os.listdir(dir)
        for fl in fil:
            if fl.endswith(".txt"):
                fil.remove(fl)
                text_name[f] = fl
        image_name[f] = fil
    return image_name, text_name

#Для наглядности как работает функция
#for book in contentplan.month_book.keys():
    #image_name, text_name = file_list(book)
    #print(image_name, text_name)

#Функция создает список из словарей по каждому посту,
# которые содержат {полный текст поста(вместе с нужными хештеграми), все изображение к посту, время для публикации поста}
def data_for_post(directory,Begindate):
    image_name, text_name = file_list(directory)
    posts_data = []
    for post in image_name.keys():
        time = function.data_unix(Begindate)
        img = []
        try:
            text_file = text_name[post]
            text_url = os.path.join(directory, post, text_file)
            text = contentplan.hashtag[directory] + f'\n\n' + function.text_in_txt(text_url)
        except:
            text = contentplan.hashtag[directory] + f'\n\n'
        date = {'text': text, 'images': img, 'unix_timestamp': time}
        for p in image_name[post]:
            images_dir = os.path.join(directory, post, p)
            img.append(images_dir)
        posts_data.append(date)
        Begindate = Begindate + datetime.timedelta(days=7)
    return posts_data

#Для наглядности как работает функция
#for book in contentplan.month_book.keys():
    #print(data_for_post(book, contentplan.month_book[book]))

def birthday_post(directory):
    image_name, text_name = file_list(directory)
    posts_data = []
    minute = 10
    for post in image_name.keys():
        for p in image_name[post]:
            time = function.data_unix(function.name_day(p,minute))
            images_dir = os.path.join(directory, post, p)
            text = contentplan.hashtag[directory]
            date = {'text': text, 'images': [images_dir], 'unix_timestamp': time}
            posts_data.append(date)
        minute +=2
    return posts_data

#Для наглядности как работает функция
#print(birthday_post(contentplan.directory_birthday))

def all_post():
    posts_data = []
    for book in contentplan.month_book.keys():
        for b in data_for_post(book, contentplan.month_book[book]):
            posts_data.append(b)
    for b in birthday_post(contentplan.directory_birthday):
        posts_data.append(b)
    return posts_data

#Для наглядности как работает функция
#print(all_post())