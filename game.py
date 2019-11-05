import pyglet
from Game import GameEngine
from pyglet.window import key

pyglet.options['search_local_libs'] = True



Keys = key.KeyStateHandler()
game = GameEngine.Gra(keys=Keys)
game_window = pyglet.window.Window()
game_window.push_handlers(Keys)

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