import pyglet
from Game import areas, sounds, GameEngine
from pyglet.window import key

speak = GameEngine.speak

pyglet.options['search_local_libs'] = True


class Menu:
    def __init__(self, keys):
        self.status = 'game'
        self.keys = keys
        self.main_menu = ['graj', 'wyjscie']
        self.current_menu = self.main_menu
        self.focus = self.current_menu[0]
        self.mission_menu = ['trening', 'powrot']
        self.focuscounter = 0
        self.clicksound = sounds.focus
        self.focussound = sounds.shiftfocus
        self.trening = GameEngine.Gra(keys=self.keys, area=areas.trening, special=-1, tasklog='zestrzel ogromna tarcze')
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

class GameWin(Menu):
    def update(self):
        if self.keys[key.ENTER]:
            startgame(Menu(keys=Keys))
        else:
            speak(('gratulacje, ukonczyles ta misje, wcisnij enter aby przejsc do menu glownego'))

class GameOver(Menu):
    def update(self):
        if self.keys[key.ENTER]:
            startgame(Menu(keys=Keys))
        else:
            speak(('przegrales, wcisnij enter aby przejsc do glownego menu'))

Keys = key.KeyStateHandler()
game_window = pyglet.window.Window()
game_window.push_handlers(Keys)

game = Menu(keys=Keys)


def startgame(mission):
    global game
    game = mission





def moving(dt):
    global game
    game.moving()
    if game.status == 'gameover':
        game = GameOver(keys=Keys)
    if game.status == 'win':
        game = GameWin(keys=Keys)
def update(dt):
    global game
    game.update()


@game_window.event
def on_draw():
    game_window.clear()
    game_window.set_caption('earwax game fps')


pyglet.clock.schedule_interval(moving, 0.3)
pyglet.clock.schedule_interval(update, 0.1)
pyglet.app.run()

"""wrzocam to tutaj, male wytlumaczenie co do mechanizmu zadan i wygrywania.
generalnie zakladam ze beda zadania trzech typow:
zabij wszystkich, zdobac cos tam i zabij konkretnego npca.
aby uporac sie z tym zadaniem i nie wchodzic w jakies dlugie kodowanie skomplikowanych zalerznosci - bla bla zrobilem tak:
powstala specjalna klasa SpecialObject oraz dodatkowy atrybut dla npc - special i dla klasy player(gracza) - special.
atrybut special dla playera jest ustawiany z klasy Gra - poprzez inicjalizacje tejze - ona rowniez posiada atrybut special, ten special jest przekazywany do instancji klasy player i... wlasnie.
co to znaczy - oznacza ilosc obiektow do zdobycia wyrazona w liczbie ujemnej, czyli jezeli:
mamy za zadanie - zdobyc cos tam, skrzynke, tarcze, glowice nuklearna... cokolwiek, tworzymy specialobiekt z odpowiednia nazwa i umieszczamy go w area.object.
albo jezeli mamy do zabicia jakiegos npca aby zaliczyc misje - zmieniamy atrybut moba, lub tworzymy moba z atrybutem special jako True.
w grze jest mechanizm ktory dodaje wszystkie speciale do siebie - gdy ich liczba osiagnie 0 (przypominam jest minusowa, jezeli nie bedzie na minusie to misja nigdy sie nie zaliczy) - wtedy zaliczy nam misje i przeniesie nas do okna GameWin."""