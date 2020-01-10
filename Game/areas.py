import copy
from random import randint
from . import guns, sounds, mobs
from .classes import Location, Area, Exit, SpecialObject

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
granatnik.spare_ammunition = 5

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


"""misja pierwsza - rozpoznanie, fragment miasta"""
skrzynka = SpecialObject(name = 'skrzynka',
x = 5,
y = 0)
macarow = guns.macarow
macarammo = guns.macarowammo
beretammo = guns.parabellum
ak = guns.ak47
akammo = guns.akammo
beretammo.x, beretammo.y = 10, 10
macarow.x, macarow.y = 10, 10
ak.x, ak.y = 10, 10
akammo.x, akammo.y = 10, 10
macarow.spare_ammunition = 3
ak.spare_ammunition = 3
gang = copy.deepcopy(mobs.gangus)
terrorysta = copy.deepcopy(mobs.terrorysta)
jihadysta = copy.deepcopy(mobs.jihadysta)
jihadysta.special = True
misja1_pokoj1 = Area(name='zagracony pokoj',
desc = 'szmaty, graty, zepsuta bron, luski po nabojach - no coz, terrorysci nie potrafia dbac o porzadek, ale moze cos jest tu ciekawego',
max_x = 10,
max_y = 15,
x = 25,
y = 25,
object = [],
exits = [],
npcs = [copy.deepcopy(gang)])
misja1_pokoj2 = Area(name = 'maly pokoj',
desc = 'maly pokoj, sadzac po wystroju mieszka tu tylko jedna osoba',
max_x = 10,
max_y = 5,
x = 10,
y = 10,
npcs = [copy.deepcopy(jihadysta)],
exits = [],
object = [skrzynka])
misja1_pokoj3 = Area(name='pokoj',
desc = 'pokoj w siedzibie terrorystow, brud smrud - nic ciekawego',
max_x = 15,
max_y = 10,
x = 5,
y = 5,
npcs = [copy.deepcopy(gang), copy.deepcopy(gang)],
object = [copy.deepcopy(macarammo), copy.deepcopy(akammo)])
misja1_siedzibagangu = Area(name='komisariat policji',
desc = 'posterunek policji przerobiony na siedzibe lokalnego gangu wspolpracujacego z terrorystami',
max_x = 50,
max_y = 50,
x = 0,
y = 30,
npcs = [copy.deepcopy(terrorysta), copy.deepcopy(terrorysta), copy.deepcopy(gang)],
object = [copy.deepcopy(beretammo)],
exits = [misja1_pokoj1, misja1_pokoj2, misja1_pokoj3])
misja1_budynek7 = Area(name='budynek przy placu',
desc = 'obszerny budynek, specjalnie powiekszony przez zburzenie scian, pewnie terrorysci odprawiali tutaj swoje modly',
x = 30,
y = 30,
max_x = 40,
max_y = 45,
npcs = [copy.deepcopy(gang)],
object = [copy.deepcopy(akammo), copy.deepcopy(akammo), copy.deepcopy(akammo)])

misja1_budynek6 = Area(name='ruiny budynku',
desc = 'budynek zostal prawie doszczetnie zniszczony, zapewne przez bombardowanie, albo po prostu nie spodobal sie tutejszym gangom',
max_x = 20,
max_y = 20,
x = 30,
y = 0,
object = [copy.deepcopy(macarammo)],
npcs = [copy.deepcopy(gang), copy.deepcopy(terrorysta)])

misja1_plac = Area(name='plac zjednoczonej europy',
desc = 'niegdys najpiekniejszy plac w srodkowo zachodniej europie, teraz jest ruina - dowodem na to jak szkodliwy dla swiata jest terroryzm',
max_x=100,
max_y = 100,
x = 0,
y = 100,
object = [],
npcs = [copy.deepcopy(gang), copy.deepcopy(gang), copy.deepcopy(gang), copy.deepcopy(terrorysta), copy.deepcopy(terrorysta)],
exits = [misja1_budynek7, misja1_budynek6, misja1_siedzibagangu])
misja1_budynek5 = Area(name='maly budynek',
desc = 'calkiem nienaruszony budynek mieszkalny, wyjatkowo posprzatany',
x = 5,
y = 20,
max_x = 20,
max_y = 20,
object = [copy.deepcopy(akammo)],
npcs = [copy.deepcopy(gang)])
misja1_budynek4 = Area(name='niski budynek',
desc = 'tutaj chyba znajdowala sie skladnica broni',
x = 10,
y = 30,
max_x = 20,
max_y = 20,
object = [copy.deepcopy(akammo), copy.deepcopy(akammo), copy.deepcopy(akammo), copy.deepcopy(macarammo), copy.deepcopy(macarammo)],
npcs = [copy.deepcopy(terrorysta)])

misja1_ulicanaplac = Area(name = 'Ulica prowadzaca na plac europejski',
desc = 'glowna ulica prowadzaca na plac',
x = 0,
y = 150,
max_x = 30,
max_y = 100,
object = [],
npcs = [copy.deepcopy(gang), copy.deepcopy(gang), copy.deepcopy(gang), copy.deepcopy(terrorysta)],
exits = [misja1_budynek4, misja1_budynek5, misja1_plac])

misja1_budynek3 = Area(name = 'maly magazyn',
desc = 'znajdujesz sie w przestronnym budynku ktore pewnie kiedys bylo magazynem',
max_x = 50,
max_y = 50,
x = 10,
y = 30,
object = [copy.deepcopy(beretammo)],
npcs = [])

misja1_budynek2 = Area(name='murowany dom',
desc = 'dom mieszkalny, kiedys pewnie mieszkalo tutaj kilka rodzin, teraz w tych ruinach pomiescic sie moze zaledwie druzyna',
x = 10,
y = 20,
max_x = 40,
max_y = 45,
object = [copy.deepcopy(ak)],
npcs = [copy.deepcopy(gang)])

misja1_budynek1 = Area(name='posterunek',
desc = 'posterunek terrorystow na glownej drodze do miasta, po architekturze wydaje ci sie, ze jest to przerobiony dom jednorodzinny - jak nisko potrafi upasc cywilizacja',
x = 10,
y = 10,
max_x = 40,
max_y = 45,
object = [copy.deepcopy(macarow)],
npcs = [copy.deepcopy(gang), copy.deepcopy(gang)])

misja1_drogadomiasta = Area(name = 'droga prowadzaca do miasta',
desc = 'znajdujesz sie na drodze prowadzaca do czesci miasta przejetego przez gangi i terrorystow, spogladasz wokolo na ruiny - niemych swiadkow licznych potyczek, odbywajacych sie w tym miescie, po bokach jest kilka budynkow, pewnie kryja sie w nich terrorysci',
max_x = 35,
max_y = 150,
x = 0,
y = 0,
object = [],
npcs = [copy.deepcopy(gang), copy.deepcopy(gang)],
exits = [misja1_budynek1, misja1_budynek2, misja1_budynek3, misja1_ulicanaplac])

"""misja 2 - szpital, bomby"""
bomba = SpecialObject(name='bomba',
x = 25,
y = 25)
dragunow = barret
dragunow.spare_ammunition = 15
pp = guns.pp19
pp.spare_ammunition = 15
medpack = guns.medpackammo
dragammo = guns.dragunowammo
ppammo = guns.pp19ammo

gang2 = gang
terrorysta2 = terrorysta
saper = mobs.soldier
saper.name = 'saper'
saper.hp = 1000
saper.x, saper.y = 25, 25
gang2.x, gang2.y = randint(0, 50), randint(0, 50)
terrorysta.x, terrorysta.y = randint(0, 50), randint(0, 50)

NazPok = {1:'pokoj1', 2:'pokoj2', 3:'pokoj3', 4:'pokoj4', 5:'pokoj5', 6:'pokoj6', 7:'pokoj7', 8:'pokoj8', 9:'pokoj9', 10:'pokoj10'}
pok10_pietro3 = Area(name=NazPok[10],
desc = 'pokoj',
x = 0,
y = 100,
object = [copy.deepcopy(medpack), copy.deepcopy(akammo)],
npcs = [copy.deepcopy(terrorysta2), copy.deepcopy(gang2), copy.deepcopy(terrorysta2)],
exits=[])
pok09_pietro3 = Area(name=NazPok[9],
desc = 'pokoj',
x = 0,
y = 90,
object = [copy.deepcopy(ppammo)],
npcs = [copy.deepcopy(terrorysta2), copy.deepcopy(gang2), copy.deepcopy(terrorysta2)],
exits=[])
pok08_pietro3 = Area(name=NazPok[8],
desc = 'pokoj',
x = 0,
y = 80,
object = [],
npcs = [copy.deepcopy(terrorysta2), copy.deepcopy(terrorysta2)],
exits = [])
pok07_pietro3 = Area(name=NazPok[7],
desc = '',
x = 0,
y = 70,
object = [copy.deepcopy(medpack)],
npcs = [copy.deepcopy(terrorysta2), copy.deepcopy(terrorysta2)],
exits = [])
pok06_pietro3 = Area(name = NazPok[6],
desc = '',
x = 0,
y = 60,
object = [],
npcs = [copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2)],
exits = [])
pok05_pietro3 = Area(name = NazPok[5],
desc = '',
x = 0,
y = 50,
object = [copy.deepcopy(bomba), copy.deepcopy(medpack)],
npcs = [copy.deepcopy(saper)],
exits = [])
pok04_pietro3 = Area(name = NazPok[4],
desc = 'pokoj',
x = 0,
y = 40,
object = [copy.deepcopy(akammo)],
npcs = [copy.deepcopy(terrorysta2), copy.deepcopy(gang2)],
exits = [])
pok03_pietro3 = Area(name = NazPok[3],
desc = '',
x = 0,
y = 30,
object = [copy.deepcopy(medpack)],
npcs = [],
exits = [])
pok02_pietro3 = Area(name = NazPok[2],
desc = 'pokoj',
x = 0,
y = 20,
object = [copy.deepcopy(medpack), copy.deepcopy(ppammo), copy.deepcopy(ppammo), copy.deepcopy(akammo), copy.deepcopy(akammo),],
npcs = [],
exits= [])
pok01_pietro3 = Area(name = NazPok[1],
desc = 'pokoj',
x = 0,
y = 10,
object = [copy.deepcopy(medpack), copy.deepcopy(medpack), copy.deepcopy(medpack)],
npcs = [],
exits = [])

pietro3 = Area(name = 'pietro trzecie',
desc = 'idziesz po trzecim pietrze tego wielkiego szpitala',
max_x = 100,
max_y = 100,
x = 0,
y = 60,
object = [],
npcs = [copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(terrorysta2)],
exits = [pok10_pietro3, pok09_pietro3, pok08_pietro3, pok07_pietro3, pok06_pietro3, pok05_pietro3, pok04_pietro3, pok03_pietro3, pok02_pietro3, pok01_pietro3])

pok10_pietro2 = Area(name=NazPok[10],
desc = 'pokoj',
x = 0,
y = 100,
object = [copy.deepcopy(bomba), copy.deepcopy(granat), copy.deepcopy(granat), copy.deepcopy(granat)],
npcs = [copy.deepcopy(saper)],
exits=[])
pok09_pietro2 = Area(name=NazPok[9],
desc = 'pokoj',
x = 0,
y = 90,
object = [copy.deepcopy(ppammo)],
npcs = [copy.deepcopy(gang2)],
exits=[])
pok08_pietro2 = Area(name=NazPok[8],
desc = 'pokoj',
x = 0,
y = 80,
object = [copy.deepcopy(akammo)],
npcs = [copy.deepcopy(gang2), copy.deepcopy(gang2)],
exits = [])
pok07_pietro2 = Area(name=NazPok[7],
desc = '',
x = 0,
y = 70,
object = [],
npcs = [copy.deepcopy(gang2)],
exits = [])
pok06_pietro2 = Area(name = NazPok[6],
desc = '',
x = 0,
y = 60,
object = [],
npcs = [copy.deepcopy(gang2), copy.deepcopy(terrorysta2)],
exits = [])
pok05_pietro2 = Area(name = NazPok[5],
desc = '',
x = 0,
y = 50,
object = [],
npcs = [],
exits = [])
pok04_pietro2 = Area(name = NazPok[4],
desc = 'pokoj',
x = 0,
y = 40,
object = [copy.deepcopy(medpack), copy.deepcopy(medpack)],
npcs = [copy.deepcopy(terrorysta2)],
exits = [])
pok03_pietro2 = Area(name = NazPok[3],
desc = '',
x = 0,
y = 30,
object = [],
npcs = [copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(terrorysta2)],
exits = [])
pok02_pietro2 = Area(name = NazPok[2],
desc = 'pokoj',
x = 0,
y = 20,
object = [copy.deepcopy(dragammo), copy.deepcopy(ppammo), copy.deepcopy(akammo), copy.deepcopy(ppammo), copy.deepcopy(medpack)],
npcs = [],
exits= [])
pok01_pietro2 = Area(name = NazPok[1],
desc = 'pokoj',
x = 0,
y = 10,
object = [copy.deepcopy(medpack), copy.deepcopy(medpack)],
npcs = [],
exits = [])

pietro2 = Area(name = 'drugie pietro szpitala',
desc = 'to jest drugie pietro tego ogromnego szpitala',
max_x = 100,
max_y = 100,
x = 0,
y = 40,
object = [],
npcs = [copy.deepcopy(gang2), copy.deepcopy(terrorysta2),copy.deepcopy(gang2), copy.deepcopy(terrorysta2),copy.deepcopy(gang2), copy.deepcopy(terrorysta2),copy.deepcopy(gang2), copy.deepcopy(terrorysta2),copy.deepcopy(gang2), copy.deepcopy(terrorysta2)],
exits = [pok10_pietro2, pok09_pietro2, pok08_pietro2, pok07_pietro2, pok06_pietro2, pok05_pietro2, pok04_pietro2, pok03_pietro2, pok02_pietro2, pok01_pietro2])

pok10_pietro1 = Area(name=NazPok[10],
desc = 'pokoj',
x = 0,
y = 100,
object = [copy.deepcopy(granat), copy.deepcopy(granat)],
npcs = [copy.deepcopy(gang2)],
exits=[])
pok09_pietro1 = Area(name=NazPok[9],
desc = 'pokoj',
x = 0,
y = 90,
object = [copy.deepcopy(ppammo), copy.deepcopy(ppammo)],
npcs = [],
exits=[])
pok08_pietro1 = Area(name=NazPok[8],
desc = 'pokoj',
x = 0,
y = 80,
object = [],
npcs = [copy.deepcopy(terrorysta2), copy.deepcopy(terrorysta2), copy.deepcopy(terrorysta2)],
exits = [])
pok07_pietro1 = Area(name=NazPok[7],
desc = '',
x = 0,
y = 70,
object = [copy.deepcopy(akammo), copy.deepcopy(akammo), copy.deepcopy(akammo)],
npcs = [copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2)],
exits = [])
pok06_pietro1 = Area(name = NazPok[6],
desc = '',
x = 0,
y = 60,
object = [],
npcs = [copy.deepcopy(terrorysta2), copy.deepcopy(terrorysta2), copy.deepcopy(terrorysta2), copy.deepcopy(terrorysta2)],
exits = [])
pok05_pietro1 = Area(name = NazPok[5],
desc = '',
x = 0,
y = 50,
object = [],
npcs = [copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2)],
exits = [])
pok04_pietro1 = Area(name = NazPok[4],
desc = 'pokoj',
x = 0,
y = 40,
object = [copy.deepcopy(medpack)],
npcs = [copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(terrorysta2)],
exits = [])
pok03_pietro1 = Area(name = NazPok[3],
desc = '',
x = 0,
y = 30,
object = [copy.deepcopy(ppammo), copy.deepcopy(ppammo)],
npcs = [copy.deepcopy(gang2)],
exits = [])
pok02_pietro1 = Area(name = NazPok[2],
desc = 'pokoj',
x = 0,
y = 20,
object = [copy.deepcopy(bomba)],
npcs = [copy.deepcopy(saper)],
exits= [])
pok01_pietro1 = Area(name = NazPok[1],
desc = 'pokoj',
x = 0,
y = 10,
object = [copy.deepcopy(medpack), copy.deepcopy(medpack), copy.deepcopy(medpack)],
npcs = [copy.deepcopy(terrorysta2)],
exits = [])

pietro1 = Area(name = 'pietro pierwsze szpitala',
desc = 'to jest pierwsze pietro tego ogromnego gmaszyska',
max_x = 100,
max_y = 100,
x = 0,
y = 20,
object = [],
npcs = [copy.deepcopy(gang2), copy.deepcopy(terrorysta2),copy.deepcopy(gang2), copy.deepcopy(terrorysta2),copy.deepcopy(gang2), copy.deepcopy(terrorysta2),copy.deepcopy(gang2), copy.deepcopy(terrorysta2),copy.deepcopy(gang2), copy.deepcopy(terrorysta2)],
exits = [pok10_pietro1, pok09_pietro1, pok08_pietro1, pok07_pietro1, pok06_pietro1, pok05_pietro1, pok04_pietro1, pok03_pietro1, pok02_pietro1, pok01_pietro1])

schody = Area(name = 'schody',
desc = 'schody na pietra szpitala',
x = 0,
y = 50,
object = [copy.deepcopy(medpack)],
npcs = [copy.deepcopy(gang2), copy.deepcopy(terrorysta2)],
exits = [pietro1, pietro2, pietro3])

stolowka = Area(name = 'Stolowka',
desc = 'stolowka szpitalna',
x = 50,
y = 0,
object = [copy.deepcopy(bomba), copy.deepcopy(akammo), copy.deepcopy(medpack), copy.deepcopy(medpack), copy.deepcopy(ppammo), copy.deepcopy(dragammo), copy.deepcopy(granatnik)],
npcs = [copy.deepcopy(saper)],
exits = [])
szpital = Area(name = 'szpital',
max_x = 110,
max_y = 110,
x = 0,
y = 50,
object = [],
npcs = [copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(gang2), copy.deepcopy(terrorysta2)],
exits = [stolowka, schody])
misja2_ulica_start = Area(name = 'ulica przed gmachem szpitala',
desc = 'szeroka ulica przed ogromnym szpitalem miejskim',
x = 0,
y = 0,
object = [copy.deepcopy(pp), copy.deepcopy(dragunow), copy.deepcopy(ak), copy.deepcopy(akammo), copy.deepcopy(ppammo), copy.deepcopy(ppammo), copy.deepcopy(ppammo), copy.deepcopy(medpack), copy.deepcopy(medpack), copy.deepcopy(medpack)],
npcs = [],
exits = [szpital])


