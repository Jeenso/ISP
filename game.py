# print read me document before starting game
# read(file) -> print file
# update software specs

items = {
    'couch': "Here is a description of the couch.",
    'armchair': "A description of the armchair. 2 ticks crawl onto your hand.",
    }

# this definition should be able to process the different doors from each room.
# how can I use a dictionary to put through other lists of stuff?

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
    'kitchen': "refrigerator    sink    drawers    cabinet",
    'bath1': "toilet    mirror    bathtub",
    'library': "armchair    shelves    desk"
    }

hammer = False
upstairs = 3

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
        print "This will be the very first scene. I'm testing that everything runs in the right order.\n"
        return 'foyer'

class foyer(Scene):
    def enter(self):
        print "Now we are in the foyer. From here you can move to the dining room, the living room, or the library."
        print "Where will you go?"
        doors('foyer')
        return door

class dining(Scene):
    def enter(self):
        print "This is the dining room."
        print "What do you want to do?"
        print "1: Go to..."
        print "2: Look at..."
        c = raw_input("> ")

        if c == "1":
            doors('dining')
            return door
        elif c == "2":
            item('dining')
            return 'dining'
        else:
            print "Please enter 1 or 2."
            return 'dining'

class living(Scene):
    def enter(self):
        print "This is a description of the living room."
        print "What do you want to do?"
        print "1: Go to..."
        print "2: Look at..."
        c = raw_input("> ")

        if c == "1":
            doors('living')
            return door
        elif c == "2":
            item('living')
            return 'living'
        else:
            print "Please enter 1 or 2."
            return 'living'



class library(Scene):
    def enter(self):
        print "This is the library."
        print "What do you want to do?"
        print "1: Go to..."
        print "2: Look at..."
        c = raw_input("> ")

        if c == "1":
            doors('library')
            return door
        elif c == "2":
            item('library')
            return 'library'
        else:
            print "Please enter 1 or 2."
            return 'library'

class kitchen(Scene):
    def enter(self):
        print "This is the kitchen."
        print "What do you want to do?"
        print "1: Go to..."
        print "2: Look at..."
        c = raw_input("> ")

        if c == "1":
            doors('kitchen')
            return door
        elif c == "2":
            item('kitchen')
            return 'kitchen'
        else:
            print "Please enter 1 or 2."
            return 'kitchen'

class bath1(Scene):
    def enter(self):
        print "This is the first floor bathroom."
        print "What do you want to do?"
        print "1: Go to..."
        print "2: Look at..."
        c = raw_input("> ")

        if c == "1":
            doors('bath1')
            return door
        elif c == "2":
            item('bath1')
            return 'bath1'
        else:
            print "Please enter 1 or 2."
            return 'bath1'

class stairs(Scene):
    def enter(self):
        if hammer != True:
            print "The stairs are padlocked. You cannot get through.\n"
            return 'foyer'
        if upstairs % 2 == 0:
            print "You are now on the first floor."
        else:
            print "You are now on the second floor."

class trial(Scene):
    def enter(self):
        print "This is the end of the trial run."
        exit(1)

class Map(object):
    scenes = {
        'Intro': Intro(),
        'foyer': foyer(),
        'dining': dining(),
        'living': living(),
        'library': library(),
        'bath1': bath1(),
        'kitchen': kitchen(),
        'stairs': stairs(),
        'trial': trial(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

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


def item(room):
    global i
    print items_dict[room]
    i = raw_input("> ")

a_map = Map('Intro')
a_game = Engine(a_map)
a_game.play()
