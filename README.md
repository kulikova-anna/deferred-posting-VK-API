# deferred-posting-VK-API
Проект для автоматизации работы SMM специалистов по наполнению Сообщества ВК контентом на месяц вперед.

**Задача** – создать удобный для простого обывателя (не програмиста) скрипт, который бы автоматически добавлял подготовленные посты в отложенные записи ВК сообщества.

Скрипт реализован на Python с применением ВК API.

**Описание для простых пользователей:**
В папке **month** размещаем материалы для будущих постов (каждый пост это отдельная папка в которой размещены картинки и текстовый файл)
![image](https://github.com/user-attachments/assets/c007d75e-3b0e-4ecb-a0a9-54741a135829)
![image](https://github.com/user-attachments/assets/f2b8b0c6-c169-4c8d-b18a-fd0b6e889af0)


В файле **contentplan.py** Редактируем папки категорий и хештеги (они автоматически добавляются к тексту поста). 
Также устанавливаем дату и время для первого поста из категории. **Скрипт предназначем для еженедельных рубрик (то есть раз в неделю будет опубликован 1 пост из папки категории начиная с той даты, которую вы указали)**
![image](https://github.com/user-attachments/assets/6544caf2-ff3f-4a93-9e5d-53b97354d509)

**Создфем файл .env с переменными token и target_group_id** –  ваш ключ апи и индификатор собщества в которое мы будем публиковать посты. 
Как получить апи ключ читайте на оф странице ВК АПИ https://dev.vk.com/ru/api/access-token/getting-started (нам нужен Ключ доступа пользователя). Важно, чтобы добавлять посты в сообщество надо иметь права администратора .

После заполнения всего предыдущего запускаем скрипт из файла main.py
