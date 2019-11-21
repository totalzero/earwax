from . import sounds
from .classes import Npc

tarcza = Npc(name='cwiczeniowa tarcza strzelecka',
desc = 'treningowa tarcza strzelecka, na ktorej pocwiczysz strzelanie',
x = 20,
y = 20,
hp = 10,
walker=False,
aggresiv=False)

tarcza.injured = sounds.npc['treninginjured']
tarcza.died = sounds.npc['treningdied']

soldier = Npc(name='zolnierz',
desc='standardowo uzbrojony zolnierz wroga',
aggresiv=True,
walker=True,
hp=100,
x=10,
y=10)

officer = Npc(name='oficer wojsk wroga',
desc='oficer wrogiej armi',
aggresiv=False,
walker=True,
hp=250,
x=5,
y=5)

general = Npc(name='general',
desc='glowny general wojsk wroga',
aggresiv=False,
walker=False,
hp=500,
x=5,
y=5)

cywil=Npc(name='cywil',
desc='cywil, nie wolno ci ich zabijac, pamietaj',
aggresiv=False,
walker=True,
hp=50,
x=1,
y=1)