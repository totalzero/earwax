from . import guns, sounds, mobs
from .classes import Location, Area


posterunek = Location(name='posterunek',
desc='posterunek zolnierzy stacjonujacych w bazie',
x=15,
y=5)
posterunek.adderobj(guns.macarow, 1)
posterunek.adderobj(guns.macarowammo, 5)
posterunek.addernpc(mobs.soldier, 5)


koszary = Location(name='koszary wojskowe',
desc='podluzny budynek w ktorym znajduja sie koszary',
x=50,
y=50)
koszary.adderobj(guns.ak47, 1)
koszary.adderobj(guns.akammo, 5)
koszary.addernpc(mobs.soldier, 15)


baza1 = Area(name = 'wojskowa baza',
desc = 'ogromna wojskowa baza ktora musisz zniszczyc',
object = [posterunek, koszary],
max_x = 1000,
max_y = 1000)
baza1.addernpc(mobs.soldier, 50)