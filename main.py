import os
from dotenv import load_dotenv, dotenv_values

from vk_api import VkApi
from vk_api.exceptions import ApiError

import time

import function
import postdate
import contentplan

load_dotenv()


# Ваш токен доступа
token =os.getenv("token")

# ID сообщества или пользователя, на стену которого вы хотите опубликовать пост
target_group_id = os.getenv("target_group_id")

# Создаем объект VKSession
vk_session = VkApi(token=token)

# Получаем объект VK_API
vk = vk_session.get_api()

#posts_data = postdate.all_post()
posts_data =postdate.birthday_post(contentplan.directory_birthday)
error_post = []

for post in posts_data:
    print('перерыв')
    time.sleep(7)
    try:
        attachments = []
        text = post['text']
        unix_time = post['unix_timestamp']
        for image in post['images']:
            print(image)
            photo = vk.photos.getWallUploadServer(group_id=target_group_id)
            params = function.params_img(photo, image, target_group_id)
            photo_id = vk.photos.saveWallPhoto(**params)[0]
            attachments.append(f"photo{photo_id['owner_id']}_{photo_id['id']}")
        # Постинг на стену сообщества
        response = vk.wall.post(owner_id=f"-{target_group_id}", from_group='1', message=text,
                                attachments=','.join(attachments), publish_date=int(unix_time))

        # Вывод информации о созданном посте
        print(f"Пост успешно создан. ID поста: {response['post_id']}")

    except ApiError as e:
        print(f"Ошибка VK API: {e}")
        error_post.append(post['images'])
        pass

print('Неопубликовано:')
for e in error_post:
    print(e)
