init python:

    mp = MultiPersistent('fivepanties!')
    
    import subprocess
    
    iren_replic = ["Don't peep!", "Who are you trying to fool?", "Cheater!", "This is dishonest!"]
    
    def get_tasklist():
        global anticheat
        global mp
        s = subprocess.check_output('tasklist', shell = True)
        if 'chrome.exe' or 'opera.exe' or 'firefox.exe' or 'iexplore.exe' or 'browser.exe' or 'MicrosoftEdge.exe' or 'tor.exe' in s:
            anticheat = True
            mp.right_answers = 0
            mp.save()
            return renpy.say(irn, renpy.random.choice(iren_replic))
            
label load_stuff:
    
    $ questions = orig_questions[:]
    $ final_answer = False
    $ correct_answer = False
    $ first_try = True
    $ anticheat = False
    $ answers_scheme = 0
    $ stat_question1 = ''
    $ stat_question2 = ''
    $ stat_question3 = ''
    $ stat_question4 = ''
    $ stat_question5 = ''
    $ stat_question6 = ''
    $ stat_question7 = ''
    $ stat_question8 = ''
    $ stat_answer1 = ''
    $ stat_answer2 = ''
    $ stat_answer3 = ''
    $ stat_answer4 = ''
    $ stat_answer5 = ''
    $ stat_answer6 = ''
    $ stat_answer7 = ''
    $ stat_answer8 = ''
    return