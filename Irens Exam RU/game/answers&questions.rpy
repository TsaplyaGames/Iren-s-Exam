init 1 python:  
    
    final_answer = False
    correct_answer = False
    first_try = True
    
    reactions_on_correct_answer = ['Молодец', 'Какой ты умный...', 'Ммм... Молодец', 'Какой ты у меня начитанный...', 'Ничего себе! И это ты знаешь!', 'В точку!',
                                   'Тебя не проведёшь!', 'Так держать!', 'Отлично! Люблю начитанных...', 'А ты не промах!', 'Божественно!', 'Идеально'
                                   'Тютелька в тютельку!', 'Супер!']
    
    reactions_on_incorrect_answer = ['Хи-хи-хи... Нет!', 'Ты что дурачок?', 'Лол, нет! Ты хоть читать умеешь?', 'Ты книги вообще открываешь?', 
                                     'Ну это как можно не знать?', 'Ты серьёзно? Неправильно!', 'Начитанность - это не про тебя.', 
                                     'Ты знал, что девушки любят умных?', 'Ну ты даёшь...', 'Неужели тебе даже аудиокниги лень слушать?',
                                     'Ха-ха-ха… Ну и ну...', 'Я тебе для чего на день рождения книги дарю?', 'Такой большой, а мозг как у хлебушка...']
    
    def create_questions():
        global questions
        questions = []
        questions.append("На каких птицах хоббиты вернулись обратно с роковой горы?")
        questions.append("Кто похищал детей в 'Оно' Стивена Кинга?")
        questions.append("Какое прозвище имел Барбридж из Пикника на обочине?")
        questions.append("На какой стороне был Антон Городецкий?")
        questions.append("Кем являлся Тайлер Дёрден из Бойцовского Клуба?")
        questions.append("Как звали главного героя в цикле Метро Дмитрия Глуховского?")
        questions.append("Кому из богов служат безликие из Песни Льда и Огня?")
        questions.append("Как звали главного героя в книге Тёмная Башня Стивена Кинга?")
        questions.append("Как звали монстра из ведьмака, который мог принимать различные облики?")
        questions.append("Какое чудовище было скрыто в Хогвартсе?")
        questions.append("Какова фамилия главного героя 'Мёртвых душ?'")
        questions.append("Скольких человек убил Раскольников?")
        questions.append("Где спит Ктулху?")
        questions.append("В какой стране происходят действия серии книг о Карлсоне?")
        questions.append("Какой военный конфликт описан в книге 'Унесённые ветром'?")
        questions.append("На какой улице жил Шерлок Холмс?")
        questions.append("Как звали кота Воланда?")
        questions.append("Как называется роман Тургенева, в котором описывается конфликт поколений?")
        questions.append("Сколько основных персонажей в романе Дюма 'Три мушкетёра'?")
        questions.append("Что просил Маленький Принц нарисовать главного героя книги 'Маленький Принц'?")
        
    def create_answers():
        global answers
        answers = []
        answers.append("Ястребах")
        answers.append("Орлах")
        answers.append("Попугаях")
        answers.append("Акробат")
        answers.append("Фокусник")
        answers.append("Клоун")
        answers.append("Стервятник")
        answers.append("Гриф")
        answers.append("Кондор")
        answers.append("Тёмной")
        answers.append("Светлой")
        answers.append("Сумеречной")
        answers.append("Галлюцинацией")
        answers.append("Реальным человеком")
        answers.append("Второй личностью главного героя")
        answers.append("Артур")
        answers.append("Артём")
        answers.append("Андрей")
        answers.append("Рглору")
        answers.append("Семерым")
        answers.append("Многоликому")
        answers.append("Роланд")
        answers.append("Ральф")
        answers.append("Ричард")
        answers.append("Мимик")
        answers.append("Допплер")
        answers.append("Ракшаса")
        answers.append("Анаконда")
        answers.append("Василиск")
        answers.append("Кассава")
        answers.append("Чичиков")
        answers.append("Апраскин")
        answers.append("Карамазов")
        answers.append("1")
        answers.append("2")
        answers.append("3")
        answers.append("Средиземное море")
        answers.append("Озеро Лохнесс")
        answers.append("Тихий океан")
        answers.append("Россия")
        answers.append("Швеция")
        answers.append("Исландия")
        answers.append("Гражданская война в Америке")
        answers.append("Война за независимость")
        answers.append("Вторая мировая война")
        answers.append("Оксфорд-стрит")
        answers.append("Пикадилли")
        answers.append("Бейкер-стрит")
        answers.append("Барсик")
        answers.append("Бегемот")
        answers.append("Слон")
        answers.append("Дворянское Гнездо")
        answers.append("Отцы и дети")
        answers.append("Дым")
        answers.append("Четыре")
        answers.append("Три")
        answers.append("Один")
        answers.append("Удава")
        answers.append("Слона")
        answers.append("Барана")
        
    def choice_question():
        global questions
        global question
        question = renpy.random.choice(questions)
        questions.remove(question)
        
    def choice_answers():
        global question
        global answers 
        global answer1
        global answer2
        global answer3
        if question == "На каких птицах хоббиты вернулись обратно с роковой горы?":
            answer1 = answers[0]
            answer2 = answers[1]
            answer3 = answers[2]
        elif question == "Кто похищал детей в 'Оно' Стивена Кинга?":
            answer1 = answers[3]
            answer2 = answers[4]
            answer3 = answers[5]
        elif question == "Какое прозвище имел Барбридж из Пикника на обочине?":
            answer1 = answers[6]
            answer2 = answers[7]
            answer3 = answers[8]
        elif question == "На какой стороне был Антон Городецкий?":
            answer1 = answers[9]
            answer2 = answers[10]
            answer3 = answers[11]
        elif question == "Кем являлся Тайлер Дёрден из Бойцовского Клуба?":
            answer1 = answers[12]
            answer2 = answers[13]
            answer3 = answers[14]
        elif question == "Как звали главного героя в цикле Метро Дмитрия Глуховского?":
            answer1 = answers[15]
            answer2 = answers[16]
            answer3 = answers[17]
        elif question == "Кому из богов служат безликие из Песни Льда и Огня?":
            answer1 = answers[18]
            answer2 = answers[19]
            answer3 = answers[20]
        elif question == "Как звали главного героя в книге Тёмная Башня Стивена Кинга?":
            answer1 = answers[21]
            answer2 = answers[22]
            answer3 = answers[23]
        elif question == "Как звали монстра из ведьмака, который мог принимать различные облики?":
            answer1 = answers[24]
            answer2 = answers[25]
            answer3 = answers[26]
        elif question == "Какое чудовище было скрыто в Хогвартсе?":
            answer1 = answers[27]
            answer2 = answers[28]
            answer3 = answers[29]
        elif question == "Какова фамилия главного героя 'Мёртвых душ'?":
            answer1 = answers[30]
            answer2 = answers[31]
            answer3 = answers[32]
        elif question == "Скольких человек убил Раскольников?":
            answer1 = answers[33]
            answer2 = answers[34]
            answer3 = answers[35]
        elif question == "Где спит Ктулху?":
            answer1 = answers[36]
            answer2 = answers[37]
            answer3 = answers[38]
        elif question == "В какой стране происходят действия серии книг о Карлсоне?":
            answer1 = answers[39]
            answer2 = answers[40]
            answer3 = answers[41]
        elif question == "Какой военный конфликт описан в книге 'Унесённые ветром'?":
            answer1 = answers[42]
            answer2 = answers[43]
            answer3 = answers[44]
        elif question == "На какой улице жил Шерлок Холмс?":
            answer1 = answers[45]
            answer2 = answers[46]
            answer3 = answers[47]
        elif question == "Как звали кота Воланда?":
            answer1 = answers[48]
            answer2 = answers[49]
            answer3 = answers[50]
        elif question == "Как называется роман Тургенева, в котором описывается конфликт поколений?":
            answer1 = answers[51]
            answer2 = answers[52]
            answer3 = answers[53]
        elif question == "Сколько основных персонажей в романе Дюма 'Три мушкетёра'?":
            answer1 = answers[54]
            answer2 = answers[55]
            answer3 = answers[56]
        elif question == "Что просил Маленький Принц нарисовать главного героя книги 'Маленький Принц'?":
            answer1 = answers[57]
            answer2 = answers[58]
            answer3 = answers[59]
            
label check_answers:
    if question == "На каких птицах хоббиты вернулись обратно с роковой горы?":
        if final_answer == "Орлах":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return 
    elif question == "Кто похищал детей в 'Оно' Стивена Кинга?":
        if final_answer == "Клоун":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "Какое прозвище имел Барбридж из Пикника на обочине?":
        if final_answer == "Стервятник":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "На какой стороне был Антон Городецкий?":
        if final_answer == "Светлой":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "Кем являлся Тайлер Дёрден из Бойцовского Клуба?":
        if final_answer == "Второй личностью главного героя":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "Как звали главного героя в цикле Метро Дмитрия Глуховского?":
        if final_answer == "Артём":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "Кому из богов служат безликие из Песни Льда и Огня?":
        if final_answer == "Многоликому":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "Как звали главного героя в книге Тёмная Башня Стивена Кинга?":
        if final_answer == "Роланд":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "Как звали монстра из ведьмака, который мог принимать различные облики?":
        if final_answer == "Допплер":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            $ final_answer = True
            return
        else:
            $ first_try = False
            return
    elif question == "Какое чудовище было скрыто в Хогвартсе?":
        if final_answer == "Василиск":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "Какова фамилия главного героя 'Мёртвых душ?'":
        if final_answer == "Чичиков":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "Скольких человек убил Раскольников?":
        if final_answer == "2":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "Где спит Ктулху?":
        if final_answer == "Тихий океан":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "В какой стране происходят действия серии книг о Карлсоне?":
        if final_answer == "Швеция":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            $ final_answer = True
            return
        else:
            $ first_try = False
            return
    elif question == "Какой военный конфликт описан в книге 'Унесённые ветром'?":
        if final_answer == "Гражданская война в Америке":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "На какой улице жил Шерлок Холмс?":
        if final_answer == "Бейкер-стрит":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "Как звали кота Воланда?":
        if final_answer == "Бегемот":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "Как называется роман Тургенева, в котором описывается конфликт поколений?":
        if final_answer == "Отцы и дети":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "Сколько основных персонажей в романе Дюма 'Три мушкетёра'?":
        if final_answer == "Четыре":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            $ final_answer = True
            return
        else:
            $ first_try = False
            return
    elif question == "Что просил Маленький Принц нарисовать главного героя книги 'Маленький Принц'?":
        if final_answer == "Барана":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return