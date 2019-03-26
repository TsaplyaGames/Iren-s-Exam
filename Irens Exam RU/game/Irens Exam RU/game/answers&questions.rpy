init 1 python:  
    
    orig_questions = ["На каких птицах хоббиты вернулись обратно с роковой горы?", "Кто похищал детей в 'Оно' Стивена Кинга?", "Какое прозвище имел Барбридж из Пикника на обочине?",
                      "На какой стороне был Антон Городецкий?", "Кем являлся Тайлер Дёрден из Бойцовского Клуба?", "Как звали главного героя в цикле Метро Дмитрия Глуховского?",
                      "Кому из богов служат безликие из Песни Льда и Огня?", "Как звали главного героя в книге Тёмная Башня Стивена Кинга?", "Как звали монстра из ведьмака, который мог принимать различные облики?",
                      "Какое чудовище было скрыто в Хогвартсе?", "Какова фамилия главного героя 'Мёртвых душ?'", "Скольких человек убил Раскольников?", 
                      "Где спит Ктулху?", "В какой стране происходят действия серии книг о Карлсоне?", "Какой военный конфликт описан в книге 'Унесённые ветром'?",
                      "На какой улице жил Шерлок Холмс?", "Как звали кота Воланда?", "Как называется роман Тургенева, в котором описывается конфликт поколений?",
                      "Сколько основных персонажей в романе Дюма 'Три мушкетёра'?", "Что просил Маленький Принц нарисовать главного героя книги 'Маленький Принц'?"]
                      
    answers = ["Ястребах", "Орлах", "Попугаях", "Акробат", "Фокусник", "Клоун", "Стервятник", "Гриф", "Кондор", "Тёмной", "Светлой", "Сумеречной", "Галлюцинацией",
               "Реальным человеком", "Второй личностью главного героя", "Артур", "Артём", "Андрей", "Рглору", "Семерым", "Многоликому", "Роланд", "Ральф", "Ричард",
               "Мимик", "Допплер", "Ракшаса", "Анаконда", "Василиск", "Кассава", "Чичиков", "Апраскин", "Карамазов", "1", "2", "3", "Средиземное море", "Озеро Лохнесс",
               "Тихий океан", "Россия", "Швеция", "Исландия", "Гражданская война в Америке", "Война за независимость", "Вторая мировая война", "Оксфорд-стрит",
               "Пикадилли", "Бейкер-стрит", "Барсик", "Бегемот", "Слон", "Дворянское Гнездо", "Отцы и дети", "Дым", "Четыре", "Три", "Один", "Удава", "Слона",
               "Барана"]
    
    reactions_on_correct_answer = ['Молодец', 'Какой ты умный...', 'Ммм... Молодец', 'Какой ты у меня начитанный...', 'Ничего себе! И это ты знаешь!', 'В точку!',
                                   'Тебя не проведёшь!', 'Так держать!', 'Отлично! Люблю начитанных...', 'А ты не промах!', 'Божественно!', 'Идеально',
                                   'Тютелька в тютельку!', 'Супер!']
    
    reactions_on_incorrect_answer = ['Хи-хи-хи... Нет!', 'Ты что дурачок?', 'Лол, нет! Ты хоть читать умеешь?', 'Ты книги вообще открываешь?', 
                                     'Ну это как можно не знать?', 'Ты серьёзно? Неправильно!', 'Начитанность - это не про тебя.', 
                                     'Ты знал, что девушки любят умных?', 'Ну ты даёшь...', 'Неужели тебе даже аудиокниги лень слушать?',
                                     'Ха-ха-ха… Ну и ну...', 'Я тебе для чего на день рождения книги дарю?', 'Такой большой, а мозг как у хлебушка...']
                                     
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
        global answers_scheme
        answers_scheme = renpy.random.randint(0, 2)
        if question == orig_questions[0]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[0], answers[1], answers[2]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[2], answers[0], answers[1]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[1], answers[2], answers[0]
        elif question == orig_questions[1]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[3], answers[4], answers[5]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[5], answers[4], answers[3]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[4], answers[5], answers[3]
        elif question == orig_questions[2]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[6], answers[7], answers[8]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[8], answers[7], answers[6]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[7], answers[8], answers[6]
        elif question == orig_questions[3]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[9], answers[10], answers[11]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[11], answers[10], answers[9]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[10], answers[11], answers[9]
        elif question == orig_questions[4]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[12], answers[13], answers[14]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[14], answers[13], answers[12]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[13], answers[14], answers[12]
        elif question == orig_questions[5]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[15], answers[16], answers[17]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[17], answers[16], answers[15]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[16], answers[17], answers[15]
        elif question == orig_questions[6]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[18], answers[19], answers[20]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[20], answers[19], answers[18]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[19], answers[20], answers[18]
        elif question == orig_questions[7]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[21], answers[22], answers[23]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[23], answers[22], answers[21]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[22], answers[23], answers[21]
        elif question == orig_questions[8]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[24], answers[25], answers[26]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[26], answers[25], answers[24]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[25], answers[26], answers[24]
        elif question == orig_questions[9]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[27], answers[28], answers[29]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[29], answers[28], answers[27]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[28], answers[29], answers[27]
        elif question == orig_questions[10]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[30], answers[31], answers[32]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[32], answers[31], answers[30]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[31], answers[32], answers[30]
        elif question == orig_questions[11]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[33], answers[34], answers[35]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[35], answers[34], answers[33]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[34], answers[35], answers[33]
        elif question == orig_questions[12]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[36], answers[37], answers[38]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[38], answers[37], answers[36]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[37], answers[38], answers[36]
        elif question == orig_questions[13]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[39], answers[40], answers[41]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[41], answers[40], answers[39]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[40], answers[41], answers[39]
        elif question == orig_questions[14]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[42], answers[43], answers[44]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[44], answers[43], answers[42]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[43], answers[44], answers[42]
        elif question == orig_questions[15]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[45], answers[46], answers[47]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[47], answers[46], answers[45]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[46], answers[47], answers[45]
        elif question == orig_questions[16]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[48], answers[49], answers[50]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[50], answers[49], answers[48]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[49], answers[50], answers[48]
        elif question == orig_questions[17]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[51], answers[52], answers[53]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[53], answers[52], answers[51]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[52], answers[53], answers[51]
        elif question == orig_questions[18]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[54], answers[55], answers[56]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[56], answers[55], answers[54]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[55], answers[56], answers[54]
        elif question == orig_questions[19]:
            if answers_scheme == 0:
                answer1, answer2, answer3 = answers[57], answers[58], answers[59]
            elif answers_scheme == 1:
                answer1, answer2, answer3 = answers[59], answers[58], answers[57]
            elif answers_scheme == 2:
                answer1, answer2, answer3 = answers[58], answers[59], answers[57]
            
label check_answers:
    if question == orig_questions[0]:
        if final_answer == answers[1]:
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return 
    elif question == orig_questions[1]:
        if final_answer == answers[5]:
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == orig_questions[2]:
        if final_answer == answers[6]:
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == orig_questions[3]:
        if final_answer == answers[10]:
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == orig_questions[4]:
        if final_answer == answers[14]:
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == orig_questions[5]:
        if final_answer == answers[16]:
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == orig_questions[6]:
        if final_answer == answers[20]:
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == orig_questions[7]:
        if final_answer == answers[21]:
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == orig_questions[8]:
        if final_answer == answers[25]:
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
    elif question == orig_questions[9]:
        if final_answer == answers[28]:
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == orig_questions[10]:
        if final_answer == answers[30]:
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == orig_questions[11]:
        if final_answer == answers[34]:
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == orig_questions[12]:
        if final_answer == answers[38]:
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == orig_questions[13]:
        if final_answer == answers[40]:
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
    elif question == orig_questions[14]:
        if final_answer == answers[42]:
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == orig_questions[15]:
        if final_answer == answers[47]:
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == orig_questions[16]:
        if final_answer == answers[49]:
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == orig_questions[17]:
        if final_answer == answers[52]:
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == orig_questions[18]:
        if final_answer == answers[54]:
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
    elif question == orig_questions[19]:
        if final_answer == answers[59]:
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return