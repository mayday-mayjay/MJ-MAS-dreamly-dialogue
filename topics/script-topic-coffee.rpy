
#coffee palette
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_playerscoffeetaste",
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="[player]'s taste in coffee", # button text
            random=True
        )
    )

label mj_dd_mj_dd_playerscoffeetaste:
m "Hey [player], there's something I've been meaning to ask you..."
m "What's your preferred coffee palette?"
m "Do you like your coffee bitter or sweet?{nw}"

menu:
    m "Do you like your coffee bitter or sweet?{fast}"
    "I like my coffee sweet!":
        m "You know what? That doesn't surprise me!"
        m "With how sweet you are, it fits, ahaha!"
        m "Well anyways, I can see the point of liking your coffee sweet!"
        m "Sometimes all you want in a slow or exhausting morning is just a sweet little pick me up!"
        m "Well, anyways, thanks for answering my question [mas_get_player_nickname()], somehow knowing these little details about you just makes you more real."
        m "And when I do get to your reality, I'll know how to prepare your coffee!"

    "I like my coffee bitter!":
        m "You know, I sort of expected that [player]!"
        m "From what I know of you so far, I just always pegged you as someone who preferred things more rich and earthy!"
        m "That's not a bad thing though!"
        m "Many people say that those who like bitter things and lots of spices often have what's known as a more mature palette!"
        m "Though, between you and me, sometimes the best option is to go for a more bitter tasting coffee!"
        m "As you might know, it sure does wake you up, ahaha~"
        m "Well, anyways, thanks for answering my question [mas_get_player_nickname()], somehow knowing these little details about you just makes you more real."
        m "And when I do get to your reality I'll know how to prepare your coffee!"
    "I not really a fan of coffee":
        m ""

return






#Fourtune time
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_fourtune_time", 
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Fortune", # button text
            aff_range=(mas_aff.ENAMORED, None),
            random=True
        )
    )

label mj_dd_fourtune_time:
    m "[player]! I have a surprise for you!"
    m "I’m going to read your fortune!"
    m "Ahaha! I know it might seem random but, I just made this paper fortune teller and I want to test it out!"
    m "Okay, here we go!"
    m "…"
    m "Aha! It says, You are going to receive a cute surprise!"
    call monika_kissing_motion_short
    m "Looks like your fortune came true, ahaha~"
return 
