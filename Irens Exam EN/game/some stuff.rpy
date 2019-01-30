screen anticheat:
    if anticheat:
        timer 1 action Hide('anticheat')
    else:
        timer 30 repeat True action Function(renpy.invoke_in_new_context, get_tasklist)