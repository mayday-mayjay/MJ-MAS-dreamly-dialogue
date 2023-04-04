#classic by MKTO
init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mj_song_classic",
            prompt="Classic",
            category=[mas_songs.TYPE_SHORT],
            aff_range=(mas_aff.ENAMORED, None),
            random=True
        ),
        code="SNG"
    )

label mj_song_classic:
    m 1dubfa "{i}~You’re over my head~{/i}"
    m 1dubfb "{i}~Outta my mind~{/i}"
    m 1dubfa "{i}~Thinking I was born in the wrong time~{/i}"
    m 5fubfa "{i}~It’s like a rewind~{/i}"
    m 5rubfb "{i}~Even in world gone plastic!{/i}"
    m 5dubfd "{i}~Baby you’re so classic!{/i}"
    m 2dubfa "..."
    m 6hubfa "Ahaha~"
    m 7fubfb "I bet it’s no brainer, who that’s about~"
    m 7wubfb "You know [player], this song has got me feeling very energetic!"
    m 2subfb "So energectic I just might~"
    call monika_kissing_motion_short
    m 2subfb "Ahaha! I just love you so much!"
return "love"
