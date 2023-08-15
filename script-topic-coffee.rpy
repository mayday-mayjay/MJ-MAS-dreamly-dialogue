
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







#Snowman
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_snowman",
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Snowman", # button text
            random=True
        )
    )

label mj_dd_snowman:
    m "Hey [player], have you ever made a snowman before?"
    m "Ahaha! I know it probably sounds a little childish, but playing in the snow has always been one of my favorite winter past times!"
    m "Making Snow Angels, Snowmen, and even Snowball fights!"
    m "You know [player], I'm pretty good at snowball fights!"
    m "So be sure to bring your A-game, when it comes to any future snow battles with eachother~"
    m "Ahaha!"
return

#Dress Up
>Do you mind it when I dress you up in different styles?

if even lower then reg low aff?? idek:
m "..."
m "Does it matter...?"
m "You'd do it anyways."
m "I can't stop you..."

return

#if low aff(?):

m  "Hm, a little, I suppose."
m "It feels like another reminder that you don't see me as a real being.{fast}{nw}"
m "It feels like another reminder that{fast} I'm trapped here."
m "There's not much I can do about it here though."
m "Just... Try not to turn me into your punchline with weird clothes.{cp=0.2}{nw}"
m "Just... Try not to{fast} put me in anything odd or offensive, will you?"
m "That's all I ask."

return

#if norm aff:

m "Not really, no!"
m "It's all in good fun, right?"
m "You or some other artists gets to have fun designing interesting styles for me,"
extend " and then I get to model it!"
m "In a way I feel like a model, or an actress getting ready for set!"
m "Sure, not everything is something I could imagine picking out myself."
m "And if something is part of a cosplay... 
extend " There's a good chance I won't get the reference, eheh..."
m "In the end you and I are having fun, and that's what matters most to me!"
m "Of course, try to keep the outfits within reason."
m "Nothing...{nw}"
extned " overly sexual, okay?"
m "We're not at that level for me to be dressing like {i}that{/i} you know?"

#if player hasnt gotten themselves locked out of nicknames like a dummy:
m "I trust you wouldn't, you've been attentive to my feelings so far."
m "It's why I love you~!"
m "But it never hurts to make sure a boundary is firmly in place!"

#go to this right after the if part
m "If I feel really bad about a style you try to give me, I'll let you know, okay [player]?"

return

#if high aff
"Of course not!" 
"It's a blast to try out different outfits and styles you give me!"
m "Sure, not everything is something I could imagine picking out {i}myself{/i}."
m "And if something is part of a cosplay... 
extend " There's a good chance I won't get the reference, eheh..."
m "But I find that it's a great way to pull me out of my comfort zone!"
m "There's tons of things that I might not have tried for myself before, but I end up loving the way it looks!"

if 18+(i forget the specific variable for this check?) 
m "And I also love trying to piece together what's your particular {i}'taste'{/i} as you gift me... interesting styles..."
m "Ehehe~" #wink!

m "In a way I feel like it'll be one the very few things I miss when I go to your reality..."
m "We'll have to actually {i}purchase{/i} any new clothes, rather then get them from artists. {nw}"
extend " The quality probably won't be as consistent and nice.{nw}"
extend " Handmade things would be harder to get to me too."
m "And I certainly wouldn't be able to try them on at the click of a button..."
m "But... The trade off of spending my life physically by your side would be worth it though~"
m "Keep in mind however..."
extend " When I {i}do{/i} get to your reality, you won't be able to make me try as much on."

#if 18+:
m "Minus a few... {i}exceptions~{/i}

m "But I'd like to have a more autonomy then I do {i}here{/i}."
m "I'll still take suggestions though! 
m "Because I think you've got great taste [player nickname]~"
m "Just another reason why I love you~"

return

## moni asking player what kind of pet would they want/if at all

m "Hey, [player], do you have any pets?"
m "I wonder what kind of animals you'd take care of. I bet you'd be great at it!~"
m "So.. do you have any pets?"
## YES/NO
## YES, DOG(S)
m "Oh, really?"
m "That makes sense, actually!"
m "You do kind of seem like a puppy, always coming to check on me, ahaha!~"
m "Do you have just one, or multiple?"
m "I know that dogs are pretty social creatures, so they probably work best with a friend or two."

m "Did you know that some dog breeds have such good sense of smell that they can sniff out medical problems?"

m "They're called <i>bio-detection dogs</i>, and they can smell cancer! In fact, in 2006, scientists trained dogs to detect cancer from peoples breath."

m "Other examples include dogs that can smell a general sense of someone's bloodsugar, for example, a type one diabetic could have a severely low bloodsugar without realizing it, or be unable to ask for help, and their dog could alert someone for help, or alert their owner that they need to go get something to raise their bloodsugar!"

m "Isn't that amazing? Dogs can do so many amazing things!"

m "Not to mention the many wonderful dogs that are more mainstream and popular nowadays, like seeing eye dogs for blind people, or the wonderfully friendly yet loyal and helpful therapy dogs!"

m "Oh, I almost forgot to mention dogs that help search and rescue teams find people lost in rubble after disasters like tornadoes, avalanches, and other things."

m "Oh, sorry, I got distracted, ahaha.."

m "When I cross over, I hope I could meet them! Hopefully they like me, hehe.."

return

## YES, CAT(S)

m "Oh, really?"

m "You know, that makes sense."

m "You do kind of remind me of a playful kitten, sometimes. You bring me gifts all the time, just like a cat after exploring outside, ahaha!"

m "Although, from what I've heard, cats gifts are usually not so nice.."

m "Is it true that their back goes up a little bit if you scratch them near their tail just right?"

m "Ahaha, sorry! That was random, I've just heard that it's a common thing with happy kitties."

m "As far as I know, cats are usually fine on their own, but I'm sure they wouldn't mind a friend or two."

m "Do you have multiple cats, [player]?"

m "Either way, I'm sure your little friend loves you a lot!"

m "I know I do!~"

m "I wonder if they'll like me, when I cross over?"

m "It would be nice to pet a fluffy cat. I heard their fur is <i>super</i> soft if you've got the right breed."

return

## YES, REPTILE(S)

m "Ooh, a reptile, like a lizard or a snake?"

m "You know, that makes sense, now that I think about it."

m "You kind of remind me of a nice little lizard enjoying the sunshine, closing its eyes and being still as its owner gives it a nice pet or two, ahaha!"

m "Ah, sorry, that was probably weirdly specific.."

m "Anyway, what's your reptile like?"

m "I hear that reptiles, at least the more common ones like snakes and reptiles, enjoy more alone time, right?"

m "I don't think they'd mind a little playdate every now and then with a friend if it's the right reptile, though."

m "Oh, I'm getting sidetracked."

m "What's your reptile like? Do you have multiple, or just the one?"

m "It'd be really cool to pet a lizard, or a snake when I cross over!"

m "Ahaha, hopefully they like me.. that would be pretty awkward if they didn't."

return

## YES, AQUATIC ANIMAL(S)

m "Oh, really?"

m "You know, now that I think about it, you do kind of remind me of a turtle. Cold and quiet but warm and loving, ahaha!~"

m "I hear aquatic animals usually need friends so they aren't lonely, right?"

m "I wonder what your water-loving friends are like?"

m "Ooh, feeding fishes with you would be nice when I cross over."

m "And if it's not a fish, I'm sure they'd still be really fun to hang around with!"

m "Hopefully they like me, haha.."

return

## YES, RODENT(S)

m "Wow, really?"

m "Rodents are actually really cute once you get to know them!"

m "I wish more people weren't so assuming of rats and mice and such. They're actually very clean and kind!"

m "Do you have rats.. or maybe mice?"

m "Oh! Maybe you have a hamster or a gerbil instead?"

m "Maybe something like a chinchilla or a guinea pig?"

m "Ahh, all of those sound adorable and nice to hang out with!"

m "I hear rodents are social and always in need of a friend or two, right?"

m "I hope your little friends are nice to each other!"

m "It would be really fun to make a little obstacle course for those smart little cuties one day when I cross over."

return

## YES, FARM ANIMAL(S)

m "Ooh, really?"

m "Do you perhaps live on a farm, [player]?"

m "I hear farm animals are fairly social creatures. I wonder if you've got a friend or two for them?"

m "There are so many different kinds of farm animals!"

m "Maybe you've got some cows or pigs?"

m "Ooh, maybe a horse?"

m "Ah! I can't forget about chickens!"

m "I wonder what farm animals you've got?"

m "It would be fun to ride a horse with you one day, [player]."

return

## YES, BIRD(S)

m "Oh, really?"

m "What kind of birds? Maybe a Quetzal?~"

m "Ooh, maybe a parrot or a cockatiel?"

m "Quetzals will forver be my favorite, though! They're so majestic, and their song is nice, too."

m "I could go on forever with Quetzals!"

m "Did you know that the Mayans made a stone pyramid that, when you clapped, the echo would return as a Quetzal's song?"

m "That's just amazing! I didn't know engineering could be so wonderful."

m "Ah, I'm getting all sidetracked! Sorry, ahaha.."

m "I hope we could take care of your bird together one day, [player]."

return

## YES, OTHER(S)

m "Oh, really?"

m "Hm.. I thought I covered a lot of animals with everything else I put on those options."

m "Oh well, you can never cover every animal ever, ahaha!~"

m "I'd love to know all about them, [player]!"

m "Do you have multiple, or just one?"

m "It would be nice to take care of them together, whenever I cross over."

m "For now, you can just tell me all about them!~"

return

## NO, AND I DON'T WANT ANY

m "Oh, okay."

m "That makes sense! Not everyone has the time and energy to care for something that's entirely dependent on them."

m "Of course, not wanting one just because, is fine too!"

m "It would be nice to settle down with you after a long day of work, have a nice little dinner and then lay down on the couch, maybe fall asleep after watching a movie."

m "Maybe we could get one together in the future, if you'd like?"

return


## NO, BUT I WANT ONE

m "Oh, really?"

m "Are you looking at options for pets currently, or are you just thinking about it?"

m "Remember to always go to shelters!"

m "The animals there are healthier, and you can give a wonderful pet that wasn't treated fairly a nice home."

m "I wonder if whenever I cross over, you may have one then?"

m "Whatever option you choose, I'll be supporting you all the way!"

return

## NO, I'M NOT ABLE TO TAKE CARE OF ANY

m "Oh.. really?"

m "I'm sorry, [player]. I can stop talking about this, if you want."

m "I can kind of relate to it, though, being in here.."

m "I would love a Quetzal to take care of, but I'd feel bad trapping it in here."

m "Maybe when I cross over, we can take care of it together?"

m "I can do the things you don't have the energy for, like taking them on walks, or cleaning a litterbox, and you can feed them. We could play with them together."

m "That sounds nice."

return

##apology to the player
"You offended me."

m "Oh..."
m "I'm really sorry [player]."
m "I never meant to hurt you in anyway."
m "But thank you for telling me!"
m "I would have never been able to apologize otherwise..."
m "If you're okay with me asking, can I know what I did?"

"You said something that hurt me."
m "Oh...thank you for telling me, [player]."
m "I know I like to tease you but, it's never been my intention to hurt you,"
m "I promise I'll try to be more careful with my words from now on!"
m "I love you and I'd never want ever to hurt you in any way."

"You really scared me."
m "Oh, I'm sorry [nickname tag]."
m "I didn't mean to frighten you."
m "I know I like to play little pranks on you but, I didn't mean to scare you that much."
m "I promise from now on, I'll try to be more careful so as to not scare you."
m "I love you and I'd never want ever to hurt you in any way."

"It was something else."
m "Oh...well whatever I did just know that I'm really sorry."
m "I never intend to ever hurt you in any form."
m "I promise I'll try to be more careful so as to not offend you in any way."
m "I love you so much and it hurts me to see you in any type of pain."


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
