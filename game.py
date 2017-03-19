from inspect import isfunction

# print read me document before starting game -> tells instructions and guidelines
# update software specs

print "What is your name?"
name = raw_input("> ")

## vocabulary
dining_list = ["dining", "dining room", "Dining", "Dining Room", "Dining room"]
living_list = ["living", "living room", "Living", "Living Room", "Living room"]
kitchen_list = ["Kitchen", "kitchen"]
library_list = ["Library", "library", "Lib", "lib"]
bathroom_list = ["Bathroom", "bathroom", "bath", "Bath"]
foyer_list = ["Foyer", "foyer"]
stairs_list = ["stairs", "steps", "Stairs", "Steps"]
basement_list = ["Basement", "basement", "Cellar", "cellar"]
hallway_list = ["Hallway", "hallway", "hall", "Hall", "corridor", "Corridor"]
lroom_list = ["left room", "Left room", "Left Room", "left", "Left"]
lgroom_list = ["large room", "Large room", "Large Room", "large", "Large"]
rroom_list = ["right room", "Right room", "Right Room", "right", "Right"]
comproom_list = ["computer room", "comp room", "Computer Room", "Computer room", "Comp Room", "Comp room", "computer", "comp", "Computer", "Comp"]
attic_list = ["Attic", "attic"]
inventory_list = ["inventory", "Inventory", "items", "Items", "Things", "Stuff", "things", "stuff"]

def library():
    if basement == True:
        print "Living Room    Bathroom    Foyer    Basement"
    else:
        print "Living Room    Bathroom    Foyer"

## dialogue dictionaries
doors_dict = {'foyer': "Dining Room    Living Room    Library    Stairs",
    'living': "Dining Room    Kitchen    Library    Bathroom    Foyer",
    'dining': "Kitchen    Living Room    Foyer",
    'kitchen': "Dining Room    Living Room",
    'bath1': "Living Room    Library",
    'library': library,
    'hallway': "Stairs    Large Room    Left Room    Right Room    Computer Room",
    'b_room': "Hallway    Bathroom",
    'p_room': "Hallway    Bathroom",
    'bathp': "Large Room",
    'bathj': "Left Room    Right Room",
    'k_room': "Hallway    Bathroom    Computer Room",
    'c_room': "Hallway    Right Room    Attic",
    }

items_dict = {'living': "couch    armchair    fireplace",
    'dining': "table    paintings",
    'kitchen': "fridge    sink    drawers    cabinet",
    'bath1': "mirror    toilet    bathtub",
    'library': "armchair    shelves    desk",
    'b_room': "dresser   pictures    bed    frame",
    'p_room': "beds    vanity    closet",
    'bathp': "mirror    toilet    bathtub",
    'bathj': "mirror    toilet    bathtub",
    'k_room': "dresser    bed    books",
    'c_room': "desktop    wires    television",
    }

## variables
# items
hammerv = False
crowbarv = False
screwdriverv = False
knifev = False
small_key = False # something is wrong with this - doesn't work at bathtub2
codev = False
a_key = False

# conditionals
bath1v = False
bathpv = False
bathjv = False
ticks = False
basementv = False
null = False
k = False
framev = False

# counters
drawersv = 0
friendship = 0
pieces = 0

## inventory
inventory = {'pb&j sandwich': "Vinh packed this because he thought we'd get hungry. It is squished beyond recognition, now.",
    'flashlight': "We'll probably need this."
    }

## inventory functions
# living room
def fireplace():
    print """Cold and dark, it still has years old ashes covering the bottom.
It appears we can look inside of it to the other floors. A spider
stares from the corner."""
    print "Look inside? \n\t1: Yes. \n\t2: No."
    c = raw_input("> ")
    if c == "1":
        print "I crawled into the fireplace to look up. The last thing I saw \nwas plummeting brick and a shower of ash.\n"
        print "-----CONGRATULATIONS! YOU DIED!-----"
        exit(1)
    elif c == "2":
        return 'dining'
    else:
        print "Please enter either 1 or 2."
        return 'dining'

def armchair():
    global ticks
    print "Although covered in dust, it looks comfortable to sit in."
    if ticks == True:
        print "That is, before we discovered the colony of ticks in it."
        print "Two ticks remain crawling about the cushion."
    print "\n\t1: Sit in it. \n\t2: Poke the cushion."
    c = raw_input("> ")
    print "\n"
    if c == "1":
        print """The cushion is quite comfortable, but a little bumpy. It appears
to be moving. Suddenly, the chair collapses and I am consumed by
a mass of twitching bugs."""
        print "\n"
        print "-----CONGRATULATIONS! YOU DIED!-----"
        exit(1)
    elif c == "2":
        if ticks == True:
            print "Do we really want more ticks to come out of it?"
            return 'living'
        else:
            ticks = True
            print """Alex taps the cushion lightly, causing two ticks to crawl through
a previous unnoticed hole. \"Ah! What are those doing there?\""""
            print "\n"
            return 'living'
    else:
        print "Please enter either 1 or 2."
        return 'living'

# dining room
def paintings():
    print "\nThe paintings on either side of the center portrait seem \nto have been done professionally. The first depicts a couple,"
    print "possibly the previous owners of the house. The last portrait \nis of a young boy with a large grin. The middle frame is empty"
    print "and whatever used to be there was replaced by a cartoon \nstrip. A girl waves from the first panel, saying, \"Let\'s have"
    print "a scavenger hunt!\" The next three panels had a chair, a \nbook, and the word 'arachnids'.\n"

# kitchen
def drawers():
    global friendship
    global knifev
    global drawersv
    drawersv += 1
    if drawersv < 2:
        print "Vinh pulls the drawer open slightly. \"Eh, nothing here.\""
    elif knifev == True:
        print "The drawer does not contain anything else."
    else:
        print "I\'m not sure if Vinh really checked the drawer thoroughly."
        print "Should I look at it again?"
        print "\t1: Trust his judgment. \n\t2: Check the drawer."
        c = raw_input("> ")
        print "\n"
        if c == "1":
            friendship =+ 1
            return 'kitchen'
        elif c == "2":
            knifev = True
            inventory.update({'knife': "Found in the kitchen drawer. Rusted only slightly and surprisingly sharp."})
            print "I opened the drawer fully and find a knife at the back."
            return 'kitchen'
        else:
            print "Please enter either 1 or 2."
            return 'kitchen'

def cabinet():
    global crowbarv
    global hammerv
    global screwdriverv
    global friendship
    print "\nInside the cabinet, there was a bulky toolbox with a \ncombination lock. It has three dials."
    print "Enter the code."
    c = raw_input("> ")
    print "\n"
    if c == "777":
        crowbarv = True
        hammerv = True
        screwdriverv = True
        inventory.update({'hammer': "Found in a toolbox in the kitchen. Very heavy, definitely lethal."})
        inventory.update({'screwdriver': "Found in a toolbox in the kitchen. Standard Phillips head, long handle and stem."})
        inventory.update({'crowbar': "Found in a toolbox in the kitchen. Not very large, kind of rusted."})
        print "\nThe lock clicks and the lid opens on its own. Inside the toolbox\n are a large hammer, a crowbar, and a screwdriver."
        print "\n\t1: Ask your friends to take one each. \n\t2: Carry them yourself."
        ch = raw_input("> ")
        print "\n"
        if ch == "1":
            friendship =+ 1
            print "\"I\'ll take this hammer,\" Vinh says as he struggles to lift it."
            print "\"Er, I\'ll  have the screwdriver, then...\" Alex picked it out."
            print "That just left the crowbar to me. I wonder what we can use these for."
            return 'kitchen'
        elif ch == "2":
            print "I closed the toolbox and tried to lift it. Gosh, it was heavy. I \nskipped arm day too often to be able to carry this."
            print "\"Dude, let me help you. You\'re struggling big time.\" Vinh and Alex \nended up having to take a tool each so we could transport them."
        else:
            print "Please enter either 1 or 2."
            return 'kitchen'
    else:
        print "Apparently, that wasn\'t right. The toolbox stays shut."
        return 'kitchen'

# bathroom 1
def bathtub():
    global crowbarv
    print "\nThe bathtub might have been white originally but is brown \nfrom years of dirt. The only shining part is the drain, which \nis loose."
    print "\nLook in the drain?"
    print "\t1: Yes.\n\t2: No."
    c = raw_input("> ")
    print "\n"
    if c == "1":
        if crowbarv == True:
            small_key = True
            inventory.update({'small key': "Found hanging in the drain of the bathtub on the first floor."})
            print "We used the crowbar we got from the toolbox and pried open \nthe drain. A tiny key on a chain had been dangling in the drain. It was wet."
            print "\"Isn\'t it weird that it\'s wet? I thought this house is \nabandoned,\" Alex mused."
            return 'bath1'
        else:
            print "Vinh tried to pull the drain with his bare hands, but it \nappeared we would need a tool."
            return 'bath1'
    elif c == "2":
        return 'bath1'
    else:
        print "Please enter either 1 or 2."
        return 'bath1'

# library
def lib_shelves():
    print "\nThere are three shelves. The spaces between are pretty wide. \nThere are some fallen books."
    print "\n\t1: Look at the first shelf. \n\t2: Look at the second shelf. \n\t3: Look at the third shelf. \n\t4: Look at the books in the spaces."
    c = raw_input("> ")
    print "\n"
    if c == "1":
        print "This shelf appears to contain mostly factual references, especially \nscience texts. Three of them have golden spines."
        print "Read a book?"
        print "\n\t1: Yes. \n\t2: No."
        c = raw_input("> ")
        print "\n"
        if c == "1":
            print """Jose Manuel Rodriguez Delgado is known for his work with neural
pacemakers. With these, he could control the actions of animals
by electrical brain stimulation. In one experiment, he inplanted
a stimoceiver, one type of pacemaker, into a bull's head. Inside
a bullring, acting as a matador, he was able to stop the bull in
its tracks right before it ran into him by pressing a button on
a remote."""
            print "\nPress enter to continue.\n"
            raw_input("> ")
            print """He went on to apply these studies to treat certain diseases in
humans. Stimulation via electrodes to the brain changed the mood
and behavior of several patients, even acting out of character.
However, this practice did not have an immediate medical purpose,
so the "button activated joy-box" lost its popularity."""
            print "\nPress enter to continue.\n"
            raw_input("> ")
            print """Still, he persisted. After conducting experiments with a community
of gibbons, he proposed that the remote could help control society.
For example, if an implant in a person's brain can detect changes in
brainwaves that reflect psychotic activity, the authorities can be
informed of this and send back waves to stabilize the person. He
published his theories in "Physical Control of the Mind: Toward a
Psychocivilized Society." He suggested that neurotechnology can
produce "a less cruel, happier, and better man."""
            print "\nI can't imagine that text would have been very popular."
            return 'library'
        elif c == "2":
            return 'library'
        else:
            print "Please enter either 1 or 2."
            return 'library'
        return 'library'
    elif c == "2":
        print "This shelf appears to contain fiction books, including several \nclassics. Two of them have golden spines."
        print "Read a book?"
        print "\n\t1: Yes. \n\t2: No."
        c = raw_input("> ")
        print "\n"
        if c == "1":
            print """There was a young girl named Chiaki. She was playing in her
bedroom when she heard her mother calling her from the kitchen.
She raced downstairs.

"Chiaki, come here. I have something to ask you," her mother said.

"What is it?" asked Chiaki.

"Do you know who ate the cakes that were meant for the guests?"

"Uh... No... I don't know," Chiaki replied.

"Did you eat the cakes?" her mother asked.

"No, Mama, I didn't," the little girl replied.

Chiaki was wringing her hands nervously."""
            print "\nPress enter to continue."
            raw_input("> ")
            print "\n"
            print """"Chiaki, I know when you are lying," her mother said. "A thief always
starts out in life by lying. And the police always catch a thief. And the
thief is always punished. Do you know what I am saying Chiaki?"

Chiaki couldn't bear the guilt anymore. She started sobbing.

"Mama, I'm sorry!" she wailed. "I ate the cakes! I'm sorry!"

"There, there. Stop crying," said her mother as she held her hand. "I
was angry because you lied to me. Now you've told the truth,
everything is going to be fine. I don't like liars, so never lie to me
again, OK?"

"OK," said Chiaki.

"Now dry your tears," said her mother. "We'll go to the store and buy
more cakes."

"OK, Mama," Chiaki said."""
            print "\nPress enter to continue."
            raw_input("> ")
            print "\n"
            print """Chiaki's mother had a baby. When she came home from the hospital,
Chiaki was delighted.

"This is Nana," her mother said. "You're her big sister. You have to
treat her with love and care."

"I will, Mama," Chiaki said.

But after the baby arrived, her mother didn't seem to have any time
for her. The baby cried all day and all night. Chiaki couldn't bear to
hear it screaming and bawling. She couldn't concentrate. She
couldn't even think. Eventually, she had enough."""
            print "\nPress enter to continue."
            raw_input("> ")
            print "\n"
            print """"Mama! I'm sick and tired of hearing her cry!" she shouted. "I can't
study with all this racket! Can you please shut her up?"

"You need to be more understanding," her mother said. "Nana is just
a baby. You're her big sister."

"But you're always with Nana," Chiaki cried. "You never have time for
me anymore. I'd like to spend time with you too, Mama. I'd like to go
to the store with you, to the park with you, cuddle with you..."

"You're old enough to go to all those places by yourself," her mother
said. "So shut your mouth and stop being so selfish."

"I hate you!" Chiaki screamed as she burst into tears."""
            print "\nPress enter to continue."
            raw_input("> ")
            print "\n"
            print """She ran upstairs, slammed her door and locked herself in her room.
That evening, she refused to come down for dinner. Instead, she
stayed in her room and brooded about Nana.

That night Chiaki had a very disturbing dream. In the nightmare, she
saw herself walking through the house in darkness. She went into
her mother's room and tip-toed over to the baby's crib. Then, she
picked up her little sister and carried her downstairs.

In the dream, Chiaki opened the back door and brought Nana out to
the garden. There, by the light of the moon, she fetched a shovel
from the shed, dug a little hole in the wet grass and buried her little
sister alive.

When she woke up in the morning, Chiaki was shaking and covered
in sweat. She felt sick to her stomach. The nightmare had seemed so
real. She was horrified."""
            print "\nPress enter to continue."
            raw_input("> ")
            print "\n"
            print """"Mom was right," she thought. "Nana is just a baby. I'm her big sister.
I need to learn to put up with things like this. I'm going to ask Mom
to forgive me."

Just then, her mother burst into her room. Tears were streaming
down her face.

"Chiaki, do you know where Nana is?" she asked. "When I woke up
this morning, she wasn't in her crib. Do you know anything?"
The little girl shook her head.

"Are you sure?" her mother demanded. "You really don't know
anything? Do you swear?"

Chiaki gulped. "Yes, I swear," she said weakly.

"Alright! Alright!" her mother said. "Help me find her!\""""
            print "\nPress enter to continue."
            raw_input("> ")
            print "\n"
            print """They searched the house from top to bottom, but they couldn't find
Nana. They ran up and down the street looking for the baby, but she
was nowhere to be seen. Finally, her mother fell to her knees and
began sobbing uncontrollably.

"Where did Nana go?" she wailed. "Where could she be? She doesn't
even know how to walk. How could she disappear like this?"
Chiaki was wringing her hands nervously.

"Chiaki you know something!" her mother screamed. "Chiaki! You
know what happened to Nana, don't you!\""""
            print "\nPress enter to continue."
            raw_input("> ")
            print "\n"
            print """"No," said Chiaki. "I don't know anything..."

"Chiaki, I warned you not to lie to me again!" her mother screamed.
"I'm not lying," Chiaki mumbled.

"I know when you're lying!" her mother shouted. "Tell me! Where is
she? Where is Nana?"

Chiaki couldn't bear the guilt anymore. She looked out the window
and pointed at a little mound of earth in the garden.

"No!" her mother cried. "Dear God! No! This can't be true!\""""
            print "\nPress enter to continue."
            raw_input("> ")
            print "\n"
            print """"Mama!" the little girl sobbed. She tried to grab her mother's hand.
"Don't touch me!" her mother screamed. "You killed Nana, didn't you!
You killed her because you were jealous!"

"I didn't mean it, Mama!" Chiaki cried. "I didn't mean it!"

Her mother flew into a violent rage. She grabbed her daughter by the
neck and began choking the life out of her. She squeezed and
squeezed until she couldn't squeeze anymore. By the time she came
to her senses, Chiaki lay dead on the kitchen floor.

Suddenly, the doorbell rang."""
            print "\nPress enter to continue."
            raw_input("> ")
            print "\n"
            print """The mother got to her feet and answered it.

When she opened the door, she saw her neighbor standing outside.
He was holding Nana in his arms.

"We found her crawling around outside," he said. "She must have
gotten out of her crib during the night. Good thing we found her
before something bad happened...\""""
            print "\n..."
            print "Well that wasn't disturbing at all."
# http://www.scaryforkids.com/white-lies/
            return 'library'
        elif c == "2":
            return 'library'
        else:
            print "Please enter either 1 or 2."
            return 'library'
        return 'library'
    elif c == "3":
        print "This shelf could be classified as 'Miscellaneous' at a bookstore. \nOne of them has a golden spine."
        print "Read a book?"
        print "\n\t1: Yes. \n\t2: No."
        c = raw_input("> ")
        print "\n"
        if c == "1":
            print "Vinh picks out the golden spined book. It turns out to be a \nhollow book."
            print "\"Well, I never liked reading much anyway.\""
            return 'library'
        elif c == "2":
            return 'library'
        else:
            print "Please enter either 1 or 2."
            return 'library'
        return 'library'
    elif c == "4":
        global name
        print "A recipe book is open to directions for the perfect pancake. \nAttached is a sticky note, reading, \"Pancakes are flat.\""
        print "Under that in a drippy red text, \"AND SO ARE YOU.\""
        print "*SLAM*"
        print "The bookshelves come together with a sticky crimson substance \nin between. It probably used to be %s." % name
        print "\n"
        print "-----CONGRATULATIONS! YOU DIED!-----"
        exit(1)
    else:
        print "Please enter 1, 2, 3, or 4."
        return 'library'

def desk():
    print "A few books lay open and the chair is pulled out slightly, as if \nsomeone just left momentarily and would return. I sneeze from \n clearing the dust from what appears to be an diary."
    print "\n\t1: Look at the diary. \n\t2: Look at the other book."
    c = raw_input("> ")
    print "\n"
    if c == "1":
        print "The book is a standard brown, with golden trimmings on the spine. \nWe read a few pages of the diary."
        print """It has been harder for me to give the kids a good impression.
Hiroto and I continue to argue and I don't think we can hide it
from them any longer.

One positive thing is that Akira is starting to feel better slowly.
I'm glad that even if I can improve my own situation, he is doing
well. It seems Kiyoko is keeping him company every day, like the
good girl she is. That and the medication will cure him."""
        print "\nPress enter to continue."
        raw_input("> ")
        print "\n"
        print """Suddenly all that progress sank down the drain. As if a whirlpool
stole it in front of my very eyes. Akira still smiles but his eyes
appear duller and duller. Kiyoko is still determined to cheer him
up. I depend on her when I cannot can him myself."""
        print "\nPress enter to continue."
        raw_input("> ")
        print "\n"
        print "I cannot continue to live with myself, with the knowledge that I..."
        print "\nThe page is torn."
        return 'library'
    elif c == "2":
        global name
        print "It is an encyclopedia of animals. The pages opened display a \ndrawing of two scorpions. These particular ones were fatal \nto humans."
        print "\n\t1: Turn the page. \n\t2: Never mind."
        c = raw_input("> ")
        if c == "1":
            print "While going to turn the page, my finger brushes the scorpion drawing. \nA shock of pain travels up my arm and my breath is short."
            print "\"%s, are you okay? Hey!\"" % name
            print "..."
            print "Due to failure to treat the sting, %s died within the next few days. \nThe three kids were unable to leave the house." % name
            print "\n"
            print "-----CONGRATULATIONS! YOU DIED!-----"
            exit(1)
        elif c == "2":
            return 'library'
        else:
            print "Please enter either 1 or 2."
            return 'library'
    else:
        print "Please enter either 1 or 2."
        return 'library'

# bro's room
def frame():
    global framev
    framev = True
    global pieces
    global code
    if pieces == 0:
        print "An empty frame lies on the ground, save for a post it note in \nthe corner. \"Find my photo.\""
        return 'b_room'
    elif pieces == 1:
        print "I put in the piece I found."
        return 'b_room'
    elif pieces == 2:
        print "I put in the parts I found. Now there is just one left."
        return 'b_room'
    elif pieces == 3:
        code = True
        print "The photo shows a scan code."
        inventory.update({'photo': "Put together from pieces around the second floor. This code can be used with a mobile camera."})
        del inventory['photo piece']
        return 'b_room'

# parent's room
def closet():
    global framev
    global pieces
    print "Suits, suits, suits... Underneath a fallen coat, a decorated box. \n\"To Dad: Happy Birthday! Don't work too hard! Love, the kids.\""
    print "Part of an image is attatched to the box."
    if framev == True:
        print "Maybe this is part of the photo."
        pieces += 1
        inventory.update({'photo piece': "One part of the photo."})
# parents' bathroom
def mirror():
    global framev
    global pieces
    print "Stained with toothbruh stains. A ripped corner of a photo is taped \nto the corner. It appears to be the boy from downstairs."
    if framev == True:
        print "Maybe this is part of the photo... I took the picture off. On the \nback was a black and white image. I can't tell what it is."
        pieces += 1
        inventory.update({'photo piece': "One part of the photo."})
# joint bathroom
def bathtub2():
    global small_key
    global framev
    global pieces
    print "A clear container sits in the tub. It appears to have a piece of \npaper on it, but requires a key to open it."
    if framev != True:
        return 'bathj'
    elif small_key == True:
        print "\"Ah, we can use the key from the drain.\" It turned out to be \na perfect fit. We got a photo piece."
    else:
        print "That piece might be part of the photo, but we need to find the key."

# kiyoko's room
def books():
    global codev
    global a_key
    print "Several science books are stacked near the bed. One book stands \nout from the rest, having a lock on it."
    print "Open the book?"
    print "\n\t1: Yes. \n\t2: No."
    c = raw_input("> ")
    print "\n"
    if c == "1":
        if codev == True:
            print "The book opened to reveal the pages are cut out. Another hollow \nbook. Inside is a key labelled for the attic. Would have been nicer \nif it were for the front door."
            a_key = True
            return 'k_room'
        else:
            print "The lock is real. We will need a key or something."
            return 'k_room'
    elif c == "2":
        return 'k_room'
    else:
        print "Please enter either 1 or 2."
        return 'k_room'


# computer room
def desktop():
    print "This PC is running. Currently, two programs are up: a web browser, and an unrecognizable icon."
    print "\n\t1: Look at the web browser. \n\t2: Look at the unrecognizable icon."
    c = raw_input("> ")
    print "\n"
    if c == "1":
        # print "a text on robert heath and his joy machine"
        return 'c_room'
    elif c == "2":
        global friendship
        pb = True
        print "\nAfter clicking the odd program, my friends, the girl, and I appeared."
        print "\n\"Ahh! It's a webcam! Close it!\" Alex exclaimed. I tried to close out, \nbut it wouldn't go away."
        print "\n\t1: Ask for a suggestion. \n\t2: Forget about it."
        c = raw_input("> ")
        if c == "1":
            friendship += 1
            print "I opened my mouth to ask, but Vinh beat me to it."
        elif c == "2":
            print "Vinh had a suggestion anyway."
        else:
            print "Please enter either 1 or 2."
            return 'c_room'
        print "\n\"Let's cover it.\""
        print "\n\"With what? We have no tape.\""
        print "\n\"Uh... I know! That sandwich I packed!\""
        print "\nwhat"
        print "\nVinh dug around in our bag and pulled out the disfigured food item. He \nproceeded to pinch the bagged sandwich around the desktop's webcam. \n\"PERFECT.\""
        print "\n\"... Right. Well... that's done, I guess...\""
        del inventory['pb&j sandwich']
        return 'c_room'
        if pb == True:
            print "No point in looking at that anymore."
    else:
        print "Please enter either 1 or 2."
        return 'c_room'

def wires():
    global friendship
    print "A haphazardous pile of wires lay near the television. \"What is this \ndoing here?\""
    print "Alex suddenly looks concerned, but she was scared since she came inside."
    print "\n\t1: Leave her alone. \n\t2: Ask her what's wrong."
    c = raw_input("> ")
    if c == "1":
        print "I needed not ask, because Alex addressed her concern soon enough."
    elif c == "2":
        friendship += 1
        print "\"Alex, are you alright?\""
    else:
        print "Please enter either 1 or 2."
        return 'c_room'
    print "\"Er, that ceiling tile doesn't look very safe, does it?\" She looks \nabove the wires, where a ceiling tile was close to falling. \nSomething appeared to be pushing it down."
    print "\n\t1: Poke the tile. \n\t2: Leave it alone."
    t = raw_input("> ")
    if t == "1":
        global trip
        trip = True
        print "I remember that we have a screwdriver from the kitchen that was \nrather long. Standing on a chair, I knock the ceiling tile away."
        print "Although I thought something would be there, there was not. The \nfloor above seemed to cave in some, here."
    elif t == "2":
        print "I figured it'd be okay. It held out for a while, so some more hours \nwould not bother it. I walked over to see the wires."
        print "\"%s, watch out!\" was the last thing I heard before a blunt object \nhit my neck."
        print "\n"
        print "-----CONGRATULATIONS! YOU DIED!-----"
        exit(1)
    else:
        print "Please enter either 1 or 2."
        return 'c_room'

def a_stairs():
    if a_key == True:
        print "\"Are you sure we should go up there?\" the girl said. \"It's \nprobably dangerous.\""
        print "\"Where else do we have to go?\""
        print "With that, we unlocked the door and climbed up."
        return 'attic'
    else:
        print "We need the attic stairs key."
        return 'c_room'

## inventory dictionaries
living_items = {'couch': "A few of the springs poked out from under the fabric. We \ndiscovered this only after Vinh flopped onto the couch \nand cut himself.\n",
    'armchair': armchair,
    'fireplace': fireplace,
    }
dining_items = {'table': "The table is set for four with a thick layer of dust covering \nthe cloth and dishware. There is a chair at each spot.\n",
    'paintings': paintings,
    }
kitchen_items = {'fridge': "A musty smell comes out when we open it. There is no \nelectricity or food in it. Thankfully, no signs of life, either.",
    'sink': "The faucet is dusty, but the sink itself is not. Water still runs.",
    'drawers': drawers,
    'cabinet': cabinet,
    }
bath1_items = {'toilet': "A standard toilet. Yellow decorates the rims and the water \nreflects it. Or... maybe it's not water.",
    'mirror': "The mirror has several stains and rust on the metal sides. \nNothing is inside of the mirror's cabinet.",
    'bathtub': bathtub,
    }
library_items = {'armchair': "A chair similar to that in the living room, but less lumpy \nand softer. It appears more used, from many days of reading and \nstudying.",
    'shelves': lib_shelves,
    'desk': desk,
    }
b_room_items = {'dresser': "When opened, it reeks of mothballs. Said mothball packets are empty, \nsince it's been forever since they've been changed.",
    'pictures': "A variety of paintings were put up near the bed, as well as an \nunfinished one on an easel at the foot of the bed. The paintings start \nbright, depicting monarch butterflies on sunny afternoons, flowers, \nthe ocean, but gradually take on darker colors, ending in a thunderstorm. \nLightning pierces the center of the last canvas. The unfinished \npainting is a half done portrait of a faceless girl.",
    'bed': "The blanket is unkempt, a teddy bear stuck in the folds near the pillow. A worn rabbit leans on its stuffed buddy.",
    'frame': frame,
    }
p_room_items = {'beds': "Although this appears to be the master bedroom, instead of one large \nbed, there are two twin sides beds with considerable distance between \nthem. One is unmade, the other looks as though it was never slept in.",
    'vanity': "A wooden jewelry box, and a few makeup products remain on the counter. \nThe wide mirror looks twice as dirty from the dust particles \nand their reflections.",
    'closet': closet,
    }
bathp_items = {'mirror': mirror,
    'toilet': "Pretty similar to the one on the first floor, but not as yellow. \nAs a whole, the rooms on the 2nd floor appear better than the first.",
    'bathtub': "The shower curtain had collapsed into the tub.",
    }
bathj_items = {'mirror': "A cup and a very, very worn toothbrush sits inside. Whoever used \nit either never went to Walmart to get a new one or brushed with \nthe power of a drill.",
    'toilet': "The lid is closed. I really don't know if I should open it.",
    'bathtub': bathtub2,
    }
k_room_items = {'dresser': "The drawers are locked. The countertop appears to have been \nwiped on accident, with only part of the top free of dust.",
    'bed': "The bed has only a frame and a mattress.",
    'books': books,
    }
c_room_items = {'desktop': desktop,
    'wires': wires,
    'television': "For some reason, this television still works. That static noise \nfills the mostly empty room. It occasionally switches to a music station.",
    'stairs': a_stairs,}

class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last scene
        current_scene.enter()

class Intro(Scene):
    def enter(self):
        print """I hate gossip. It lasts for two days and ruins lives. However,
this rumor was a decade's old one. Villagers heard screaming from
the rundown house at the end of the road. Although, no one has
lived there for years. Scouting out the house around Halloween is
very popular among the (idiotic) students at my school. They all
say that no one will come back alive if they go inside, but all
of that sounds like crap to me. Ghosts aren't even real.\n"""
        raw_input("Press enter to continue.")
        print """"Well, if you're not afraid and think it's nothing, let's go see
it, then! Nothing will happen, right?" my friend Vinh said.\n"""
        print """He\'s really into the horror genre and dare-devil things. Walking
into a creaky abandoned building fits right into his hobbies.\n"""
        print """"I mean... even if there aren't any ghosts, what if we get hurt?"
Alex, who has a hint of reason, added.\n"""
        print """"If the worst happens, we can just knock the door down. Besides,
are you a chicken, Alex?" Vinh proceeded to squawk and flap his
arms around Alex.\n"""
        raw_input("Press enter to continue.")
        print """"Hey, leave her alone. We can go for five minutes. Anything worth
seeing will be seen in that amount of time," I said.\n"""
        print """And so it was decided. That Friday evening, we walked to the house
at the end of the road. The front door wasn't even locked. Does no
one have watch over this property?\n"""
        print """The scene beyond the front door was filthy. Spiderwebs decorated
the doorframes and corners. The only light source, the fading sun
behind us, cast long shadows on the broken floor. A couple of
floorboards were missing, loose, or creaked beneath our feet. A
musty odor permeated through the hallway.\n"""
        raw_input("Press enter to continue.")
        print "\"Here we are, Vinh. Absolutely nothing to see.\"\n"
        print "\"Hey, don't talk so loudly! What if they ghost can hear us?\"\n"
        print "\"Vinh... you\'re the loud one here.\"\n"
        print "\"Who asked you, Alex?\"\n"
        print "\"Ah, cut it out. Let\'s leave. I\'m bored.\"\n"
        print """I turned back to the door, which had closed with a thud behind us.
The door knob rattled in my hand.\n"""
        raw_input("Press enter to continue.")
        print "\"Um.\"\n"
        print "I tried to turn it again.\n"
        print "\"Why won\'t it open?\"\n"
        print "\"Here, I didn\'t polish my karate kick for nothing! Hiyaaaa--\"\n"
        print "*THUD*\n"
        print "\"OUCH WHAT THE HECK?\" Vinh crumpled into the fetal position,"
        print "clutching his foot. \"I THOUGHT THIS DOOR WAS ROTTING.\"\n"
        print """Upon closer inspection, it would appear that the door had a layer
of iron supporting it. We tried the windows and walls near the door.
This building was determined to contain us, so we supposed the only
way was forward.\n"""
        return 'foyer'

## first floor
class foyer(Scene):
    def enter(self):
        global loc
        global hammerv
        global k
        loc = 'foyer'
        if hammerv == True and k != True:
            k = True
            print "\nWhen we entered the foyer this time, something was there that \nhadn't been before."
            print "\n\"What are you doing here? Isn't it dangerous?\" Vinh, of all people, \nsaid. A girl stood in front of us, looking as if we might hurt her."
            print "\n\"Um... My friends dared me to come here a while ago, but then \nthey got scared and left me... The door was locked from the inside \nso I couldn't get out...\""
            print "\n\"What terrible friends. But... we never heard anything before,\" \nsaid Alex."
            print "\n\"Well, when I heard the door I got scared so I hid in a closet \nI found. Although, a bit later I thought it could be my friends, \nbut you all sound quite different, so...\""
            print "\nI'd read enough books to know not to trust strangers. Especially \nthe ones you find in haunted houses. But you can make use of \nyour enemies, too. Four minds are better than three. Maybe."
            print "\n\"We'll be your new friends! Your other 'friends' suck. Let's \nget out of here together!\" the sometimes chivalrous Vinh said."
            print "\nThe girl smiled. \"Okay!\""
        else:
            print """We are in the foyer. Careful of the gaps in the floor. There are
two spiderwebs, one with fly carcasses and another with an active
spider, pulling its prey towards itself.\n"""
        print "Where will we go?"
        doors('foyer')
        global null
        if null == True:
            return 'foyer'
        else:
            return door

class dining(Scene):
    def enter(self):
        print "Perhaps at one point the walls were more vibrant, but now they are \na muted green. It\'s a really gross color, actually, like the green on"
        print "the outside of boiled egg yolks. Three frames, hang opposite of the \nentrance, a rectangular table separating us from them."
        action('dining')
        global null
        if null == True:
            return 'dining'
        else:
            return door

class kitchen(Scene):
    def enter(self):
        print "The floor tiles are half gone, exposing the rotting foundation. \nOther tiles are cracked. Vinh sneezed and the dust particles flew \ninto the last remnants of daylight."
        action('kitchen')
        global null
        if null == True:
            return 'kitchen'
        else:
            return door

class living(Scene):
    def enter(self):
        global bath1v
        bath1v = True
        print "\"Was this the living room? Looks more like the dying room now.\""
        print "\"If you could stop with the puns. We are stuck in a rotting, \ncreepy house. This is no joke.\""
        print "\"I'm just trying to lighten the mood, because these moldy \ncurtains sure aren't helping...\""
        action('living')
        global null
        if null == True:
            return 'living'
        else:
            bath1v = False
            return door

class bath1(Scene):
    def enter(self):
        print "Generally grimy, the bathroom appears to leave us dirtier after \nanyone tries to bathe here. An almost artistic cobweb stretches \nfrom the mirror to the broken lightswitch, a lone spider rolling \nmore fiber."
        action('bath1')
        global null
        if null == True:
            return 'bath1'
        else:
            return door

class library(Scene):
    def enter(self):
        global bath1v
        bath1v = True
        print "\"I love this room!\" Alex exclaimed. It was the least terrible one \nwe had come across so far. The shelves are stacked with books"
        print "of all colors, although faded from the sun. A thick layer of dust \ncovered the reddish brown wood. No fingerprints to be seen."
        action('library')
        global null
        if null == True:
            return 'library'
        else:
            bath1v = False
            return door

class basement(Scene):
    def enter(self):
        basement = True
        print "This is the basement."

class stairs(Scene):
    def enter(self):
        global hammerv
        global loc
        if hammerv != True:
            print "The stairs are padlocked. You cannot get through.\n"
            return 'foyer'
        if loc == 'foyer':
            print "We head upstairs."
            return 'hallway'
        elif loc == 'hallway':
            print "We head downstairs."
            return 'foyer'

## second floor
class hallway(Scene):
    def enter(self):
        global loc
        loc = 'hallway'
        print "It began to get dark, so only the dim light from downstairs illuminated \nthe doors. The hallway upstairs was narrower than the foyer, mostly \njust surrounding us with doors."
        print "Where should we go?"
        doors('hallway')
        global null
        if null == True:
            return 'hallway'
        else:
            return door

class p_room(Scene):
    def enter(self):
        global bathpv
        bathpv = True
        print "The large bedroom looked rather empty because of its few furnishings \nand bare walls. Surprisingly, the electricity still worked in this room... \nA few cobwebs in the corner cast spindly shadows on the walls."
        action('p_room')
        global null
        if null == True:
            return 'p_room'
        else:
            bathpv = False
            return door

class bathp(Scene):
    def enter(self):
        print "Although connected to the large bedroom, it's a small bathroom."
        action('bathp')
        global null
        if null == True:
            return 'bathp'
        else:
            return door

class b_room(Scene):
    def enter(self):
        global bathjv
        bathjv = True
        print "The clutter around the room makes it appear lived in, but a coat \nof dust over everything tells otherwise. Whoever lived here made \nthe most of their room."
        action('b_room')
        global null
        if null == True:
            return 'b_room'
        else:
            bathjv = False
            return door

class bathj(Scene):
    def enter(self):
        print "Another door faces us from the other side of the bathroom as we \nwalk in. There are some cracks in the ceiling from water damage."
        action('bathj')
        global null
        if null == True:
            return 'bathj'
        else:
            return door

class k_room(Scene):
    def enter(self):
        print "This room is completely void of character, except for a pile of books \nand some patches of discoloration on the walls. Some wire hangers \nfill the closet."
        action('k_room')
        global null
        if null == True:
            return 'k_room'
        else:
            return door

class c_room(Scene):
    def enter(self):
        print "The room is mostly empty, but it looks to be a good environment \nfor work or study. It partially looks to be for technological"
        print "storage, as well. What appears to be pull down stairs takes up \npart of the ceiling."
        action('c_room')
        global null
        if null == True:
            return 'c_room'
        else:
            return door

class attic(Scene):
    def enter(self):
        print "This is the attic."
        if basementv == True:
            return 'true'
        elif knifev == True and screwdriverv == True:
            return 'escape_t'
        # elif friendship > (some number):
        #   return 'experiment'
        else:
            return 'escape_a'
        return door

## endings
class experiment(Scene):
    def enter(self):
        print "Ending 1: All of you are used in experiment."
        exit(1)

class escape_a(Scene):
    def enter(self):
        print "Ending 2: You escape alone, your friends having volunteered to help Kiyoko."
        exit(1)

class escape_t(Scene):
    def enter(self):
        print "Ending 3: Everyone escapes the house."
        exit(1)

class true(Scene):
    def enter(self):
        print "Best Ending: You all and Kiyoko come to terms."
        exit(1)

class Map(object):
    scenes = {
        'Intro': Intro(),
        'basement': basement(),
        'foyer': foyer(),
        'dining': dining(),
        'living': living(),
        'library': library(),
        'bath1': bath1(),
        'kitchen': kitchen(),
        'stairs': stairs(),
        'hallway': hallway(),
        'b_room': b_room(),
        'p_room': p_room(),
        'bathp': bathp(),
        'bathj': bathj(),
        'k_room': k_room(),
        'c_room': c_room(),
        'attic': attic(),
        'experiment': experiment(),
        'escape_a': escape_a(),
        'escape_t': escape_t(),
        'true': true(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

## inventory function
def inventory_func():
    for i in inventory:
        print i + ": " + inventory[i]

## mapping function
def doors(room):
    global null
    null = False
    if isfunction(doors_dict[room]) == True:
        doors_dict[room]()
    else:
        print doors_dict[room]
    r = raw_input("\n> ")
    print "\n"
    global door
    global bath1v
    global bathpv
    global bathjv
    if r in dining_list:
        door = 'dining'
    elif r in living_list:
        door = 'living'
    elif r in kitchen_list:
        door = 'kitchen'
    elif r in library_list:
        door = 'library'
    elif r in basement_list:
        door = 'basement'
    elif r in bathroom_list and bath1v == True:
        door = 'bath1'
    elif r in bathroom_list and bathpv == True:
        door = 'bathp'
    elif r in bathroom_list and bathjv == True:
        door = 'bathj'
    elif r in foyer_list:
        door = 'foyer'
    elif r in stairs_list:
        door = 'stairs'
    elif r in hallway_list:
        door = 'hallway'
    elif r in lroom_list:
        door = 'b_room'
    elif r in lgroom_list:
        door = 'p_room'
    elif r in rroom_list:
        door = 'k_room'
    elif r in comproom_list:
        door = 'c_room'
    elif r in attic_list:
        door = 'attic'
    elif r in inventory_list:
        null = True
        inventory_func()
    else:
        null = True
        print "That is not a room in this house."

## items function
def item(room):
    global t
    print "\n"
    print items_dict[room]
    t = raw_input("> ")
    print "\n"
    if room == 'living':
        idict = living_items
    if room == 'dining':
        idict = dining_items
    if room == 'library':
        idict = library_items
    if room == 'bath1':
        idict = bath1_items
    if room == 'kitchen':
        idict = kitchen_items
    if room == 'b_room':
        idict = b_room_items
    if room == 'p_room':
        idict = p_room_items
    if room == 'bathp':
        idict = bathp_items
    if room == 'bathj':
        idict = bathj_items
    if room == 'k_room':
        idict = k_room_items
    if room == 'c_room':
        idict = c_room_items
    if t in inventory_list:
        inventory_func()
    if t not in idict:
        print "That item is not in this room."
    if isfunction(idict[t]) == True:
        idict[t]()
    else:
        print idict[t]

## action function
def action(room):
    global null
    null = False
    print "\nWhat will we do? \n\t1: Go to... \n\t2: Look at..."
    c = raw_input("\n> ")
    if c == "1":
        doors(room)
    elif c == "2":
        item(room)
        return room
    elif c in inventory_list:
        inventory_func()
    else:
        print "Please enter 1 or 2."
        return room

a_map = Map('Intro')
a_game = Engine(a_map)
a_game.play()
