from function import month_now_and_next, iteration
month_now, month_next = month_now_and_next()

#В этом файле содержится шаблон текста для поста "Итоги месяца"
#Элементы обернутые в {} вставляются автоматически (месяц и постоянные рубрики)
#При добавлении новых рубрик добавляем сообтветствуюзий текст в шаблон а так же одну из конструкций {}
#{iteration(noTag_post, '#тутнаштег')} - если это не постоянный тег и его нет среди hashtag в файле contentplan
#{iteration(all_post, '#тутнаштег')} - если это постоянная рубрика (создаем соответствующую папку в month и добавляем данные в файл contentplan
def monthpost_text(all_post, noTag_post):
    mes = f'''У нас есть Хорошая и добрая традиция — ежемесячно мы будем напоминать вам о событиях месяца, которые вы могли пропустить.
Итак, {month_now}, поехали! 

🎁Поздравили всех причастных с 

🎉Отпраздновали 

🤔Узнали о 

💡Познакомились с , а ещё узнали 

❓Ответили на вопросы: 

📃Продолжили читать вдохновляющие истории из рубрики #накануне_выходных
{iteration(noTag_post, '#накануне_выходных')}

🤖Познакомились с новыми технологиями Шедевры ИИ #искуственныйинтелект
{iteration(noTag_post, '#искуственныйинтелект')}

📝Становились грамотней с рубрикой #говоримправильно
{iteration(all_post, '#говоримправильно')}

📚Прочитали интересные книги из наших подборок #книжныйсомелье 
{iteration(all_post, '#книжныйсомелье')}

🎬Посмотрели классные фильмы #помощьзала
{iteration(all_post, '#помощьзала')}

🥗Научились готовить вкусные блюда #рецепты
{iteration(all_post, '#рецепты')}

💌Познакомились с цитатами известных людей #легендарныецитаты
{iteration(all_post, '#легендарныецитаты')}

🏴‍☠Узнали новые схемы мошенничества #мошенники
{iteration(all_post, '#мошенники')}

🍁{month_now} закончился, но впереди {month_next}, а это значит, что нас ждет еще много интересного.'''
    return mes

