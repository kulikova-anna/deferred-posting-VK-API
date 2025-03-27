import datetime

#Заменить now_month на текущий месяц, в котором будем выставлять посты
#В month_book при необходимости можем поменять день и время, когда хотим выставлять посты определенной рубрики
#Внимание!Это дни первого поста из цикла, остальные будут публиковаться через неделю в то же время.
#Например если первый пост по дате в понедельник, то и все остальные посты цикла будут публиковаться в понедельник
#При создании новой рубрики добавляем по аналогии папку рубрики в month_book и hashtag(если # не предусмотрен, ставим ' ')

now_month = 3
now_year = 2025

month_book ={
    r".\month\Грамотность" : datetime.datetime(now_year, now_month, 3, 12, 30, 0),
    r".\month\Приведи друга" : datetime.datetime(now_year, now_month, 4, 12, 30, 0),
    r".\month\Советы" : datetime.datetime(now_year, now_month, 5, 12, 30, 0),
    r".\month\Книги" : datetime.datetime(now_year, now_month, 6, 12, 30, 0),
    r".\month\Фильмы" : datetime.datetime(now_year, now_month, 7, 12, 30, 0),
    r".\month\Рецепты" : datetime.datetime(now_year, now_month, 8, 12, 30, 0),
    r".\month\Цитаты" : datetime.datetime(now_year, now_month, 9, 12, 30, 0)
}

hashtag = {
    r".\month\Грамотность" : '#говоримправильно',
    r".\month\Советы" : ' ',
    r".\month\Приведи друга" : ' ',
    r".\month\Книги" : '#книжныйсомелье',
    r".\month\Фильмы" : '#помощьзала',
    r".\month\Рецепты" : '#рецепты',
    r".\month\Цитаты" : '#легендарныецитаты',
    #r".\month\Мошенники" : '#мошенники',
    r".\month\ДР" : '🎁'

}

directory_birthday = r".\month\ДР"
