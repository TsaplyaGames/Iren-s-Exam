init 1 python:  
    
    final_answer = False
    correct_answer = False
    first_try = True
    
    reactions_on_correct_answer = ['Attaboy', 'You are so clever...', 'Hm… Well done', 'You are so well-read...', 'Wow! You know even this!', 'Exactly!',
                                    'You can\'t be fooled!', 'Keep it up!', 'Excellent! I love well-read guys...', 'You are not fool!', 'Divinely!', 'Perfect!'
                                    'On the nose!', 'Super!']
    
    reactions_on_incorrect_answer = ['Ha-ha-ha… Nope!', 'Are you stupid?', 'Lol, no! Can you even read?', 'Do you even open a books?', 
                                     'How is it possible not to know it?', 'Are you serious? Wrong!', 'Well-read - it is not about you', 
                                     'You know, girls love clever guys?', 'Epic fail...', 'You are really too lazy even to listen audiobooks?',
                                     'Ha-ha-ha… well well...', 'What for do I gift you books on your birthday?', 'So big, but your mind is like bread’s one...']
    
    def create_questions():
        global questions
        questions = []
        questions.append("By which birds did the Hobbits came back from the Doom Mountain?")
        questions.append("Who kidnapped children in Stephen King's 'It'?")
        questions.append("What nickname Barbridge From 'Roadside Picnic' had?")
        questions.append("On which side Anton Gorodetskiy was?")
        questions.append("Who Tyler Derden from the 'Fight Club' was?")
        questions.append("What's name of main character in 'Metro' cycle of Dmitriy Gluhovskiy")
        questions.append("Which of the gods do serve faceless from 'Song of Ice and Fire'?")
        questions.append("What's name of the main character Stephen King's 'Dark Tower'?")
        questions.append("What's name of 'Witcher's' monster, that can transform into different appearances?")
        questions.append("What monster was hidden in Hogwarts?")
        questions.append("What's surname of 'Dead souls' main character?")
        questions.append("How namy people did Raskolnikov killed?")
        questions.append("Where do Ctulhu sleeps?")
        questions.append("In which county do happen book series about Carlson?")
        questions.append("What military conflict described in 'Gone by the wind'?")
        questions.append("On which street did Sherlock Holmes lived?")
        questions.append("What was Voland's cat name?")
        questions.append("What is Turgenev's novel called, where described generation's conflict?")
        questions.append("How many main characters was in 'Three musketeers' novel?")
        questions.append("What do Little Prince asked main character of eponymous book to draw?")
        
    def create_answers():
        global answers
        answers = []
        answers.append("By hawks")
        answers.append("By eagles")
        answers.append("By parrots")
        answers.append("Acrobat")
        answers.append("Magician")
        answers.append("Clown")
        answers.append("Vulture")
        answers.append("Griffin")
        answers.append("Condor")
        answers.append("The dark")
        answers.append("The light")
        answers.append("The twilight")
        answers.append("Hallucination")
        answers.append("Real person")
        answers.append("The second personality of the main character")
        answers.append("Arthur")
        answers.append("Artyom")
        answers.append("Andrey")
        answers.append("Rglor")
        answers.append("The Seven")
        answers.append("Many-Faced God")
        answers.append("Roland")
        answers.append("Ralph")
        answers.append("Richard")
        answers.append("Mimic")
        answers.append("Doppler")
        answers.append("Rakshasa")
        answers.append("Anaconda")
        answers.append("Basilisk")
        answers.append("Cassava")
        answers.append("Chichikov")
        answers.append("Aprsakin")
        answers.append("Karamazow")
        answers.append("1")
        answers.append("2")
        answers.append("3")
        answers.append("Mediterranean sea")
        answers.append("Lochness")
        answers.append("Pacific ocean")
        answers.append("Russia")
        answers.append("Sweden")
        answers.append("Iceland")
        answers.append("American civil war")
        answers.append("War for independence")
        answers.append("Second world war")
        answers.append("Oxford street")
        answers.append("Piccadilly")
        answers.append("Baker street")
        answers.append("Lucky")
        answers.append("Behemoth")
        answers.append("Elephant")
        answers.append("Noble Nests")
        answers.append("Fathers and children")
        answers.append("Smoke")
        answers.append("Four")
        answers.append("Three")
        answers.append("One")
        answers.append("Boa")
        answers.append("Elephant")
        answers.append("Lamb")
        
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
        if question == "By which birds did the Hobbits came back from the Doom Mountain?":
            answer1 = answers[0]
            answer2 = answers[1]
            answer3 = answers[2]
        elif question == "Who kidnapped children in Stephen King's 'It'?":
            answer1 = answers[3]
            answer2 = answers[4]
            answer3 = answers[5]
        elif question == "What nickname Barbridge From 'Roadside Picnic' had?":
            answer1 = answers[6]
            answer2 = answers[7]
            answer3 = answers[8]
        elif question == "On which side Anton Gorodetskiy was?":
            answer1 = answers[9]
            answer2 = answers[10]
            answer3 = answers[11]
        elif question == "Who Tyler Derden from the 'Fight Club' was?":
            answer1 = answers[12]
            answer2 = answers[13]
            answer3 = answers[14]
        elif question == "What's name of main character in 'Metro' cycle of Dmitriy Gluhovskiy":
            answer1 = answers[15]
            answer2 = answers[16]
            answer3 = answers[17]
        elif question == "Which of the gods do serve faceless from 'Song of Ice and Fire'?":
            answer1 = answers[18]
            answer2 = answers[19]
            answer3 = answers[20]
        elif question == "What's name of the main character Stephen King's 'Dark Tower'?":
            answer1 = answers[21]
            answer2 = answers[22]
            answer3 = answers[23]
        elif question == "What's name of 'Witcher's' monster, that can transform into different appearances?":
            answer1 = answers[24]
            answer2 = answers[25]
            answer3 = answers[26]
        elif question == "What monster was hidden in Hogwarts?":
            answer1 = answers[27]
            answer2 = answers[28]
            answer3 = answers[29]
        elif question == "What's surname of 'Dead souls' main character?":
            answer1 = answers[30]
            answer2 = answers[31]
            answer3 = answers[32]
        elif question == "How namy people did Raskolnikov killed?":
            answer1 = answers[33]
            answer2 = answers[34]
            answer3 = answers[35]
        elif question == "Where do Ctulhu sleeps?":
            answer1 = answers[36]
            answer2 = answers[37]
            answer3 = answers[38]
        elif question == "In which county do happen book series about Carlson?":
            answer1 = answers[39]
            answer2 = answers[40]
            answer3 = answers[41]
        elif question == "What military conflict described in 'Gone by the wind'?":
            answer1 = answers[42]
            answer2 = answers[43]
            answer3 = answers[44]
        elif question == "On which street did Sherlock Holmes lived?":
            answer1 = answers[45]
            answer2 = answers[46]
            answer3 = answers[47]
        elif question == "What was Voland's cat name?":
            answer1 = answers[48]
            answer2 = answers[49]
            answer3 = answers[50]
        elif question == "What is Turgenev's novel called, where described generation's conflict?":
            answer1 = answers[51]
            answer2 = answers[52]
            answer3 = answers[53]
        elif question == "How many main characters was in 'Three musketeers' novel?":
            answer1 = answers[54]
            answer2 = answers[55]
            answer3 = answers[56]
        elif question == "What do Little Prince asked main character of eponymous book to draw?":
            answer1 = answers[57]
            answer2 = answers[58]
            answer3 = answers[59]
            
label check_answers:
    if question == "By which birds did the Hobbits came back from the Doom Mountain?":
        if final_answer == "By eagles":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return 
    elif question == "Who kidnapped children in Stephen King's 'It'?":
        if final_answer == "Clown":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "What nickname Barbridge From 'Roadside Picnic' had?":
        if final_answer == "Vulture":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "On which side Anton Gorodetskiy was?":
        if final_answer == "The light":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "Who Tyler Derden from the 'Fight Club' was?":
        if final_answer == "The second personality of the main character":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "What's name of main character in 'Metro' cycle of Dmitriy Gluhovskiy":
        if final_answer == "Artyom":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "Which of the gods do serve faceless from 'Song of Ice and Fire'?":
        if final_answer == "Many-Faced God":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "What's name of the main character Stephen King's 'Dark Tower'?":
        if final_answer == "Roland":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "What's name of 'Witcher's' monster, that can transform into different appearances?":
        if final_answer == "Doppler":
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
    elif question == "What monster was hidden in Hogwarts?":
        if final_answer == "Basilisk":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "What's surname of 'Dead souls' main character?":
        if final_answer == "Chichikov":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "How namy people did Raskolnikov killed?":
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
    elif question == "Where do Ctulhu sleeps?":
        if final_answer == "Pacific ocean":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "In which county do happen book series about Carlson?":
        if final_answer == "Sweden":
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
    elif question == "What military conflict described in 'Gone by the wind'?":
        if final_answer == "American civil war":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "On which street did Sherlock Holmes lived?":
        if final_answer == "Baker street":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "What was Voland's cat name?":
        if final_answer == "Behemoth":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "What is Turgenev's novel called, where described generation's conflict?":
        if final_answer == "Fathers and children":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return
    elif question == "How many main characters was in 'Three musketeers' novel?":
        if final_answer == "Four":
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
    elif question == "What do Little Prince asked main character of eponymous book to draw?":
        if final_answer == "Lamb":
            $ correct_answer = True
            if first_try:
                if not anticheat:
                    $ mp.right_answers += 1
                    $ mp.save()
            return
        else:
            $ first_try = False
            return