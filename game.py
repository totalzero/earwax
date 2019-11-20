import pyglet
from Game import areas, sounds, GameEngine
from pyglet.window import key

speak = GameEngine.speak

pyglet.options['search_local_libs'] = True


class Menu:
    def __init__(self, keys):
        self.keys = keys
        self.main_menu = ['graj', 'wyjscie']
        self.current_menu = self.main_menu
        self.focus = self.current_menu[0]
        self.mission_menu = ['trening', 'powrot']
        self.focuscounter = 0
        self.clicksound = sounds.focus
        self.focussound = sounds.shiftfocus
        self.trening = GameEngine.Gra(keys=self.keys, area=areas.baza1)
    def action(self, focus):
        if focus == 'wyjscie':
            pyglet.app.exit()
        if focus == 'graj':
            self.current_menu = self.mission_menu
        if focus == 'powrot':
            self.current_menu = self.main_menu
        if focus == 'trening':
            startgame(self.trening)

    def update(self):
        if self.focuscounter >= len(self.current_menu):
            self.focuscounter = 0
        if self.focuscounter <0:
            self.focuscounter = 0

        if self.keys[key.UP]:
            self.focuscounter -=1
            self.focus = self.current_menu[(self.focuscounter -1)]
            speak((str(self.focus)))
            self.focussound.play()
        if self.keys[key.DOWN]:
            self.focuscounter +=1
            self.focus = self.current_menu[(self.focuscounter -1)]
            speak((str(self.focus)))
            self.focussound.play()

        if self.keys[key.ENTER]:
            self.action(self.focus)
            self.clicksound.play()

    def moving(self):
        pass


Keys = key.KeyStateHandler()
game_window = pyglet.window.Window()
game_window.push_handlers(Keys)

game = Menu(keys=Keys)


def startgame(mission):
    global game
    game = mission





def moving(dt):
    game.moving()

def update(dt):
    game.update()


@game_window.event
def on_draw():
    game_window.clear()


pyglet.clock.schedule_interval(moving, 0.3)
pyglet.clock.schedule_interval(update, 0.1)
pyglet.app.run()