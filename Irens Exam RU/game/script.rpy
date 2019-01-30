init 2:
    $ irn = Character("Ирен", who_color="#02d9c7")
    $ me = Character("[gg_name]", who_color="#33ff00")
    
label start:
    $ anticheat = False
    $ create_questions()
    $ create_answers()
    $ mp.right_answers = 0
    $ mp.save()
    $ gg_name = renpy.input('Напишите имя для главного героя')
    if gg_name == '':
        $ gg_name = 'Jon'
    "Первая половина учебного дня окончена, настало время перерыва."
    "Я успел пообедать, побеседовать со всеми знакомыми в колледже, узнать расписание семинара на завтра, но всё ещё оставалось куча времени."
    "От нечего делать я направился в кабинет, где должно было состояться следующее занятие."
    "Я вошёл в кабинет, там уже сидела Ирен за своим любимым занятием: чтением."
    "Если меня спросят: 'Кто такая Ирен?', то я отвечу: Ирен - чудо."
    "Красивая, умная, образованная, с хорошим чувством юмора..."
    "В общем, мне повезло иметь такую девушку."
    "Правда она любит во всё внести что-то немножко сумасшедшее, но тем интереснее."
    me "Привет, Ирен!"
    irn "О! Здравствуй-здравствуй."
    me "Тоже заняться нечем?"
    irn "Ну, как нечем… Читаю, вот."
    "Чтение, у неё к этому делу какая-то нездоровая страсть. Я могу предложить кое-что интересное."
    "Памятуя о любви Ирен к разным сумасшествиям, я изрёк:"
    me "Ирен, бросай ты эту книгу и давай раздевайся!"
    irn "Прямо тут?"
    "Ирен захихикала"
    me "Если помнишь, то мы и не в таких местах занимались сексом."
    irn "Твоя правда, но..."
    me "Что?"
    irn "Перед этим ты должен ответить на восемь вопросов."
    me "Ну ё-моё, Ирен..."
    irn "Ну, тогда можешь просто подрочить."
    "Вот умеет она настоять на своём..."
    me "Ладно, давай, всё равно делать нечего."
    jump first_pack_of_questions_first_part
    
label first_pack_of_questions_first_part:
    show screen anticheat
    if correct_answer:
        $ correct_answer = False
        $ final_answer = ''
        $ first_try = True
        $ good_reaction = renpy.random.choice(reactions_on_correct_answer)
        "[good_reaction]"
        jump first_pack_of_questions_second_part
    if first_try:
        $ choice_question()
        "[question]"
        $ choice_answers()
    else:
        $ bad_reaction = renpy.random.choice(reactions_on_incorrect_answer)
        "[bad_reaction]"
        "[question]"
    menu:
        "[answer1]":
            $ final_answer = answer1
            call check_answers
            if first_try:
                jump first_pack_of_questions_first_part
            else:
                jump first_pack_of_questions_first_part
        "[answer2]":   
            $ final_answer = answer2
            call check_answers
            if first_try:
                jump first_pack_of_questions_first_part
            else:
                jump first_pack_of_questions_first_part
        "[answer3]":
            $ final_answer = answer3
            call check_answers
            if first_try:
                jump first_pack_of_questions_first_part
            else:
                jump first_pack_of_questions_first_part
          
label first_pack_of_questions_second_part:
    if correct_answer:
        $ correct_answer = False
        $ final_answer = ''
        $ first_try = True
        $ good_reaction = renpy.random.choice(reactions_on_correct_answer)
        "[good_reaction]"
        jump second_pack_of_questions_first_part
    if first_try:
        $ choice_question()
        "[question]"
        $ choice_answers()
    else:
        $ bad_reaction = renpy.random.choice(reactions_on_incorrect_answer)
        "[bad_reaction]"
        "[question]"
    menu:
        "[answer1]":
            $ final_answer = answer1
            call check_answers
            if first_try:
                jump first_pack_of_questions_second_part
            else:
                jump first_pack_of_questions_second_part
        "[answer2]":
            $ final_answer = answer2
            call check_answers
            if first_try:
                jump first_pack_of_questions_second_part
            else:
                jump first_pack_of_questions_second_part
        "[answer3]":
            $ final_answer = answer3
            call check_answers
            if first_try:
                jump first_pack_of_questions_second_part
            else:
                jump first_pack_of_questions_second_part
    
label second_pack_of_questions_first_part:
    if correct_answer:
        $ correct_answer = False
        $ final_answer = ''
        $ first_try = True
        $ good_reaction = renpy.random.choice(reactions_on_correct_answer)
        "[good_reaction]"
        jump second_pack_of_questions_second_part
    if first_try:
        $ choice_question()
        "[question]"
        $ choice_answers()
    else:
        $ bad_reaction = renpy.random.choice(reactions_on_incorrect_answer)
        "[bad_reaction]"
        "[question]"
    menu:
        "[answer1]":
            $ final_answer = answer1
            call check_answers
            if first_try:
                jump second_pack_of_questions_first_part
            else:
                jump second_pack_of_questions_first_part
        "[answer2]":
            $ final_answer = answer2
            call check_answers
            if first_try:
                jump second_pack_of_questions_first_part
            else:
                jump second_pack_of_questions_first_part
        "[answer3]":
            $ final_answer = answer3
            call check_answers
            if first_try:
                jump second_pack_of_questions_first_part
            else:
                jump second_pack_of_questions_first_part
            
label second_pack_of_questions_second_part:
    if correct_answer:
        $ correct_answer = False
        $ final_answer = ''
        $ first_try = True
        $ good_reaction = renpy.random.choice(reactions_on_correct_answer)
        "[good_reaction]"
        jump third_pack_of_questions_first_part
    if first_try:
        $ choice_question()
        "[question]"
        $ choice_answers()
    else:
        $ bad_reaction = renpy.random.choice(reactions_on_incorrect_answer)
        "[bad_reaction]"
        "[question]"
    menu:
        "[answer1]":
            $ final_answer = answer1
            call check_answers
            if first_try:
                jump second_pack_of_questions_second_part
            else:
                jump second_pack_of_questions_second_part
        "[answer2]":
            $ final_answer = answer2
            call check_answers
            if first_try:
                jump second_pack_of_questions_second_part
            else:
                jump second_pack_of_questions_second_part
        "[answer3]":
            $ final_answer = answer3
            call check_answers
            if first_try:
                jump second_pack_of_questions_second_part
            else:
                jump second_pack_of_questions_second_part
    
label third_pack_of_questions_first_part:
    if correct_answer:
        $ correct_answer = False
        $ final_answer = ''
        $ first_try = True
        $ good_reaction = renpy.random.choice(reactions_on_correct_answer)
        "[good_reaction]"
        jump third_pack_of_questions_second_part
    if first_try:
        $ choice_question()
        "[question]"
        $ choice_answers()
    else:
        $ bad_reaction = renpy.random.choice(reactions_on_incorrect_answer)
        "[bad_reaction]"
        "[question]"
    menu:
        "[answer1]":
            $ final_answer = answer1
            call check_answers
            if first_try:
                jump third_pack_of_questions_first_part
            else:
                jump third_pack_of_questions_first_part
        "[answer2]":
            $ final_answer = answer2
            call check_answers
            if first_try:
                jump third_pack_of_questions_first_part
            else:
                jump third_pack_of_questions_first_part
        "[answer3]":
            $ final_answer = answer3
            call check_answers
            if first_try:
                jump third_pack_of_questions_first_part
            else:
                jump third_pack_of_questions_first_part
            
label third_pack_of_questions_second_part:
    if correct_answer:
        $ correct_answer = False
        $ final_answer = ''
        $ first_try = True
        $ good_reaction = renpy.random.choice(reactions_on_correct_answer)
        "[good_reaction]"
        jump fourth_pack_of_questions_first_part
    if first_try:
        $ choice_question()
        "[question]"
        $ choice_answers()
    else:
        $ bad_reaction = renpy.random.choice(reactions_on_incorrect_answer)
        "[bad_reaction]"
        "[question]"
    menu:
        "[answer1]":
            $ final_answer = answer1
            call check_answers
            if first_try:
                jump third_pack_of_questions_second_part
            else:
                jump third_pack_of_questions_second_part
        "[answer2]":
            $ final_answer = answer2
            call check_answers
            if first_try:
                jump third_pack_of_questions_second_part
            else:
                jump third_pack_of_questions_second_part
        "[answer3]":
            $ final_answer = answer3
            call check_answers
            if first_try:
                jump third_pack_of_questions_second_part
            else:
                jump third_pack_of_questions_second_part
    
label fourth_pack_of_questions_first_part:
    if correct_answer:
        $ correct_answer = False
        $ final_answer = ''
        $ first_try = True
        $ good_reaction = renpy.random.choice(reactions_on_correct_answer)
        "[good_reaction]"
        jump fourth_pack_of_questions_second_part
    if first_try:
        $ choice_question()
        "[question]"
        $ choice_answers()
    else:
        $ bad_reaction = renpy.random.choice(reactions_on_incorrect_answer)
        "[bad_reaction]"
        "[question]"
    menu:
        "[answer1]":
            $ final_answer = answer1
            call check_answers
            if first_try:
                jump fourth_pack_of_questions_first_part
            else:
                jump fourth_pack_of_questions_first_part
        "[answer2]":
            $ final_answer = answer2
            call check_answers
            if first_try:
                jump fourth_pack_of_questions_first_part
            else:
                jump fourth_pack_of_questions_first_part
        "[answer3]":
            $ final_answer = answer3
            call check_answers
            if first_try:
                jump fourth_pack_of_questions_first_part
            else:
                jump fourth_pack_of_questions_first_part
            
label fourth_pack_of_questions_second_part:
    if correct_answer:
        $ correct_answer = False
        $ final_answer = ''
        $ first_try = True
        $ good_reaction = renpy.random.choice(reactions_on_correct_answer)
        "[good_reaction]"
        jump after_exam
    if first_try:   
        $ choice_question()
        "[question]"
        $ choice_answers()
    else:
        $ bad_reaction = renpy.random.choice(reactions_on_incorrect_answer)
        "[bad_reaction]"
        "[question]"
    menu:
        "[answer1]":
            $ final_answer = answer1
            call check_answers
            if first_try:
                jump fourth_pack_of_questions_second_part
            else:
                jump fourth_pack_of_questions_second_part
        "[answer2]":
            $ final_answer = answer2
            call check_answers
            if first_try:
                jump fourth_pack_of_questions_second_part
            else:
                jump fourth_pack_of_questions_second_part
        "[answer3]":
            $ final_answer = answer3
            call check_answers
            if first_try:
                jump fourth_pack_of_questions_second_part
            else:
                jump fourth_pack_of_questions_second_part
            
label after_exam:
    if mp.right_answers == 8:
        "Ну ты и книжный червь! Молодец! Ты заслужил награду..."
    elif mp.right_answers >= 5 and mp.right_answers <= 7:
        "Ну ничего, приемлемо, давай, снимай штаны!"
    elif mp.right_answers >= 3 and mp.right_answers <= 4:
        "Хоть что-то ты знаешь, хотя часть, наверное, угадал, Ладно, фиг с тобой."
    elif mp.right_answers >= 1 and mp.right_answers <= 2:
        "Да чего было от тебя ожидать. Пошли трахаться!"
    elif mp.right_answers == 0:
        "Н-да… Так и быть, будет тебе секс из жалости."
    jump ending

label ending:
    return