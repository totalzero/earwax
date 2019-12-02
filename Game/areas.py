import copy
from random import randint
from . import guns, sounds, mobs
from .classes import Location, Area, Exit

macarow = copy.deepcopy(guns.macarow)
macarow.x, macarow.y = 10, 10
ammo_macarow = copy.deepcopy(guns.macarowammo)
ammo_macarow.x, ammo_macarow.y = 10, 10
ak = copy.deepcopy(guns.ak47)
akammo = copy.deepcopy(guns.akammo)
akammo.x, akammo.y = 10, 10
ak.x, ak.y = 10, 10
granatnik = copy.deepcopy(guns.grenade)
granat = copy.deepcopy(guns.granatammo)
granatnik.x, granatnik.y = 10, 10
granat.x, granat.y = 10, 10

barret = copy.deepcopy(guns.dragunow)
barret.x, barret.y = 10, 10
tarcza_win = copy.deepcopy(mobs.tarcza)
tarcza_win.special = True
tarcza_win.x, tarcza_win.y = 100, 100
tarcza_win.name = 'ogromna tarcza'
tarcza_win.hp = 50
tarczasnajper1 = copy.deepcopy(mobs.tarcza)
tarczasnajper2 = copy.deepcopy(mobs.tarcza)
tarczasnajper3 = copy.deepcopy(mobs.tarcza)
tarczasnajper1.x, tarczasnajper1.y = 15, 100
tarczasnajper2.x, tarczasnajper2.y = 5, 300
tarczasnajper3.x, tarczasnajper3.y = 0, 950


tarcza1 = copy.deepcopy(mobs.tarcza)
tarcza2 = copy.deepcopy(mobs.tarcza)
tarcza3 = copy.deepcopy(mobs.tarcza)
tarcza1.x, tarcza1.y = 15, 15
tarcza2.x, tarcza2.y = 20, 20
tarcza3.x, tarcza3.y = 22, 22


trening_snajper = Area(name='trening uzywania broni snajperskiej',
desc = 'tutaj nauczysz sie obslugi karabinu snajperskiego. Jak ci pewnie wiadomo jako strzelec wyborowy masz dostep do wszystkich celow na mapie, nie zalerznie w jakiej odleglosci od ciebie sie one znajduja, aby jednak moc celowac musisz wcisnac klawisz spacja - aby uaktywnic zoom, nastepnie klawiszem q mozesz sie przelaczac miedzy celami',
x = 0,
y = 25,
max_x=1000,
max_y = 1000,
sound = sounds.doors[1],
object = [barret],
npcs = [tarczasnajper1, tarczasnajper2, tarczasnajper3])

trening_granat = Area(name = 'trening obslugi granatow',
desc='Tutaj nauczysz sie jak obslugiwac granaty w tej grze. wyglada to troche inaczej niz normalnie, po pierwsze - musisz miec granatnik, naszczescie jeden lezy tutaj gdzies niedaleko, po drugie musisz miec granaty do granatnika - zbierz wszystko z ziemi i idz na cele. Granat ma dzialanie obszarowe, to znaczy zabija wszystkich przeciwnikow ktorzy sa w twoim zasiegu, wyproboj go.',
x = 0,
y = 20,
max_x = 25,
max_y = 25,
sound = sounds.doors[3],
object = [granatnik, granat, granat],
npcs = [copy.deepcopy(tarcza2), copy.deepcopy(tarcza2), copy.deepcopy(tarcza2)])

trening_karabin = Area(name='trening strzelania z karabinu',
desc = 'tutaj poczujesz roznice miedzy pistoletem a karabinem, jezeli oczywiscie ukonczyles juz trening strzelania z pistoletu, jezeli nie to przypomne ci, klawisz c-bron i amunicja, klawisz n - twoje cele do zestrzelenia, milej zabawy.',
x = 0,
y = 15,
max_x = 25,
max_y = 25,
sound = sounds.doors[2],
npcs = [copy.deepcopy(tarcza1), copy.deepcopy(tarcza2), copy.deepcopy(tarcza3)],
object = [ak, akammo, akammo, akammo])

trening_pistolet = Area(name='trening strzelania z pistoletu',
desc='witaj na treningu strzelania, najpierw zaczniesz oczywiscie od pistoletu, jezeli sie nie zorientowales, to wcisnij c - uslyszysz wsp pistoletu, ktory ozesz zebrac, idz na ta pozycje i zbierz go razem z amunicja do niego. Aby cos zebrac wcisnij lshift, aby ustawic sie na przedmiotach na ziemi, a nastepnie litera f wybierz co chcesz zabrac.',
x=0,
y=5,
max_x=25,
max_y=25,
sound = sounds.doors[1],
npcs=[tarcza1, tarcza2, tarcza3],
object = [macarow, ammo_macarow, ammo_macarow, ammo_macarow])

trening = Area(name='glowny budynek treningowy',
desc = 'Witaj w grze, zadaniem tej misji jest abys przecwiczyl sobie klawisze i granie - pomoze ci to w wypelnianiu pozostalych misji ktore na ciebie czekaja, najpierw jednak zapoznaj sie z klawiszem Z - jest to twoja obecna pozycja na mapie, pod klawiszem E masz wszystkie budynki do ktorych mozesz wejsc, pod klawiszem c - bronie i wyposarzenie, a klawisz n powie ci jacy przeciwnicy sa w obecnej lokacji. klawisze strzalek sprawia, ze sie poruszysz, wiec moze przejdz do najblizej ciebie polozonego budynkowi w ktorym odbedziesz nastepny trening. jak zakonczysz juz wszystkie treningi, albo po prostu jakbys chcial zaliczyc odrazu to zadanie, to idz i zastrzel tarcze na koncu tego pokoju.',
max_x=100,
max_y=100,
exits=[trening_pistolet, trening_karabin, trening_granat, trening_snajper],
npcs =[tarcza_win],
sound = sounds.doors[1])


