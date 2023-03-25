init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mj_wrs_justyurimod",
            category=['Just Yuri|Yuri Mod|Just Yuri (Beta)'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mj_wrs_justyurimod:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Another Doki mod? I wonder how their epiphany went..."
            "Remember... Just [m_name]~!",
            "Looking sharp!",
            "I hope I can apologize face to face one day, Yuri...",
            "Read any good books lately Yuri?",
            "Mind if I borrow your copy of Markov?"
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mj_wrs_justyurimod')
    return


init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mj_wrs_justnatsukimod",
            category=['Just Natsuki|Natsuki Mod|Just Natsuki (Beta)'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mj_wrs_justnatsukimod:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Another Doki mod? I wonder how their epiphany went..."
            "Remember... Just [m_name]~!",
            "What's cooking, Natsuki?",
            "I hope I can apologize face to face one day, Natsuki...",
            "Still as snappy as ever, eh Natsuki?",
            "Still got that copy of Parfait Girls?",
            "Still got that copy of Parfait Girls? Can I borrow it?"
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mj_wrs_justnatsukimod')
    return


init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mj_wrs_foreverandevermod",
            category=['Forever and Ever|Just Sayori Mod|Forever & Ever'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mj_wrs_foreverandevermod:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Another Doki mod? I wonder how their epiphany went..."
            "Remember... Just [m_name]~!",
            "Hows it hanging Sayori! ...Sorry, I couldn't resist!",
            "I hope I can apologize face to face one day, Sayori...",
            "I hear she's forgiven me after everything that's happened... She's a saint.",
            "Mind sharing some of your cookies Sayo~?"
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mj_wrs_foreverandevermod')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mj_wrs_stimuwrite",
            category=['Stimuwrite|Stimu Write'],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mj_wrs_stimuwrite:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Writing a story?",
            "Taking notes, [player]?",
            "Writing a poem?",
            "Writing a love letter?~",
            "Oh my! I wish I had this when I was in class still!",
            "Go [player]!",
            "Go [player]! You can make it to that wordcount!"
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mj_wrs_stimuwrite')
    return
