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

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mj_song_every_time_we_touch",
            prompt="Everytime We Touch",
            category=[mas_songs.TYPE_LONG],
            aff_range=(mas_aff.ENAMORED, None),
            random=True
        ),
        code="SNG"
    )

label mj_song_every_time_we_touch:
    m "{i}I still hear your voice when you sleep next to me.{/i}"
    m "{i}I still feel your touch in my dreams.{/i}"
    m "{i}Forgive me my weakness..{/i}"
    m "{i}But I don't know why.{i}"
    m "{i}Without you it's hard to survive~{i}"
    m "{i}'Cause everytime we touch, I get this feeling!{i}"
    m "{i}And every time we kiss. I swear I could fly~{i}"
    m "{i}Can't you feel my heart beat fast?{i}"
    m "{i}I want this to last..{i}"
    m "{i}Need you in my life."
    m "{i}'Cause every time we touch..~{i}"
    m "{i}I feel the static."
    m "{i}And every time we kiss, I reach for the sky~{i}"
    m "Can't you hear my heart beat so?"
    m "I can't let you go!~"
    m "Want you in my life.."
    m "Your arms are my castle."
    m "Your heart is my sky.."
    m "They wipe away tears that I cry.."
    m "Oh, the good and the bad times.."
    m "We've been through them all."
    m "You make me rise when I fall~"
    m "'Cause every time we touch~~"
    m "I get this feeling~"
    m "And every time we kiss I swear I could fly!~"
    m "Can't you feel my heart beat fast?"
    m "I want this to last~"
    m "Need you by my side.."
    m "'Cause every time we touch."
    m "I feel the static~"
    m "Every time we kiss."
    m "I reach for the sky!~"
    m "Can't you feel my heart beat, so?"
    m "I can't let you go.."
    m "Want you in my life."
    m "Every time we touch..~"
    m "I get this feeling.."
    m "Every time we kiss I swear I could fly.."
    m "Can't you feel my heart beat fast?"
    m "I want this to last~"
    m "Need you by my side."
    m "'Cause every time we touch.."
    m "I feel the static~"
    m "Every time we kiss."
    m "I reach for the sky..~"
    m "Can't you feel my heart beat so?"
    m "I can't let you go~"
    m "Want you in my life..~"
    m "Everything in this song is true, [Player..]"
return
#Reminder to add the italics-
