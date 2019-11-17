import copy
from random import randint
from . import guns, sounds, mobs
from .classes import Location, Area, Exit

macarow = copy.deepcopy(guns.macarow)
macarow.x, macarow.y = 10, 10
ammo_macarow = copy.deepcopy(guns.macarowammo)
ammo_macarow.x, ammo_macarow.y = 10, 10

posterunek = Area(name='posterunek',
desc='posterunek',
x=5,
y=5,
max_x=25,
max_y=25,
sound = sounds.doors[1],
npcs=[copy.deepcopy(mobs.soldier), copy.deepcopy(mobs.soldier)],
object = [macarow, ammo_macarow, ammo_macarow, ammo_macarow])

baza1 = Area(name='baza',
desc = 'przykladowa kraina',
max_x=100,
max_y=100,
exits=[posterunek],
sound = sounds.doors[1],
npcs=[copy.deepcopy(mobs.soldier), copy.deepcopy(mobs.soldier), copy.deepcopy(mobs.soldier)])


