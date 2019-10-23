import pyglet
from Game import classes
from pyglet.window import key

pyglet.options['search_local_libs'] = True
pyglet.resource.path = ['/Resources', '../Resources', 'Resources']
pyglet.resource.reindex()



keys = key.KeyStateHandler()
game = classes.Gra(keys=keys)
game_window = pyglet.window.Window()
game_window.push_handlers(keys)

def moving(dt):
    game.moving()

def update(dt):
    game.update()
    for x in game.area.npcs:
        x.update()

@game_window.event
def on_draw():
    game_window.clear()



pyglet.clock.schedule_interval(moving, 0.3)
pyglet.clock.schedule_interval(update, 0.1)
pyglet.app.run()