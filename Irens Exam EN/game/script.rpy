init 2:
    $ irn = Character("Iren", who_color="#02d9c7")
    $ me = Character("[gg_name]", who_color="#33ff00")
    
label start:
    $ anticheat = False
    $ create_questions()
    $ create_answers()
    $ mp.right_answers = 0
    $ mp.save()
    $ gg_name = renpy.input('Write name for gg')
    if gg_name == '':
        $ gg_name = 'Jon'
    "Half of the studying day is over, it’s time for a break."
    "I had a lunch, talked with all college familiars, found out tomorrow's workshop, but many time still left."
    "Having nothing to do, I went to the cabinet, where the next lesson would be."
    "I entered the cabinet, Irene had already sat there doing her favorite occupation: reading."
    "If someone asks me: 'Who is Irene?', I will answer: 'Irene is a miracle.'"
    "Beautiful, clever, well-educated, has a good sense of humor..."
    "So, I am lucky to have such a girlfriend."
    "Actually she loves to add something crazy to anything, but that’s interesting."
    me "Hi, Irene!"
    irn "Oh! Hi-hi."
    me "You also have nothing to do?"
    irn "Why? I am reading."
    "Reading, She has unhealthy passion to this thing. I can offer something more interesting."
    "Knowing Iren’s love to crazy things, I said:"
    me "Irene, Drop reading and take of your clothes!"
    irn "Right there?"
    "Irene laughed"
    me "If you remember, we had sex in the more strange places."
    irn "You are right, but..."
    me "What?"
    irn "Before you have to answer eight literature questions."
    me "God damn it, Irene..."
    irn "So, you can just fap."
    "She can insist on her..."
    me "Okay, let’s do it, in any case I have nothing to do."
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
        "You are really bookworm! Well done! You deserved some reward..."
    elif mp.right_answers >= 5 and mp.right_answers <= 7:
        "Okay then, acceptable. Take off your pants."
    elif mp.right_answers >= 3 and mp.right_answers <= 4:
        "You know something, but, I think, you guessed some. Okay, I don’t care."
    elif mp.right_answers >= 1 and mp.right_answers <= 2:
        "What did I expected from you? Let’s fuck!"
    elif mp.right_answers == 0:
        "Well-well… Alright you will get sex, because I feel pity to you."
    jump ending

label ending:
    return