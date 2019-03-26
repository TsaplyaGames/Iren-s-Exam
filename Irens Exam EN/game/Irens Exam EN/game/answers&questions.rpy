init 1 python:  
    
    orig_questions = ["By which birds did the Hobbits came back from the Doom Mountain?", "Who kidnapped children in Stephen King's 'It'?",
                      "What nickname Barbridge From 'Roadside Picnic' had?", "On which side Anton Gorodetskiy was?", "Who Tyler Derden from the 'Fight Club' was?",
                      "What's name of main character in 'Metro' cycle of Dmitriy Gluhovskiy", "Which of the gods do serve faceless from 'Song of Ice and Fire'?",
                      "What's name of the main character Stephen King's 'Dark Tower'?", "What's name of 'Witcher's' monster, that can transform into different appearances?",
                      "What monster was hidden in Hogwarts?", "What's surname of 'Dead souls' main character?", "How namy people did Raskolnikov killed?",
                      "Where do Ctulhu sleeps?", "In which county do happen book series about Carlson?", "What military conflict described in 'Gone by the wind'?",
                      "On which street did Sherlock Holmes lived?", "What was Voland's cat name?", "What is Turgenev's novel called, where described generation's conflict?",
                      "How many main characters was in 'Three musketeers' novel?", "What do Little Prince asked main character of eponymous book to draw?"] 
                 
    answers = ["By hawks", "By eagles", "By parrots", "Acrobat", "Magician", "Clown", "Vulture", "Griffin", "Condor", "The dark", "The light", "The twilight",
               "Hallucination", "Real person", "The second personality of the main character", "Arthur", "Artyom", "Andrey", "Rglor", "The Seven", "Many-Faced God",
               "Roland", "Ralph", "Richard", "Mimic", "Doppler", "Rakshasa", "Anaconda", "Basilisk", "Cassava", "Chichikov", "Aprsakin", "Karamazow", "1", "2", "3",
               "Mediterranean sea", "Lochness", "Pacific ocean", "Russia", "Sweden", "Iceland", "American civil war", "War for independence", "Second world war",
               "Oxford street", "Piccadilly", "Baker street", "Lucky", "Behemoth", "Elephant", "Noble Nests", "Fathers and children", "Smoke", "Four", "Three",
               "One", "Boa", "Elephant", "Lamb"]
    
    reactions_on_correct_answer = ['Attaboy', 'You are so clever...', 'Hm… Well done', 'You are so well-read...', 'Wow! You know even this!', 'Exactly!',
                                    'You can\'t be fooled!', 'Keep it up!', 'Excellent! I love well-read guys...', 'You are not fool!', 'Divinely!', 'Perfect!'
                                    'On the nose!', 'Super!']
    
    reactions_on_incorrect_answer = ['Ha-ha-ha… Nope!', 'Are you stupid?', 'Lol, no! Can you even read?', 'Do you even open a books?', 
                                     'How is it possible not to know it?', 'Are you serious? Wrong!', 'Well-read - it is not about you', 
                                     'You know, girls love clever guys?', 'Epic fail...', 'You are really too lazy even to listen audiobooks?',
                                     'Ha-ha-ha… well well...', 'What for do I gift you books on your birthday?', 'So big, but your mind is like bread’s one...']
        
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
            
    def stats_questions_answers(num_question):
        global question
        global stat_question1
        global stat_question2
        global stat_question3
        global stat_question4
        global stat_question5
        global stat_question6
        global stat_question7
        global stat_question8
        global stat_answer1
        global stat_answer2
        global stat_answer3
        global stat_answer4
        global stat_answer5
        global stat_answer6
        global stat_answer7
        global stat_answer8
        if num_question == 1:
            stat_question1 = question
            if question == orig_questions[0]:
                stat_answer1 = answers[1]
            elif question == orig_questions[1]:
                stat_answer1 = answers[5]
            elif question == orig_questions[2]:
                stat_answer1 = answers[6]
            elif question == orig_questions[3]:
                stat_answer1 = answers[10]
            elif question == orig_questions[4]:
                stat_answer1 = answers[14]
            elif question == orig_questions[5]:
                stat_answer1 = answers[16]
            elif question == orig_questions[6]:
                stat_answer1 = answers[20]
            elif question == orig_questions[7]:
                stat_answer1 = answers[21]
            elif question == orig_questions[8]:
                stat_answer1 = answers[25]
            elif question == orig_questions[9]:
                stat_answer1 = answers[28]
            elif question == orig_questions[10]:
                stat_answer1 = answers[30]
            elif question == orig_questions[11]:
                stat_answer1 = answers[34]
            elif question == orig_questions[12]:
                stat_answer1 = answers[38]
            elif question == orig_questions[13]:
                stat_answer1 = answers[40]
            elif question == orig_questions[14]: 
                stat_answer1 = answers[42]
            elif question == orig_questions[15]:
                stat_answer1 = answers[47]
            elif question == orig_questions[16]:
                stat_answer1 = answers[49]
            elif question == orig_questions[17]:
                stat_answer1 = answers[52]
            elif question == orig_questions[18]:
                stat_answer1 = answers[54]
            elif question == orig_questions[19]:
                stat_answer1 = answers[59]
        elif num_question == 2:
            stat_question2 = question
            if question == orig_questions[0]:
                stat_answer2 = answers[1]
            elif question == orig_questions[1]:
                stat_answer2 = answers[5]
            elif question == orig_questions[2]:
                stat_answer2 = answers[6]
            elif question == orig_questions[3]:
                stat_answer2 = answers[10]
            elif question == orig_questions[4]:
                stat_answer2 = answers[14]
            elif question == orig_questions[5]:
                stat_answer2 = answers[16]
            elif question == orig_questions[6]:
                stat_answer2 = answers[20]
            elif question == orig_questions[7]:
                stat_answer2 = answers[21]
            elif question == orig_questions[8]:
                stat_answer2 = answers[25]
            elif question == orig_questions[9]:
                stat_answer2 = answers[28]
            elif question == orig_questions[10]:
                stat_answer2 = answers[30]
            elif question == orig_questions[11]:
                stat_answer2 = answers[34]
            elif question == orig_questions[12]:
                stat_answer2 = answers[38]
            elif question == orig_questions[13]:
                stat_answer2 = answers[40]
            elif question == orig_questions[14]: 
                stat_answer2 = answers[42]
            elif question == orig_questions[15]:
                stat_answer2 = answers[47]
            elif question == orig_questions[16]:
                stat_answer2 = answers[49]
            elif question == orig_questions[17]:
                stat_answer2 = answers[52]
            elif question == orig_questions[18]:
                stat_answer2 = answers[54]
            elif question == orig_questions[19]:
                stat_answer2 = answers[59]
        elif num_question == 3:
            stat_question3 = question
            if question == orig_questions[0]:
                stat_answer3 = answers[1]
            elif question == orig_questions[1]:
                stat_answer3 = answers[5]
            elif question == orig_questions[2]:
                stat_answer3 = answers[6]
            elif question == orig_questions[3]:
                stat_answer3 = answers[10]
            elif question == orig_questions[4]:
                stat_answer3 = answers[14]
            elif question == orig_questions[5]:
                stat_answer3 = answers[16]
            elif question == orig_questions[6]:
                stat_answer3 = answers[20]
            elif question == orig_questions[7]:
                stat_answer3 = answers[21]
            elif question == orig_questions[8]:
                stat_answer3 = answers[25]
            elif question == orig_questions[9]:
                stat_answer3 = answers[28]
            elif question == orig_questions[10]:
                stat_answer3 = answers[30]
            elif question == orig_questions[11]:
                stat_answer3 = answers[34]
            elif question == orig_questions[12]:
                stat_answer3 = answers[38]
            elif question == orig_questions[13]:
                stat_answer3 = answers[40]
            elif question == orig_questions[14]: 
                stat_answer3 = answers[42]
            elif question == orig_questions[15]:
                stat_answer3 = answers[47]
            elif question == orig_questions[16]:
                stat_answer3 = answers[49]
            elif question == orig_questions[17]:
                stat_answer3 = answers[52]
            elif question == orig_questions[18]:
                stat_answer3 = answers[54]
            elif question == orig_questions[19]:
                stat_answer3 = answers[59]
        elif num_question == 4: 
            stat_question4 = question
            if question == orig_questions[0]:
                stat_answer4 = answers[1]
            elif question == orig_questions[1]:
                stat_answer4 = answers[5]
            elif question == orig_questions[2]:
                stat_answer4 = answers[6]
            elif question == orig_questions[3]:
                stat_answer4 = answers[10]
            elif question == orig_questions[4]:
                stat_answer4 = answers[14]
            elif question == orig_questions[5]:
                stat_answer4 = answers[16]
            elif question == orig_questions[6]:
                stat_answer4 = answers[20]
            elif question == orig_questions[7]:
                stat_answer4 = answers[21]
            elif question == orig_questions[8]:
                stat_answer4 = answers[25]
            elif question == orig_questions[9]:
                stat_answer4 = answers[28]
            elif question == orig_questions[10]:
                stat_answer4 = answers[30]
            elif question == orig_questions[11]:
                stat_answer4 = answers[34]
            elif question == orig_questions[12]:
                stat_answer4 = answers[38]
            elif question == orig_questions[13]:
                stat_answer4 = answers[40]
            elif question == orig_questions[14]: 
                stat_answer4 = answers[42]
            elif question == orig_questions[15]:
                stat_answer4 = answers[47]
            elif question == orig_questions[16]:
                stat_answer4 = answers[49]
            elif question == orig_questions[17]:
                stat_answer4 = answers[52]
            elif question == orig_questions[18]:
                stat_answer4 = answers[54]
            elif question == orig_questions[19]:
                stat_answer4 = answers[59]
        elif num_question == 5:
            stat_question5 = question
            if question == orig_questions[0]:
                stat_answer5 = answers[1]
            elif question == orig_questions[1]:
                stat_answer5 = answers[5]
            elif question == orig_questions[2]:
                stat_answer5 = answers[6]
            elif question == orig_questions[3]:
                stat_answer5 = answers[10]
            elif question == orig_questions[4]:
                stat_answer5 = answers[14]
            elif question == orig_questions[5]:
                stat_answer5 = answers[16]
            elif question == orig_questions[6]:
                stat_answer5 = answers[20]
            elif question == orig_questions[7]:
                stat_answer5 = answers[21]
            elif question == orig_questions[8]:
                stat_answer5 = answers[25]
            elif question == orig_questions[9]:
                stat_answer5 = answers[28]
            elif question == orig_questions[10]:
                stat_answer5 = answers[30]
            elif question == orig_questions[11]:
                stat_answer5 = answers[34]
            elif question == orig_questions[12]:
                stat_answer5 = answers[38]
            elif question == orig_questions[13]:
                stat_answer5 = answers[40]
            elif question == orig_questions[14]: 
                stat_answer5 = answers[42]
            elif question == orig_questions[15]:
                stat_answer5 = answers[47]
            elif question == orig_questions[16]:
                stat_answer5 = answers[49]
            elif question == orig_questions[17]:
                stat_answer5 = answers[52]
            elif question == orig_questions[18]:
                stat_answer5 = answers[54]
            elif question == orig_questions[19]:
                stat_answer5 = answers[59]
        elif num_question == 6:
            stat_question6 = question
            if question == orig_questions[0]:
                stat_answer6 = answers[1]
            elif question == orig_questions[1]:
                stat_answer6 = answers[5]
            elif question == orig_questions[2]:
                stat_answer6 = answers[6]
            elif question == orig_questions[3]:
                stat_answer6 = answers[10]
            elif question == orig_questions[4]:
                stat_answer6 = answers[14]
            elif question == orig_questions[5]:
                stat_answer6 = answers[16]
            elif question == orig_questions[6]:
                stat_answer6 = answers[20]
            elif question == orig_questions[7]:
                stat_answer6 = answers[21]
            elif question == orig_questions[8]:
                stat_answer6 = answers[25]
            elif question == orig_questions[9]:
                stat_answer6 = answers[28]
            elif question == orig_questions[10]:
                stat_answer6 = answers[30]
            elif question == orig_questions[11]:
                stat_answer6 = answers[34]
            elif question == orig_questions[12]:
                stat_answer6 = answers[38]
            elif question == orig_questions[13]:
                stat_answer6 = answers[40]
            elif question == orig_questions[14]: 
                stat_answer6 = answers[42]
            elif question == orig_questions[15]:
                stat_answer6 = answers[47]
            elif question == orig_questions[16]:
                stat_answer6 = answers[49]
            elif question == orig_questions[17]:
                stat_answer6 = answers[52]
            elif question == orig_questions[18]:
                stat_answer6 = answers[54]
            elif question == orig_questions[19]:
                stat_answer6 = answers[59]
        elif num_question == 7:
            stat_question7 = question
            if question == orig_questions[0]:
                stat_answer7 = answers[1]
            elif question == orig_questions[1]:
                stat_answer7 = answers[5]
            elif question == orig_questions[2]:
                stat_answer7 = answers[6]
            elif question == orig_questions[3]:
                stat_answer7 = answers[10]
            elif question == orig_questions[4]:
                stat_answer7 = answers[14]
            elif question == orig_questions[5]:
                stat_answer7 = answers[16]
            elif question == orig_questions[6]:
                stat_answer7 = answers[20]
            elif question == orig_questions[7]:
                stat_answer7 = answers[21]
            elif question == orig_questions[8]:
                stat_answer7 = answers[25]
            elif question == orig_questions[9]:
                stat_answer7 = answers[28]
            elif question == orig_questions[10]:
                stat_answer7 = answers[30]
            elif question == orig_questions[11]:
                stat_answer7 = answers[34]
            elif question == orig_questions[12]:
                stat_answer7 = answers[38]
            elif question == orig_questions[13]:
                stat_answer7 = answers[40]
            elif question == orig_questions[14]: 
                stat_answer7 = answers[42]
            elif question == orig_questions[15]:
                stat_answer7 = answers[47]
            elif question == orig_questions[16]:
                stat_answer7 = answers[49]
            elif question == orig_questions[17]:
                stat_answer7 = answers[52]
            elif question == orig_questions[18]:
                stat_answer7 = answers[54]
            elif question == orig_questions[19]:
                stat_answer7 = answers[59]
        elif num_question == 8:
            stat_question8 = question
            if question == orig_questions[0]:
                stat_answer8 = answers[1]
            elif question == orig_questions[1]:
                stat_answer8 = answers[5]
            elif question == orig_questions[2]:
                stat_answer8 = answers[6]
            elif question == orig_questions[3]:
                stat_answer8 = answers[10]
            elif question == orig_questions[4]:
                stat_answer8 = answers[14]
            elif question == orig_questions[5]:
                stat_answer8 = answers[16]
            elif question == orig_questions[6]:
                stat_answer8 = answers[20]
            elif question == orig_questions[7]:
                stat_answer8 = answers[21]
            elif question == orig_questions[8]:
                stat_answer8 = answers[25]
            elif question == orig_questions[9]:
                stat_answer8 = answers[28]
            elif question == orig_questions[10]:
                stat_answer8 = answers[30]
            elif question == orig_questions[11]:
                stat_answer8 = answers[34]
            elif question == orig_questions[12]:
                stat_answer8 = answers[38]
            elif question == orig_questions[13]:
                stat_answer8 = answers[40]
            elif question == orig_questions[14]: 
                stat_answer8 = answers[42]
            elif question == orig_questions[15]:
                stat_answer8 = answers[47]
            elif question == orig_questions[16]:
                stat_answer8 = answers[49]
            elif question == orig_questions[17]:
                stat_answer8 = answers[52]
            elif question == orig_questions[18]:
                stat_answer8 = answers[54]
            elif question == orig_questions[19]:
                stat_answer8 = answers[59]
                
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