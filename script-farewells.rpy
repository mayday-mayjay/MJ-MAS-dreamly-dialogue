init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_mj_dd_thundering",
            prompt="It´s thundering.",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_mj_dd_thundering:
    m 1ekc "Oh..."
    m 1eka "Thanks for letting me know, [player]!"
    m 2ekc "Please, be safe..."
    m 2ekc "...and if you happen to need to get out of your home, try to avoid lighting as much as you can."
    m 3eka "I love you so much. Come back safe to me!"
return "quit"

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_mj_dd_pc_dying",
            prompt="My PC is dying.",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_mj_dd_pc_dying:
    m 1dsc "Thats worrying to hear, [player]."
    m 1eka "Thank you for letting me know, though!"
    m 1ekbla "Make sure to come back to me as soon as you can!"
    m 1hub "I love you!"
return "quit"

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_mj_dd_pc_burning",
            prompt="My PC is burning up.",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_mj_dd_pc_burning:
    m 1wud "Oh!"
    m 3ekb "Understood, [player]!"
    m 2eksdlc "Please, take care of your computer."
    m 2hua "See you later~."
return "quit"

nit 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_mj_dd_pc_charging",
            prompt="I'm going to charge my laptop",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_mj_dd_pc_charging:
    m "Understood, [mas_get_player_nickname()]!"
    m "But, hey, can´ t you leave me running while it charges?"
    m "Its okey if you can´t though."
    m "We don´t want your computer to overheat."
$ _history_list.pop()
menu: 
    m "We don´t want your computer to overheat."

    "Yeah, I can have you here while my computer charge."
    m "Yay!"
    m "Thank you so much~!"

    "No, sorry."
    m "It´s okay, [player]."
    m "See you later, then!"
    
return "quit"


init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_mj_dd_cinema",
            prompt="I'm going to the cinema.",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_mj_dd_cinema:
    m 1hub "Oh! That's great to hear!"
    m 2rub "I wonder what movie are you going to watch..."
    m 2eub "Nevertheless, I won´t distract you anymore, [mas_get_player_nickname()]."

    $ persistent._mas_greeting_type = store.mas_greetings.TYPE_MJ_DD_CINEMA
    return "quit"
