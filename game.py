from inspect import isfunction

# print read me document before starting game -> tells instructions and guidelines
# read(file) -> print file
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

## dialogue dictionaries
doors_dict = {'foyer': "Dining Room    Living Room    Library    Upstairs",
    'living': "Dining Room    Kitchen    Library    Bathroom    Foyer",
    'dining': "Kitchen    Living Room    Foyer",
    'kitchen': "Dining Room    Living Room",
    'bath1': "Living Room    Library",
    'library': "Living Room    Bathroom    Foyer",
    # conditional to show basement after discovering it
    }

items_dict = {'living': "couch    armchair",
    'dining': "table    fireplace    paintings",
    'kitchen': "fridge    sink    drawers    cabinet",
    'bath1': "toilet    mirror    bathtub",
    'library': "armchair    shelves    desk"
    }

## variables
hammer = False
upstairs = 3

## inventory
inventory = { } # figure out how to print dictionaries
# how do I say "if inventory is empty, print "you don't have any items"?

## inventory functions
#def armchair():

def fireplace():
    print """Cold and dark, it still has years old ashes covering the bottom.
It appears we can look inside of it to the other floors. A spider
stares from the corner."""
    print "Look inside? \n\t1: Yes. \n\t2: No."
    f = raw_input("> ")
    if f == "1":
        print "I crawled into the fireplace to look up. The last thing I saw \nwas plummeting brick and a shower of ash.\n"
        print "-----CONGRATULATIONS! YOU DIED!-----"
        exit(1)
    elif f == "2":
        return 'dining'
    else:
        print "Please enter either 1 or 2."
        return 'dining'

## inventory dictionaries
living_items = {'couch': "This is the couch. test.",
    #'armchair':, # replace with function
    }
dining_items = {'table': "The table is set for four with a thick layer of dust covering \nthe cloth and dishware. There is a chair at each spot.",
    'fireplace': fireplace,
    #'paintings':, # replace with function
    # use a dict for the entry for paintings?
    }
kitchen_items = {'fridge': "This is the refrigerator.",
    'sink': "This is the sink.",
    #'drawers':, # replace with function
    #'cabinet':, # replace with function
    }
bath1_items = {'toilet': "A standard toilet.",
    'mirror': "The mirror has several stains and rust on the metal sides. It has hinges, so it appears to be a cabinet as well.",
    #'bathtub':, # replace with function
        #"The bathtub might have been white originally but is brown from years of dirt. The only shining part is the drain, which is loose."
    }
library_items = {'armchair': "It's a chair. It is soft. aju noice",
    #'shelves':, # replace with function
        # "There are three shelves. The spaces between are pretty wide. There are some fallen books."
        # " I think this section needs a dictionary?",
    #'desk':, # replace with function"
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
        print """From the foyer, we can move to the dining room, the living room,
or the library. Where should we go?"""
        doors('foyer')
        return door

class foyer(Scene):
    def enter(self):
        print """We are in the foyer. Careful of the gaps in the floor. There are
two spiderwebs, one with flie carcasses and another with an active
spider, pulling its prey towards itself."""
        print "Where will you go?"
        doors('foyer')
        return door

class dining(Scene):
    def enter(self):
        print "This is the dining room."
        action('dining')
        return door

class living(Scene):
    def enter(self):
        print "This is a description of the living room."
        action('living')
        return door

class library(Scene):
    def enter(self):
        print "This is the library."
        action('library')
        return door

class kitchen(Scene):
    def enter(self):
        print "This is the kitchen."
        action('kitchen')
        return door

class bath1(Scene):
    def enter(self):
        print "This is the first floor bathroom."
        action('bath1')
        return door

class stairs(Scene):
    def enter(self):
        if hammer != True:
            print "The stairs are padlocked. You cannot get through.\n"
            return 'foyer'
        if upstairs % 2 == 0:
            print "You are now on the first floor."
        else:
            print "You are now on the second floor."

class basement(Scene):
    def enter(self):
        print "This is the basement."

class trial(Scene):
    def enter(self):
        print "This is the end of the trial run."
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
        # upstairs central hallway
        # bro's room
        # parents' room
        # parents' bathroom
        # joint bathroom
        # kiyoko's room
        # computer room
        # attic
        'trial': trial(), # replace with ending
            # classes for each ending (4)
                # used in experiment
                    # didn't meet requirement for ending 3 but
                    # friendship > (some number)
                # escape alone
                    # didn't meet requirement for ending 1 or 3
                # escape together
                    # requires knife == True and screwdriver == True
                # secret ending
                    # requires basement == True
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
    print doors_dict[room]
    r = raw_input("> ")
    global door
    if r in dining_list:
        door = 'dining'
    elif r in living_list:
        door = 'living'
    elif r in kitchen_list:
        door = 'kitchen'
    elif r in library_list:
        door = 'library'
    elif r in bathroom_list:
        door = 'bath1'
    elif r in foyer_list:
        door = 'foyer'
    elif r in stairs_list:
        door = 'stairs'
    else:
        print "That is not a room in this house."

## items function
def item(room):
    global t
    print items_dict[room]
    t = raw_input("> ")
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
    print "What will we do? \n\t1: Go to... \n\t2: Look at..."
    c = raw_input("> ")
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
