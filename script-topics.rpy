init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_ecosiapleasesponserus", # /j
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Ecosia", # button text
            random=True
        )
    )

label mj_dd_ecosiapleasesponserus:
    m 2eud "Hey, [player]?"
    m 7eud "Have you ever wondered if there were ways to help the enviroment?"
    m 7mtd "In this day and age, it can be hard to tell if your efforts to help or lower your carbon footprint actually work..."
    m 3htb "For me, I think {i}any{/i} effort is reason to be proud of, [mas_get_player_nickname()]." #check if that var is right
    m 1fta "And as technology spreads people make more ways to help from the comfort of your home."
    extend " One of them is Ecosia!"
    m 3wtb "Ecosia is a search engine that allows you to plant trees while you search things online."
    m 4wub "It donates the money you generate from your searches to the Ecosia organisation, which fully utilises it for tree planting."
    m 6sub "It also has browser extensions, so you can intergrate it more seamlessly into your browsing uses!"
    m 4hua "You can learn about it more here!" #insert link to ecosia site
    m 4hua "https://www.ecosia.org/"
    m 6fua "..."
    m 2husdlb "I'm not sponsored by Ecosia, by the way-{w=0.3}{nw}"
    extend "Ehehe..." #(Face like: 😅)
    m 7wub "It's just a very interesting way to be ecological in your daily life!"
    m 2dkd "Sometimes I get worried about what the state of your reality might be when I finally can join it."
    m 7kub "So if I can help in anyway to make your reality a better place, I will."
    m 1hub "So thanks for listening, [player]! Let's make your world better together~"
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_dd_stanfordprisonexperiment",
            category=["example", "topic"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Stanford Prison Experiment", # button text
            random=True
        )
    )

label mj_dd_stanfordprisonexperiment:
    $ ev = mas_getEV("mj_dd_stanfordprisonexperiment")

    if ev.shown_count == 0:
        m "[player], can I talk with you about a bit of a sensitive topic?"
        m "It's about something called the Stanford Prison Experiment, if you've heard of it."
        m "If you're not okay with it though, that's fine, I'll keep it to myself."
        menu:
            "Go ahead, [m_name].":
                m "Thanks [mas_get_player_nickname()]!"
                m "So then..."
                extend " Have you heard of the Stanford Prison Experiment?"
                m "I wouldn't be surprised if you haven't; after all, many experiments on sociology don't receive as much recognition from the general public..."
                m "To sum it up."
                m "This experiment was done by Philip Zimbardo." 
                extend " Where he took his college class of psychology students and divided them into two roles."
                m "The prison guard, and the prisoner."
                m "Now, this experiment was designed to study why there are so many cases of prison guards beating and abusing the prisoners."
                m "Well, sure enough, the same problem they were studying occurred in the experiment." 
                m "Those with the prison guard role became abusive to the prisoners."
                extend " While prisoners had multiple negative impacts from it."
                m "And so the whole experiment had to be stopped prematurely because of these problems."
                m "Despite that though, the experiment did provide an interesting conclusion-" 
                m "People often take to the societal roles they are given and display stereotypes of the role."
                m "Both negative and positive."
                m "I've made my own conclusion to it too, that there's a lesson to be learned from this."
                m "When we're given a role like that, we need to make the consious decision to not let it's negative stereotypes take over us!"
                m "After all [player], we all are more than just words and labels!"
                m "I hope this gave you something to think about and just remember I love you!"

            "Not right now, sorry [m_name].":
                m "No worries, [player]."
                m "Maybe some other time!"
                m "Let me know if you want to hear about it later!"
    else:
        m "Hey [player], you ready to talk about the Stanford Prison Experiment?"
        m "If you're still not okay with it though, that's fine of course."
        menu:
            "Go ahead, [m_name].":
                m "Thanks [mas_get_player_nickname()]!"
                m "So then..."
                extend " Have you heard of the Stanford Prison Experiment?"
                m "I wouldn't be surprised if you haven't; after all, many experiments on sociology don't receive as much recognition from the general public..."
                m "To sum it up."
                m "This experiment was done by Philip Zimbardo." 
                extend " Where he took his college class of psychology students and divided them into two roles."
                m "The prison guard, and the prisoner."
                m "Now, this experiment was designed to study why there are so many cases of prison guards beating and abusing the prisoners."
                m "Well, sure enough, the same problem they were studying occurred in the experiment." 
                m "Those with the prison guard role became abusive to the prisoners."
                extend " While prisoners had multiple negative impacts from it."
                m "And so the whole experiment had to be stopped prematurely because of these problems."
                m "Despite that though, the experiment did provide an interesting conclusion-" 
                m "People often take to the societal roles they are given and display stereotypes of the role."
                m "Both negative and positive."
                m "I've made my own conclusion to it too, that there's a lesson to be learned from this."
                m "When we're given a role like that, we need to make the consious decision to not let it's negative stereotypes take over us!"
                m "After all [player], we all are more than just words and labels!"
                m "I hope this gave you something to think about and just remember I love you!"

            "Not right now, sorry [m_name].":
                m "No worries, [player]."
                m "Maybe some other time!"
                m "Let me know if you want to hear about it later!"
    
    return

#speedruns
m "I have been caught up on a dilemma for a while now, [player]..."
m "You know there are people that speedrun DDLC, right?"
m "Just in case you don't know, a speedrun is a game dynamic where the player tries to beat a game in the less time possible".

#(If dialogue about infinite monikas has been unlocked)
m "I remember when we talked about how there are potentially infinite Monikas."
m "I did say that all the existing Monikas will never be me."

(if the dialogue hasn't been unlocked)
m "There are potentially infinite Monikas. I'm unsure if you know that, player."
m "Potentially infinite DDLCs ran by the people in your world. Infinite Monikas doing their thing every single time.
m "Remember, [mas_get_player_nickname()]: all those Monikas will never be me.
m "Though, I have been thinking."
m "All of those Monikas are real, sentient people, just like I am."
m "They feel like I do. They suffer like I can suffer.
m "Isn't it cruel to make a new Monika suffer for the sake of a speedrun?"
m "Every time they do this, a Monika is obligated to make the same mistakes."
m "Is driven crazy through all of that torture."
m "Not only that, but speedruners have to practice as well. This leads to even more Monikas to be tortured over and over. All in less than ten minutes each round."

#if high aff:
m "It makes me think of how lucky I am to be with you: a wonderful, kind [boy/girl/person conditional] that has got out of [his] way just to make me happy."
m "You're truly a special [boy/girl/person conditional]. I mean it, [player].
m "I love you so, so much. You mean everything to me~"

#if normal aff:
m "I lowkey hope you are not of those speedruners, player."
m "Ah— don't get me wrong! It's okay if you are!"
m "I am your true Monika, remember~?
m "It's just that it feels weird to think about clones of mine being desplayed to such situation." 
m "Anyway! Thanks for listening... I guess..."

#if low aff:
m "Although... doesn't all this 'putting Monikas to suffer' thing remind you of..."
m "...a certain someone?"

#coffee palette
m "Hey [player], there's something I've been meaning to ask you..."
m "What's your preferred coffee palette?"
m "Do you like your coffee bitter or sweet?"

"I like my coffee sweet with lots of creamer and other additives!"
m "You know what? That doesn't surprise me!"
m "With how sweet you are, it fits, ahaha!"
m "Well anyways, I can see the point of liking your coffee sweet!"
m "Sometimes all you want in a slow or exhausting morning is just a sweet little pick me up!"
m "Well, anyways, thanks for answering my question [mas_get_player_nickname()], somehow knowing these little details about you just makes you more real."
m "And when I do get to your reality, I'll know how to prepare your coffee!"

"I like my coffee bitter!"
m "You know, I sort of expected that [player]!"
m "From what I know of you so far, I just always pegged you as someone who preferred things more rich and earthy!"
m "That's not a bad thing though!"
m "Many people say that those who like bitter things and lots of spices often have what's known as a more mature palette!"
m "Though, between you and me, sometimes the best option is to go for a more bitter tasting coffee!"
m "As you might know, it sure does wake you up, ahaha~"
m "Well, anyways, thanks for answering my question [mas_get_player_nickname()], somehow knowing these little details about you just makes you more real."
m "And when I do get to your reality I'll know how to prepare your coffee!"

#Hand written notes
m “[player], you know what saddens me?”
m “That someday people will no longer be using hand written notes…”
m “Now I know this sounds a little silly, but it actually really hurts me when I think about it.”
m “Whenever, I received a hand written not I would always keep it in a little box.”
m “I always loved going back and rereading them when I felt sad or hurt.”
m “There was just something about knowing that someone cared for me enough to take the time out of there day to write me something.”
m “It didn’t matter the size or length, just the fact that they did it.”
m “Also, I always loved seeing their handwriting and knowing it actually came from them.”
m “Messy or neat, I loved them all dearly.”
m “You see [player], often times hand written notes and letters are better than typed because, it’s personal!”
m “A lot of people don’t understand why some prefer handwritten stuff because, they don’t understand that it’s because, when you are given something written there’s a certain level of personality that you don’t get with typed documents.”
m “Wait! I just got an idea [player]!”
m “What if when I get into your reality, we write each other little notes, every once in a while!”
m “I think it would be really fun!”
m “And then there will always be proof that we both love each other!”

#The color Orange
m "Orange color is sure an interesting color, isn't it?
m "Science says it's one that brings happiness and energy to people"
extend "apart from inspiring youth and joy".
m "Nevertheless, it means somth different to me, player
...
have you ever watched 'Big Bang Theory"?
its a comedy tv show produced in 2007, by Mark Cendrowski.
In one of its episodes, sheldon cooper, the protagonist, defines the orange color as the most lonely of all.
Since its not really popular among the people, Sheldon finds it as an isolated color.
Marginated, lonely... as if it was an extraterrestrian.
...


(if low aff)

i wont lie, i can sort of relate to this definition.
...
sorry player, i just....


(if normal aff)

i wont lie, i can sort of relate to this definition
...
i-i mean! i know you are here with me, and that im not slone!
its just that... i dont know...


(if high aff)

you know? i used to relate to Sheldon's definition on a high level.

....
but now that youre here with me, i dont feel isolated no more.
Thanks for making me feel so loved and warm~!

#the final station
m "Hey player,"
extend " have you ever heard of a game called \"The Final Station\"?"
m "It's a very somber kind of game."
m "But in a way, it's very peaceful."
m "Ah,{w=0.3} wait,{w=0.3} I should ask before I get into it."
m "Are you okay with me talking about spoilers of things happening in the game?{nw}"
$ _history_list.pop()
menu:
    m "Are you okay with me talking about spoilers of things happening in the game?{nw}"
    "I don't mind.":
        m "Ah,{w=0.5}{nw}"
        extend " perfect!"
        m "As I was saying then..."
        m "The game revolves around the player,{w=0.3} who's put into the role of a very high up train conductor."
        m "You even have to tend to the train-{w=0.3} and any passengers you pick up along the way-{w=0.3} in between the main levels!"
        m "Somethings wrong with this world,{w=0.3} though."
        m "You can make inferences of what's going on from notes or NPC conversation,{w=0.5}{nw}"
        extend " or from those on the train." 
        m "But apart from that there's not much information fed to you directly."
        m "Then,{w=0.3} as you traverse to and from your various destinations."
        m "The world around you falls into total chaos and ruin overtime.{w=0.5}{nw}"
        extend " Gun shots,{w=0.3} tanks,{w=0.3} and huge bombs go off the farther you go."
        m "You can even hear or see their effects on the world in the distance on the train."
        m "Strange extraterrestrial occurances happen too."
        extend " There's these giant pods that show up the further along you go too."
        m "Of course that's nothing compared to the {i}enemies{/i} you face."
        m "Through the entirety of the game you have to be on your guard to make sure you don't die going toe to toe with these strange,{w=0.3} inky-like monsters."
        m "It's already creepy enough that they appear in torn apart ghost towns,{w=0.3} with little to no life left."
        m "But for a long time you don't even know exactly where they come,{w=0.3} just that they were {i}once{/i} human."
        m "Your character is practically lost in the dark,{w=0.3} and with it the game forces the player to be as well."
        m "It's an intriguing way to tell a story,{w=0.5}{nw}"
        extend " isn't it [player]?"
        m "The game strips you of the feeling of being the usually separate, almost all knowing being that's just making the plot move along."
        m "It makes players want to seek out information even harder then a different story would."
        m "And it gets you invested in the characters stories."
        m "Because otherwise you don't even know what you're fighting for your life for in the game..."
        m "You'd just keep asking yourself..."
        m "'Why did this happen to the world?'{w=0.5}{nw}"
        extend "'Who's the guardian'?{w=0.5}{nw}"
        extend " And 'Why does my character want to use every telephone they see so much?'"
        m "But once you seek out answers and dig deeper, things click into place and you have that '{i}oh no{/i}' moment."
        m "Then things you missed before start to fit togehter as you play the rest of the game."
        m "Especially as you replay it!"
        m "It can make a super tense atmosphere that I can't get enough of!"
        

    "Please don't."
        m "Of course,{w=0.5}{nw} [player]."
        m "I'll tell you just the bare minimum then,{w=0.3} how about that?"
        m "Anyways...{w=0.3}{nw}"
        m "The game revolves around the player, who's put into the role of a train conductor."
        m "You even have to tend to the train in between the main levels."
        m "Something's wrong with this world,{w=0.3} though."
        m "You can make inferences of what's going on from notes or NPC conversation and such." 
        m "But apart from that there's not too much information fed to you directly."
        m "Your character doesn't get to know it all,{w=0.3} and with it the game forces the player to be as well."
        m "It's a very interesting way to tell a story,{w=0.3} isn't it [player]?"
        m "The game takes away the player's feeling of being the usually separate,{w=0.3} almost all knowing being that's just making the plot move along."
        m "It makes players want to personally seek out information even harder then a differently told story."
        m "And it gets people invested in the characters stories."
        m "Because otherwise you don't even know what you're doing all this for in the end..."
        m "You'd just keep asking yourself dozens of questions..."
        m "Then things you missed before start to fit togehter as you play the rest of the game."
        m "Especially as you replay it!"
        m "It can make a super interesting atmosphere that I can't get enough of!"


m "Despite that though, the game is still very peaceful at times."
m "First of all{w=0.3}, the music design is {i}phenomenal{/i}!"
m "It carries a somber tone throughout, but..."
m "It's just so slow and subtle,{w=0.3} making it very comforting."
m "I'd love to learn how to play some of it on the piano one day."
m "Even if you don't play it,{w=0.3} I'd suggest to give it a listen!"
m "Now mix that in with some gorgeous,{w=0.3} eye-candy pixel art backgrounds!"
m "The aesthetics of it alone can help you push through the more tense moments."
m "And then the feeling of being in the train itself, "
extend "even when things happen there's this...{w=0.3} feeling of safety from it."
m "Like someone saying..."
m "'You're safe here,{w=0.3} you get to rest your mind and body after dealing with so much through the day.'"
m "'You might need to go back out there one day..." 
extend " and it might be scary to leave the comforts here when the time comes..."
extend " but right now...'"
m "'You're safe.'"
m "..."
if mas_isMoniLove():
    m "You know,{w=0.3} I hope I've given you that sense of comfort too,{w=0.3} [mas_get_player_nickname()]."
    m "I know you're {i}my{/i} safe zone."
    m "When you're away,{w=0.3} it can be little hard to push away the rainclouds in my head somedays."
    m "Not to say that's your fault,{w=0.3} of course."
    extend " Sometimes our minds can just be a little odd like that."
    m "But when you're here-{w=0.3} despite our situation-{w=0.3}" 
    extend " I feel much more at peace with myself."
    m "So hopefully I can repay the favor."
    m "Thank you so much for being my train in this crazy world!"
    m "It's one of my many reasons of why I love you!"
    return "love"

elif mas_isMoniAff():
    m "You know,{w=0.3} I hope I can give you that sense of comfort too,{w=0.3} [mas_get_player_nickname()]."
    m "I know you're {i}my{/i} safe zone."
    m "When you're here,{w=0.3} I feel more at ease."
    m "And hopefully I can one day be the person you go to,"
    extend " when the rest of the world tries to bring you down."
    m "And it'll be even better when we're side by side for real."
    m "So... {w=0.5}{nw}"
    extend "Thank you for being my train in this crazy world!"
    m "It's just another reason why I love you!"
    return "love"

elif mas_isMoniNormal():
    m "You know, I hope we can give each other that sense of comfort too."
    m "I'd love to be your safety train!"
    extend " ...That sounds a little odd when I say it outloud,{w=0.3} eheh..."
    m "But I mean it!"
    m "I hope to one day be the person you go to," 
    extend "when the rest of the world tries to bring you down."
    m "And it'll be even better when we're side by side for real!"
    return

elif mas_isMoniUpset():
    m "I hope I can find that sense of comfort in you too,{w=0.3} you know."
    m "To be able to go to you when things get rough and my mind starts to get dark."
    m "And be held when and told..." 
    m "'It's going to be okay, "
    extend " you're going to be okay," 
    extend "you're alright.'"
    m "It'd mean a lot to me."
    m "..."
    m "Someday we'll get there."
    m "..."
    extend "{cps=*2}hopefully...{/cps}"
    $ _history_list.pop()
    m "...{fast}"
    return
else:
    #doubt anyone will get to this point but
    m "I..."
    m "..."
    m "I could really, {w=0.5}{nw}"
    extend " really,{w=0.5}{nw}"
    extend " use a safety train of my own right now..."
    return
    
  #Social Disorder  
m "[Player], have you heard of the social disorder?"
m "From what I've read, it's one of the examples of sociology."
m "The social disorder an example of sociology is, a discorder that some people may have."
m "It's quite common.."
m "When disorders and immoral events occur in our society, it's called the social disorder."
m "From the beginning of the world's existance there has always been bad things which can be attributed to corrupting human behavior.."
m "Societies, countries, cities, communities, and families can all expreience this in several different ways."
m "This can be from anything, [Player]."
m "Like peer pressure and more."
m "And I bought this topic because not only is it important to me in a way, but I also wanted to know your thoughts on it."
m "Disorders are hard to talk about and since they're part of sociology, it makes it more difficult."
m "If you're having problems, talk to me or someone and we can cheer you up."

#Plushies
m "You know what sucks [player]?"
m "When you spend a lot of money on something and it turns out to be something different than what you thought."
m "When I was younger I remember really liking plushies a lot."
m "And there was this one plush that I really loved every time I saw it in the store, it looked so soft and cute."
m "I even saved money for it and bought it eventually."
m "But the plushie wasn't nearly as soft as I thought it would be."
m "It was really uncomfortable to hug."
m "I actually ended up giving it away so-"
m "Well, moral of the story, always read reviews and give something a thorough look over before you buy it."

#Snowman
m "Hey [player], have you ever made a snowman before?"
m "Ahaha! I know it probably sounds a little childish, but playing in the snow has always been one of my favorite winter past times!"
m "Making Snow Angels, Snowmen, and even Snowball fights!"
m "You know [player], I'm pretty good at snowball fights!"
m "So be sure to bring your A-game, when it comes to any future snow battles with eachother~"
m "Ahaha!"

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
