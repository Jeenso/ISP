class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('trial')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Intro(Scene):

    def enter(self):
        print "This will be the very first scene. I'm testing that everything runs in the right order."
        return 'foyer'

class Foyer(Scene):
    def enter(self):
        print "Now we are in the foyer. From here you can move to the dining room, the living room, or the library."
        print "Where will you go?"
        print "1: Dining room; 2: Living room; 3: Library"

        f = raw_input("> ")

        if f == "1":
            return 'dining'
        elif f == "2":
            return 'living'
        elif f == "3":
            return 'library'
        else:
            print "Please enter either 1, 2, or 3."
            return 'foyer'

class dining(Scene):
    def enter(self):
        print "This is the dining room."
        return 'trial'

class living(Scene):
    def enter(self):
        print "This is the living room."
        return 'trial'

class library(Scene):
    def enter(self):
        print "This is the library."
        return 'trial'

class trial(Scene):
    def enter(self):
        print "This is the end of the trial run."


class Map(object):

    scenes = {
        'Intro': Intro(),
        'foyer': Foyer(),
        'dining': dining(),
        'living': living(),
        'library': library(),
        'trial': trial(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('Intro')
a_game = Engine(a_map)
a_game.play()
