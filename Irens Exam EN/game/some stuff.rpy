screen anticheat:
    if anticheat:
        timer 1 action Hide('anticheat')
    else:
        timer 30 repeat True action Function(renpy.invoke_in_new_context, get_tasklist)
        
screen after_game_stats:
    vbox xpos 0.1 ypos 0.1:
        text 'Question #1:' + ' ' + stat_question1
        text 'Right answer:' + ' ' + stat_answer1
        text 'Question #2:' + ' ' + stat_question2
        text 'Right answer:' + ' ' + stat_answer2
        text 'Question #3:' + ' ' + stat_question3
        text 'Right answer:' + ' ' + stat_answer3
        text 'Question #4:' + ' ' + stat_question4
        text 'Right answer:' + ' ' + stat_answer4
        text 'Question #5:' + ' ' + stat_question5
        text 'Right answer:' + ' ' + stat_answer5
        text 'Question #6:' + ' ' + stat_question6
        text 'Right answer:' + ' ' + stat_answer6
        text 'Question #7:' + ' ' + stat_question7
        text 'Right answer:' + ' ' + stat_answer7
        text 'Question #8:' + ' ' + stat_question8
        text 'Right answer:' + ' ' + stat_answer8
        text 'Number of right answers:' + ' ' + str(mp.right_answers)