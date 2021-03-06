from . import sounds
from .classes import Pistols, Snajper, Carabines, Grenades, Knifes, Medpack, Ammo

knife = Knifes(name='noz',
desc='noz do mordowania',
missiles = 1,
is_reload=False,
damage=40,
fire_sound=sounds.knife['fire'],
aims_at=sounds.knife['aimsat'])


beretta = Pistols(name = 'beretta 9mm',
desc = 'pistolet beretta 9mm, na amunicje 9mm parabellum',
is_reload = True,
missiles =20,
maxbullets=20,
damage = 225,
fire_sound = sounds.beretta['fire'],
get_sound = sounds.beretta['get'],
empty_sound = sounds.beretta['empty'],
reload_sound = sounds.beretta['reload'],
aims_at = sounds.beretta['aimsat'])

macarow = Pistols(name = 'pistolet macarow',
desc = 'slawny na caly swiat rosyjski pistolet macarow, na amunicje 9mm',
is_reload = True,
damage = 30,
missiles=20,
maxbullets=20,
fire_sound = sounds.macarow['fire'],
get_sound = sounds.macarow['get'],
empty_sound = sounds.macarow['empty'],
reload_sound = sounds.macarow['reload'],
aims_at = sounds.macarow['aimsat'])

ak47 = Carabines(name='karabin ak47',
desc = 'karabin szturnowy ak47',
is_reload = True,
damage = 75,
missiles=45,
maxbullets=45,
fire_sound = sounds.ak47['fire'],
get_sound = sounds.ak47['get'],
empty_sound = sounds.ak47['empty'],
reload_sound = sounds.ak47['reload'],
aims_at = sounds.ak47['aimsat'])

dragunow = Snajper(name='karabin snajperski swd',
desc = 'karabin snajperski swd dragunow',
is_reload = True,
damage = 1000,
missiles = 5,
maxbullets=5,
spare_ammunition=2,
fire_sound = sounds.dragunow['fire'],
get_sound = sounds.dragunow['get'],
empty_sound = sounds.dragunow['empty'],
reload_sound = sounds.dragunow['reload'],
aims_at = sounds.dragunow['aimsat'])

barret82 = Snajper(name='karabin snajperski barret82A1',
desc = 'karabin snajperski jednostek specjalnych delta force',
is_reload=True,
x=5,
y=5,
missiles=10,
maxbullets=10,
spare_ammunition=2,
damage = 1000,
fire_sound=sounds.barret['fire'],
get_sound=sounds.barret['get'],
reload_sound=sounds.barret['reload'],
aims_at=sounds.barret['aimsat'],
empty_sound=sounds.barret['empty'])

mp4 = Carabines(name='pistolet maszynowy mp4',
desc='pistolet maszynowy mp4',
missiles = 50,
maxbullets=50,
is_reload=True,
damage=50,
x=0,
y=0,
fire_sound=sounds.mp4['fire'],
empty_sound=sounds.mp4['empty'],
reload_sound=sounds.mp4['reload'],
get_sound=sounds.mp4['get'],
aims_at=sounds.mp4['aimsat'])

pp19 = Carabines(name='pp19 bizon',
desc='pistolet maszynowy pp19 bizon',
missiles = 64,
maxbullets=64,
is_reload=True,
damage = 50,
fire_sound = sounds.pp19['fire'],
empty_sound=sounds.pp19['empty'],
reload_sound=sounds.pp19['reload'],
get_sound=sounds.pp19['get'],
aims_at=sounds.pp19['aimsat'])

grenade = Grenades(name='granatnik',
desc='granat jak to granat, nie ma tu co opisywac',
fire_sound=sounds.grenade['fire'],
aims_at=sounds.grenade['aimsat'],
get_sound=sounds.grenade['get'],
missiles = 3,
spare_ammunition=5)

medpack = Medpack(name='pakiet medyczny',
desc='podstawowy pakiet medyczny niezbedny podczas misji',
missiles=1,
damage=1,
fire_sound = sounds.medpack['fire'],
spare_ammunition=5)

medpackammo = Ammo(name='pakiet medyczny',
desc = 'podstawowy pakiet medyczny',
x=2,
y=2,
bullets=1,
type=medpack.name)

granatammo = Ammo(name='granat',
desc='granat, moze ci sie przydac',
x=0,
y=0,
bullets=1,
type=grenade.name)

parabellum = Ammo(name='magazynek do beretty',
desc = 'najpopularniejsza na swiecie amunicja 9mm parabellum do pistoletow i pistoletow maszynowych',
x = 10,
y = 10,
bullets = 20,
type = beretta.name)

mp4ammo = Ammo(name='magazynek do mp4',
desc='amunicja parabellum w magazynku przeznaczonym do pistoletu maszynowego mp4',
x=0,
y=0,
bullets = 50,
type = mp4.name)

barret_ammo = Ammo(name='amunicja do karabinu barret82',
desc='amunicja do karabinu snajperskiego barre82',
bullets=10,
x=0,
y=0,
type=barret82.name)

dragunowammo = Ammo(name='magazynek do karabinu dragunow',
desc='amunicja do karabinu snajperskiego dragunow',
x=0,
y=0,
bullets=5,
type=dragunow.name)

macarowammo = Ammo(name='magazynek do macarowa',
desc='amunicja do pistoletu macarow',
bullets=20,
x=0,
y=0,
type=macarow.name)

akammo = Ammo(name='magazynek do ak47',
desc='amunicja do karabinu ak47',
bullets=40,
x=0,
y=0,
type=ak47.name)

pp19ammo = Ammo(name = 'amunicja do pp19',
x = 10,
y = 10,
desc = 'amunicja do pistoletu maszynowego pp19 bizon',
bullets = 64,
type = pp19.name)
