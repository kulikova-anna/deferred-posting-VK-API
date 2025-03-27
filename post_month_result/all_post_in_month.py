#В этом файле ничего не трогаем
#Результаты выполнения копируем для создания поста Итоги месяца
import datetime
from pathlib import Path

from vk_api import VkApi

import contentplan
import key
import text_monthresult

#Часть с подключением API
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("token")
target_group_id = os.getenv("target_group_id")

# token = key.token
# target_group_id = key.target_group_id
vk_session = VkApi(token=token)
vk = vk_session.get_api()

#Получаем список из 100(максимальное число) опубликованных постов из сообщества
response = vk.wall.get(owner_id=f"-{target_group_id}", count=100, filter='owner')

tag_and_post = {} #постоянные рубрики
notag_post={} #остальные посты

for tag in contentplan.hashtag.values():
    tag_and_post[tag]=[]

for post in response['items']:
    date = datetime.datetime.fromtimestamp(post['date'])
    print(date)
    if date.month == contentplan.now_month:
        post_url = f"https://vk.com/wall-{target_group_id}_{post['id']}"
        notag_post[post_url] = post['text']
        # print(f"пост {post['id']} опубликован {date}")
        # print(post['text'])
        for value in contentplan.hashtag.values():
            # print(value)
            if value != ' ' and value in post['text']:
                tag_and_post[value].append(post_url)
                del notag_post[post_url]
                break
            else:
                pass
    else:
        print('error', f"https://vk.com/wall-{target_group_id}_{post['id']}")

#print(tag_and_post)
#print(notag_post)

print('---Посты без #---')
for key, values in notag_post.items():
    print(f'{key} - {values.replace("\n\n"," ")}')

text_mes= text_monthresult.monthpost_text(tag_and_post, notag_post)
print('---Текст для поста Итоги месяца---')
print(text_mes)