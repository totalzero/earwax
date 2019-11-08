import copy
from random import randint
from . import guns, sounds, mobs
from .classes import Location, Area, Exit

macarow = copy.deepcopy(guns.macarow)
macarow.x, macarow.y = 10, 10
ammo_macarow = copy.deepcopy(guns.macarowammo)
ammo_macarow.x, ammo_macarow.y = 10, 10

baza1 = None

baza_wejscie = Exit(name='wyjscie do bazy',
x = 0,
y = 0,
sound = sounds.doors[1],
area = baza1)

posterunek = Area(name='posterunek',
desc='posterunek',
max_x=25,
max_y=25,
exits=[baza_wejscie],
object = [macarow, ammo_macarow, ammo_macarow, ammo_macarow])

posterunek_wejscie = Exit(name='posterunek',
x=5,
y=5,
sound = sounds.doors[1],
area = posterunek)




baza1 = Area(name='baza',
desc = 'przykladowa kraina',
max_x=100,
max_y=100,
exits=[posterunek_wejscie],
npcs=[copy.deepcopy(mobs.soldier)])


