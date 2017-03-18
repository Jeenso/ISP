from inspect import isfunction

# print read me document before starting game -> tells instructions and guidelines
# update software specs

## vocabulary
dining_list = ["dining", "dining room", "Dining", "Dining Room", "Dining room"]
living_list = ["living", "living room", "Living", "Living Room", "Living room"]
kitchen_list = ["Kitchen", "kitchen"]
library_list = ["Library", "library", "Lib", "lib"]
bathroom_list = ["Bathroom", "bathroom", "bath", "Bath"]
foyer_list = ["Foyer", "foyer"]
stairs_list = ["stairs", "steps", "Stairs", "Steps"]
    # rooms leading to stairs will need a location value (true or false)
    # in stairs class, use the conditional to decide where to go
    # will the stairs lead to basement and attic as well or will those have their own classes
inventory_list = ["inventory", "Inventory", "items", "Items", "Things", "Stuff", "things", "stuff"]

def library():
    if basement == True:
        print "Living Room    Bathroom    Foyer    Basement"
    else:
        print "Living Room    Bathroom    Foyer"

## dialogue dictionaries
doors_dict = {'foyer': "Dining Room    Living Room    Library    Upstairs",
    'living': "Dining Room    Kitchen    Library    Bathroom    Foyer",
    'dining': "Kitchen    Living Room    Foyer",
    'kitchen': "Dining Room    Living Room",
    'bath1': "Living Room    Library",
    'library': library,
    'hallway': "Downstairs    Large Bedroom    Left Bedroom    Right Bedroom    Computer Room",
    'b_room': "Hallway    Bathroom",
    'p_room': "Hallway    Bathroom",
    'bathp': "Large Bedroom",
    'bathj': "Left Bedroom    Right Bedroom",
    'k_room': "Hallway    Bathroom    Computer Room",
    'c_room': "Hallway    Right Bedroom    Attic",
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
    'c_room': "desktop    laptop    wires    television",
    }

## variables
# REMEMBER to go through where variables are and write in new items to the inventory!
hammerv = False
crowbarv = False
screwdriverv = False
upstairs = 3
ticks = False
basementv = False
knifev = False
screwdriverv = False
# drain item
friendship = 0

## inventory
inventory = { } # figure out how to print dictionaries
# how do I say "if inventory is empty, print "you don't have any items"?

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
    print "\nThe paintings on either side of the center portrait seem \nto have been done professionally. The first depicts a couple,""
    print "possibly the previous owners of the house. The last portrait \nis of a young boy with a large grin. The middle frame is empty"
    print "and whatever used to be there was replaced by a cartoon \nstrip. A girl waves from the first panel, saying, \"Let\'s have"
    print "a scavenger hunt!\" The next three panels had a chair, a \nbook, and the word 'arachnids'.\n"

# kitchen
def drawers():
    global friendship
    drawersv =+ 1
    if drawersv > 2:
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
                print "I opened the drawer fully and find a knife at the back."
                return 'kitchen'
            else:
                print "Please enter either 1 or 2."
                return 'kitchen'

def cabinet():
    print "\nInside the cabinet, there was a bulky toolbox with a \ncombination lock."
    print "Enter the code."
    c = raw_input("> ")
    print "\n"
        if c == "777":
            crowbar = True
            hammerv = True
            screwdriverv = True
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
                    print "\"Dude, let me help you. You\'re struggling big time.\" Vinh and Alex \nended up having to take a tool each so we could transport them.""
                else:
                    print "Please enter either 1 or 2."
                    return 'kitchen'
        else:
            print "Apparently, that wasn\'t right. The toolbox stays shut."
            return 'kitchen'

# bathroom 1
def bathtub():
    print "\nThe bathtub might have been white originally but is brown \nfrom years of dirt. The only shining part is the drain, which \nis loose."
    print "\nLook in the drain?"
    print "\t1: Yes.\n\t2: No."
    c = raw_input("> ")
    print "\n"
    if c == "1":
        if crowbarv == True:
            # drain item = True
            print "We used the crowbar we got from the toolbox and pried open \nthe drain. A (something) had been dangling in the drain. It was wet."
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
        #3 golden spined books
        #A science text about Jose Delgado
        return 'library'
    elif c == "2":
        #2 golden spined books
        #A children's tale
        return 'library'
    elif c == "3":
        #1 golden spined book
        #A hollow book.
        return 'library'
    elif c == "4":
        print "A recipe book is open to directions for the perfect pancake. \nAttached is a sticky note, reading, \"Pancakes are flat.""
        print "Under that in a drippy red text, \"AND SO ARE YOU.\""
        print "*SLAM*"
        print "The bookshelves come together with a sticky crimson substance \nin between. It probably used to be you, the player."
        print "\n"
        print "-----CONGRATULATIONS! YOU DIED!-----"
        exit(1)
    else:
        print "Please enter 1, 2, 3, or 4."
        return 'library'

def desk():
    print "stuff"

# bro's room
def frame():
    print "stuff"

# parent's bathroom
def mirror():
    print "stuff"

# kiyoko's room
def books():
    print "stuff"

# computer room
def desktop():
    print "stuff"

def wires():
    print "stuff"

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
bath1_items = {'toilet': "A standard toilet. Yellow decorates the rims and the bowl \nlacks water.",
    'mirror': "The mirror has several stains and rust on the metal sides. \nNothing is inside of the mirror's cabinet.",
    'bathtub': bathtub,
    }
library_items = {'armchair': "A chair similar to that in the living room, but less lumpy \nand softer. It appears more used, from many days of reading and \nstudying.",
    'shelves': lib_shelves,
    'desk': desk,
    }
b_room_items = {'dresser': "stuff",
    'pictures': "stuff",
    'bed': "stuff",
    'frame': frame,
    }
p_room_items = {'beds': "stuff",
    'vanity': "stuff",
    'closet': "Stuff",
    }
bathp_items = {'mirror': mirror,
    'toilet': "Stuff",
    'bathtub': "stuff",
    }
bathj_items = {'mirror': "stuff",
    'toilet': "stuff",
    'bathtub': "stuff",
    }
k_room_items = {'dresser': "stuff",
    'bed': "stuff",
    'books': books,
    }
c_room = {'desktop': desktop,
    'laptop': "stuff",
    'wires': wires,
    'television': "stuff",
    }

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
        print """"Well, if you're not afraid and think it's nothing, let's go see
it, then! Nothing will happen, right?" my friend Vinh said.\n"""
        print """He\'s really into the horror genre and dare-devil things. Walking
into a creaky abandoned building fits right into his hobbies.\n"""
        print """"I mean... even if there aren't any ghosts, what if we get hurt?"
Alex, who has a hint of reason, added.\n"""
        print """"If the worst happens, we can just knock the door down. Besides,
are you a chicken, Alex?" Vinh proceeded to squawk and flap his
arms around Alex.\n"""
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
        print "\"Here we are, Vinh. Absolutely nothing to see.\"\n"
        print "\"Hey, don't talk so loudly! What if they ghost can hear us?\"\n"
        print "\"Vinh... you\'re the loud one here.\"\n"
        print "\"Who asked you, Alex?\"\n"
        print "\"Ah, cut it out. Let\'s leave. I\'m bored.\"\n"
        print """I turned back to the door, which had closed with a thud behind us.
The door knob rattled in my hand.\n"""
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
        print """We are in the foyer. Careful of the gaps in the floor. There are
two spiderwebs, one with fly carcasses and another with an active
spider, pulling its prey towards itself.\n"""
        print "Where will we go?"
        doors('foyer')
        return door

class dining(Scene):
    def enter(self):
        print "Perhaps at one point the walls were more vibrant, but now they are \na muted green. It\'s a really gross color, actually, like the green on"
        print "the outside of boiled egg yolks. Three frames, hang opposite of the \nentrance, a rectangular table separating us from them."
        action('dining')
        return door

class kitchen(Scene):
    def enter(self):
        print "The floor tiles are half gone, exposing the rotting foundation. \nOther tiles are cracked. Vinh sneezed and the dust particles flew \ninto the last remnants of daylight."
        action('kitchen')
        return door

class living(Scene):
    def enter(self):
        print "This is a description of the living room."
        action('living')
        return door

class bath1(Scene):
    def enter(self):
        print "This is the first floor bathroom."
        action('bath1')
        return door

class library(Scene):
    def enter(self):
        print "This is the library."
        action('library')
        return door

class basement(Scene):
    def enter(self):
        basement = True
        print "This is the basement."

class stairs(Scene):
    def enter(self):
        if hammerv != True:
            print "The stairs are padlocked. You cannot get through.\n"
            return 'foyer'
        if upstairs % 2 == 0:
            print "You are now on the first floor."
        else:
            print "You are now on the second floor."

## second floor
class hallway(Scene):
    def enter(self):
        print "This is the upstairs central hallway."
        door('hallway')
        return door

class p_room(Scene):
    def enter(self):
        print "This is Kiyoko's parents' room."
        action('p_room')
        return door

class bathp(Scene):
    def enter(self):
        print "This is the parents' bathroom."
        action('bathp')
        return door

class b_room(Scene):
    def enter(self):
        print "This is Kiyoko's brother's room."
        action('b_room')
        return door

class bathj(Scene):
    def enter(self):
        print "This is the joint bathroom."
        action('bathj')
        return door

class k_room(Scene):
    def enter(self):
        print "This is Kiyoko's room."
        action('k_room')
        return door

class c_room(Scene):
    def enter(self):
        print "This is the computer room."
        action('c_room')
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

## mapping function
def doors(room):
    if isfunction(doors_dict[room]) == True:
        doors_dict[room]()
    else:
        print doors_dict[room]
    r = raw_input("\n> ")
    print "\n"
    global door
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
    else:
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
    if t not in idict:
        print "That item is not in this room."
    elif isfunction(idict[t]) == True:
        idict[t]()
    else:
        print idict[t]

## action function
def action(room):
    print "\nWhat will we do? \n\t1: Go to... \n\t2: Look at..."
    c = raw_input("\n> ")
    if c == "1":
        doors(room)
    elif c == "2":
        item(room)
        return room
    elif c in inventory_list:
        print inventory
        # figure out how to format printing
    else:
        print "Please enter 1 or 2."
        return room

## plot event (key dialogue) function

a_map = Map('Intro')
a_game = Engine(a_map)
a_game.play()
