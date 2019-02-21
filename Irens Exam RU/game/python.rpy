init python:

    mp = MultiPersistent('fivepanties!')
    
    import subprocess
    
    iren_replic = ["Не подглядывать!", "Ты кого обмануть вздумал?", "Обманщик!", "Так нечестно!"]
    
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
    return