import pyglet
import Tolk
from pyglet.window import key
from random import randint
from collections import Counter as counter

pyglet.resource.path = ['/Resources', '../Resources', 'Resources']
pyglet.resource.reindex()



Tolk.load()
def speak(args):
#funkcja obslugujaca mowe - speak(argument) i wymawia to co jest w argument
    Tolk.output(str(args))

class Player:
    """glowna gracza definiujaca playera, zawiera obsluge ekwipunku, pozycji (x y), hp, exp, cele(aim i main aim), oraz obsluge dzwieku krokow"""
    def __init__(self, x=0, y=0, step=[], eq = [], hp=500, aims=[], main_aim=None, current_weapon=None, ammo=[]):
        self.x = 0
        self.y = 0
        self.step = step
        self.eq = eq
        self.ammo = ammo
        self.hp = hp
        self.aims = aims
        self.main_aim = main_aim
        self.current_weapon = current_weapon

    def add_weapon(self, weapon):
        """metoda dodajaca itemek do ekwipunku, obslugiwana z metody update w definicji klawisza F"""
        self.eq.append(weapon)
        weapon.get_sound.play()

    def add_ammo(self, ammo):
        getammo = pyglet.resource.media('getammo.wav', streaming=False)
        self.ammo.append(ammo)
        getammo.play()

class Area:
    def __init__(self, desc = '', max_x=100, max_y=100, player_position_x = 0, player_position_y = 0, name = None, object=[], npcs=[]):
        self.max_x = max_x
        self.max_y = max_y
        self.player_position_x = player_position_x
        self.player_position_y = player_position_y
        self.name = name
        self.desc = desc
        self.object = object
        self.npcs = npcs


class Doors:
    def __init__(self, desc='', name = 'door', x=0, y=0, next_area = None, sound=None):
        self.next_area = next_area
        self.x = x
        self.y = y
        self.name = name
        self.sound = sound

class Weapon:
    def __init__(self, name, desc='', missiles = 20, is_reload=True, x=0, y=0, damage=100, get_sound=None, fire_sound=None, reload_sound=None, empty_sound=None, aims_at=None, ammotype=None):
        self.name = name
        self.ammotype = ammotype
        self.desc = desc
        self.missiles = missiles
        self.is_reload = is_reload
        self.damage = damage
        self.get_sound = get_sound
        self.fire_sound = fire_sound
        self.reload_sound = reload_sound
        self.empty_sound = empty_sound
        self.x = x
        self.y = y
        self.aims_at = aims_at

    def fire(self, player):
        miss = bool(randint(0, 1))
        if self.missiles >0:
            self.fire_sound.play()
            self.missiles -=1
        else:
            self.empty_sound.play()
        try:
            if (player.main_aim == None) or (miss == True) or (self.missiles <=0):
                pass
            else:
                player.main_aim.hp -= randint(1, self.damage)
                player.main_aim.injured[randint(0, 4)].play()
        except:
            pass

    def mode(self, player, area, modespace):
        pass

class Ammo:
    pass

class Parabellum(Weapon, Ammo):
    def __init__(self, name='amunicja 9mm parabellum', desc='amunicja 9mm parabellum do pistoletow i pistoletow maszynowych', x=0, y=0):
        self.name = name
        self.desc = desc
        self.ammunition = 20
        self.x = x
        self.y = y



    def fire(self, player):
        pass

class AK_ammo(Weapon, Ammo):
    def __init__(self):
        self.name = 'magazynek do karabinow i karabinkow AK'
        self.desc = 'amunicja do broni rodziny AK'
        self.ammunition = 50

class Pistols(Weapon):
    pass

class Carabines(Weapon):
    pass

class Knifes(Weapon):
    def fire(self, player):
        miss = bool(randint(0, 1))
        self.fire_sound.play()
        try:
            if (player.main_aim == None) or (miss == True) or (self.missiles <=0):
                pass
            else:
                player.main_aim.hp -= randint(1, self.damage)
                player.main_aim.injured[randint(0, 4)].play()
        except:
            pass

class Medpack(Weapon):
    def fire(self, player):
        if self in player.eq:
            self.fire.play()
            player.hp +=500
            player.eq.remove(self)
        else:
            pass

class Grenades(Weapon):
    def fire(self, player):
        self.fire_sound.play()
        player.eq.remove(self)
        for i in player.aims:
            i.hp -= i.hp


class Snajper(Weapon):
    def mode(self, player, area, modespace):
        zoomin = pyglet.resource.media('weapons/zoomin.wav', streaming=False)
        zoomout = pyglet.resource.media('weapons/zoomout.wav', streaming=False)
        if modespace == True:
            zoomin.play()
            for i in area.npcs:
                if i in player.aims:
                    pass
                else:
                    player.aims.append(i)
        else:
            player.aims.clear()
            player.main_aim = None

class Npc:
    def __init__(self, desc='', aggresiv=False, walker=False, x=0, y=0, hp=100, name='',):
        self.npc_attacks = pyglet.resource.media('fire.wav', streaming=False)
        self.name = name
        self.desc = desc
        self.x = x
        self.y = y
        self.hp = hp
        self.aggresiv = aggresiv
        self.walker = walker
        self.injured =[pyglet.resource.media('npc/injured/1.wav', streaming=False), pyglet.resource.media('npc/injured/2.wav', streaming=False), pyglet.resource.media('npc/injured/3.wav', streaming=False), pyglet.resource.media('npc/injured/4.wav', streaming=False)]
        self.died =[pyglet.resource.media('npc/died/1.wav', streaming=False), pyglet.resource.media('npc/died/2.wav', streaming=False), pyglet.resource.media('npc/died/3.wav', streaming=False), pyglet.resource.media('npc/died/4.wav', streaming=False), pyglet.resource.media('npc/died/5.wav', streaming=False)]

    def update(self):
        """tutaj obslugiwane jest poruszanie sie, najpierw sprawdza czy pozycja npc nie jest mniejsza od 0, jezeli tak to rowna ja 0, nastepnie losuje czy ma sie poruszyc, jezeli tak to sprawdza czy atrybut walker jest prawdziwy, wtedy losuje o ile ma sie poruszyc, zakres od -2 do 2"""
        if self.x<0:
            self.x = 0

        if self.y <0:
            self.y = 0

        if bool(randint(0, 1))==True:
            if self.walker == True:
                self.x += randint(-5, 5)
                self.y += randint(-5, 5)

class Objects:
    def __init__(self):
        self.steps =[pyglet.resource.media('steps/glowny/1.wav', streaming=False), pyglet.resource.media('steps/glowny/2.wav', streaming=False), pyglet.resource.media('steps/glowny/3.wav', streaming=False), pyglet.resource.media('steps/glowny/4.wav', streaming=False), pyglet.resource.media('steps/glowny/5.wav', streaming=False), pyglet.resource.media('steps/glowny/6.wav', streaming=False), pyglet.resource.media('steps/glowny/7.wav', streaming=False), pyglet.resource.media('steps/glowny/8.wav', streaming=False)]

        self.parabellum_ammo = Parabellum(x=10, y=10)
        self.akammo = AK_ammo()

        self.drzwi_glowny = Doors(name='drzwi', desc='drzwi do glownego pokoju testowego', next_area='glowny', sound=pyglet.resource.media('doors/door3.wav', streaming=False))
        self.drzwi_korytarz = Doors(name='drzwi', desc='drzwi do korytarza', x=randint(0, 25), y=randint(0, 50), next_area='korytarz', sound=pyglet.resource.media('doors/door2.wav', streaming=False))

        self.pistol = Pistols(name='pistol', desc='podstawowa bron testowa', ammotype=self.parabellum_ammo, x=10, y=10, get_sound=pyglet.resource.media('weapons/pistol/GET_WEAPON.wav', streaming=False), aims_at=pyglet.resource.media('weapons/pistol/aims_at.wav', streaming=False), fire_sound=pyglet.resource.media('weapons/pistol/fire.wav', streaming=False), reload_sound=pyglet.resource.media('weapons/pistol/reload.wav', streaming=False), empty_sound=pyglet.resource.media('weapons/pistol/empty.wav', streaming=False))
        self.knife = Knifes(name='noz typu muela', desc='podstawowy noz testowy', damage=20, is_reload=False, fire_sound=pyglet.resource.media('weapons/knife/fire.wav', streaming=False), aims_at=pyglet.resource.media('weapons/knife/aims_at.wav', streaming=False))
        self.mg4 = Carabines(name='MG-4', damage=80, desc='karabin szturmowy mg4', missiles=100, fire_sound=pyglet.resource.media('weapons/mg4/fire.wav', streaming=False), empty_sound=pyglet.resource.media('weapons/mg4/empty.wav', streaming=False), reload_sound=pyglet.resource.media('weapons/mg4/reload.wav', streaming=False), get_sound=pyglet.resource.media('weapons/mg4/GET_WEAPON.wav', streaming=False), aims_at=pyglet.resource.media('weapons/mg4/aims_at.wav', streaming=False))
        self.ak47 = Carabines(name='karabin szturmowy ak47', desc='karabin szturmowy ak47', ammotype=self.akammo, fire_sound=pyglet.resource.media('weapons/ak47/fire.wav', streaming=False), empty_sound=pyglet.resource.media('weapons/ak47/empty.wav', streaming=False), reload_sound=pyglet.resource.media('weapons/ak47/reload.wav', streaming=False), get_sound=pyglet.resource.media('weapons/ak47/GET_WEAPON.wav', streaming=False), aims_at=pyglet.resource.media('weapons/ak47/aims_at.wav', streaming=False) )
        self.grenade = Grenades(x=10, y=10, name='granat', desc='po prostu granat, ma zawleczke i zapalnik, lyzke nawet', fire_sound=pyglet.resource.media('weapons/grenade/fire.wav', streaming=False), get_sound=pyglet.resource.media('weapons/grenade/GET_WEAPON.wav', streaming=False), aims_at=pyglet.resource.media('weapons/grenade/aims_at.wav', streaming=False))

        self.examplenpc = Npc(name='examplenpc', desc='przykladowy npc w grze', x=randint(25, 50), y=randint(15, 100), walker=True)
        self.examplenpc2 = Npc(name='examplenpc2', desc='przykladowy przeciwnik w grze', x=randint(0, 50), y=randint(0, 50), walker=True, aggresiv=True)


class Mapa:
    def __init__(self, objects=Objects()):
        self.objects = objects
        self.mapa = {'glowny':Area(name='glowny', desc='glowny pokoj testowy', object=[self.objects.drzwi_korytarz, self.objects.pistol, self.objects.parabellum_ammo], npcs=[self.objects.examplenpc, self.objects.examplenpc2]), 'korytarz':Area(max_x=20, max_y=20, name='korytarz', desc='korytarz', object=[self.objects.drzwi_glowny, self.objects.grenade, self.objects.grenade], npcs=[self.objects.examplenpc, self.objects.examplenpc, self.objects.examplenpc])}






class Gra:
    """cala logika gry, zawiera obiekty takie jak player, area, map, keys - ktore to sa instancjami klas o tej samej nazwie - obserwuje i nadzoruje wszystkie obiekty w grze, okresla ich wzajemne relacje, odpowiada za wszystko"""
    def __init__(self, keys=dict(LEFT=False, UP=False, DOWN=False, RIGHT=False), mapa = Mapa(), obj=Objects()):
        self.obj = obj
        self.mapa = mapa.mapa
        self.player = Player(step=self.obj.steps, eq=[self.obj.knife, self.obj.grenade], ammo=[self.obj.parabellum_ammo])
        self.area = self.mapa['glowny']
        self.keys = keys
        stepping = 0
        self.stepping = stepping
        alert = pyglet.resource.media('cel.wav', streaming=False)
        self.alert = alert
        celownik = 0
        self.celownik = celownik
        self.modespace = False
        self.tab_focus = counter(self.player.eq)
        self.tab_iter = iter(self.tab_focus)
        self.tab_sound = pyglet.resource.media('weapons/unduck.wav', streaming=False)
        self.itemcounter = []

    def itemadder(self, item):
        itemalert = pyglet.resource.media('itemalert.wav', streaming=False)
        itemalert.play()
        self.itemcounter.append(item)


    def open_door(self, name_loc):
        self.area = self.mapa[name_loc]

    def attack(self, enemy, miss):
        try:
            if self.player.main_aim == None or miss == True:
                pass
            else:
                enemy.hp -= randint(0, self.player.current_weapon.damage)
                enemy.injured[randint(0, 4)].play()
            if enemy.hp <=0:
                enemy.died[randint(0, 4)].play()
                self.area.npcs.remove(enemy)
                self.player.main_aim = None
                self.player.aims.remove(enemy)
        except:
            pass

    def npc_attacks(self, npc):
        a = bool(randint(0, 1))
        b = bool(randint(0, 1))
        c = bool(randint(0, 1))
        if a&b== True:
            npc.npc_attacks.play()
            if c==True:
                self.player.hp -=randint(0, 25)
                speak(('jestes pod ostrzalem'))

    def update(self):
        if self.stepping >= (len(self.player.step)-1):
            self.stepping = 0

        if self.celownik >= (len(self.player.aims)):
            self.celownik = 0

        if self.keys[key.SPACE]:
            if self.modespace == False:
                self.modespace = True
                self.player.current_weapon.mode(self.player, self.area, self.modespace)
            else:
                self.modespace = False
                self.player.current_weapon.mode(self.player, self.area, self.modespace)

        if self.keys[key.H]:
            speak(('hp', str(self.player.hp)))
            if len(self.player.aims) > 0:
                for i in self.player.aims:
                    speak((str(i.name, i.hp)))
            else:
                pass

        if self.keys[key.A]:
            try:
                amunicja = counter(self.player.ammo)
                speak(('posiadasz w magazynku', str(self.player.current_weapon.missiles), 'pociskow'))
                speak(('do tego posiadasz w ekwipunku:'))
                for i in amunicja:
                    speak((str(i.name), str(amunicja[i])))
            except:
                speak(('brak amunicji do tej broni'))
        if self.keys[key.R]:
            sprawdzam = False
            if self.player.current_weapon.is_reload == True:
                for i in self.player.ammo:
                    if type(self.player.current_weapon.ammotype) == type(i):
                        sprawdzam = True
                        self.player.current_weapon.missiles += i.ammunition
                        self.player.ammo.remove(i)
                        break
                if sprawdzam == True:
                    self.player.current_weapon.reload_sound.play()
                else:
                    speak(('nie posiadasz amunicji do tej broni'))
            else:
                speak(('ta bron nie posiada pociskow'))

        if self.keys[key.D]:
            for i in self.area.object + self.area.npcs:
                if (i.x == self.player.x)& (i.y == self.player.y):
                    speak((str(i.desc)))
                else:
                    speak((str(self.area.desc)))

        if self.keys[key.LCTRL]:
#            try:
                self.player.current_weapon.fire(self.player)
                self.tab_focus = counter(self.player.eq)
                self.tab_iter = iter(self.tab_focus)
#            except:
#                pass

        if self.keys[key.TAB]:
            try:
                self.player.current_weapon = next(self.tab_iter)
                speak(self.player.current_weapon.name)
                self.tab_sound.play()
            except StopIteration:
                self.tab_iter = iter(self.tab_focus)

        if self.keys[key.Q]:
            try:
                self.player.main_aim = self.player.aims[self.celownik]
                self.celownik +=1
                speak(('celujesz w', str(self.player.main_aim.name)))
                self.player.current_weapon.aims_at.play()
            except:
                speak('brak celow')
                self.player.main_aim = None

        if self.keys[key.I]:
            for i in self.player.eq:
                speak((str(i.name)))

        if self.keys[key.F]:
            if len(self.itemcounter) > 0:
                for i in self.itemcounter:
                    if isinstance(i, Ammo)==True:
                        self.player.add_ammo(i)
                        self.area.object.remove(i)
                        self.itemcounter.remove(i)
                    elif isinstance(i, (Pistols, Carabines, Grenades, Medpack, Snajper))==True:
                        self.player.add_weapon(i)
                        self.area.object.remove(i)
                        self.itemcounter.remove(i)
            self.tab_focus = counter(self.player.eq)





        if self.keys[key.Z]:
            speak(('x', str(self.player.x), 'y', str(self.player.y)))

        if self.keys[key.N]:
            for i in self.area.npcs:
                speak((str(i.name),':', str(i.x), str(i.y)))

        if self.keys[key.C]:
            for i in self.area.object:
                speak((str(i.name), 'x:', str(i.x), 'y:', str(i.y)))

        if self.keys[key.O]:
            try:
                for x in self.area.object:
                    if (x.x == self.player.x) & (x.y == self.player.y):
                        x.sound.play()
                        self.open_door(x.next_area)
                        self.player.main_aim = None
                        self.player.aims.clear()
            except:
                speak(('to nie sa drzwi'))

        if self.keys[key.M]:
            speak(('jestes w', self.area.name, 'wymiary tego pomieszczenia to:', self.area.max_x, 'na', self.area.max_y), 'twoj glowny cel to:', str(self.player.main_aim.name))


        for i in self.area.npcs:
            x = abs(i.x - self.player.x)
            y = abs(i.y - self.player.y)
            if (x <= 5) & (y <=5):
                if i.walker == True:
                    self.alert.play()
                    self.player.aims.append(i)
                    i.walker = False
            else:
                i.walker = True
                if i in self.player.aims:
                    self.player.aims.remove(i)

        for x in self.area.npcs:
            if x.x > self.area.max_x:
                x.x = self.area.max_x
            if x.y > self.area.max_y:
                x.y = self.area.max_y

        for x in self.player.aims:
            if x.aggresiv == True:
                self.npc_attacks(x)
                if self.player.main_aim == None:
                    self.player.main_aim = x

        for x in self.area.npcs:
            #pentla sprawdzajaca stan hp i usuwajaca npc ktore sa umarle
            if x.hp <=0:
                x.died[randint(0, 4)].play()
                self.area.npcs.remove(x)
                self.player.aims.remove(x)
                if self.player.main_aim == x:
                    self.player.main_aim = None

        for i in self.area.object:
        #pentla dodajaca itemy do self.itemcounter
            x = abs(i.x - self.player.x)
            y = abs(i.y - self.player.y)
            if (x==0)&(y==0):
                if not i in self.itemcounter:
                    self.itemadder(i)
            if (x>3)&(y>3):
                if i in self.itemcounter:
                    self.itemcounter.remove(i)

    def moving(self):
        if self.keys[key.UP]:
            if self.player.y <= self.area.max_y:
                self.player.y +=1
                self.player.step[self.stepping].play()
                self.stepping +=1

        if self.keys[key.DOWN]:
            if self.player.x >=0:
                self.player.step[self.stepping].play()
                self.stepping +=1
                self.player.y -=1
                if self.player.y < 0:
                    self.player.y = 0

        if self.keys[key.LEFT]:
            if self.player.x >=0:
                self.player.x -=1
                self.player.step[self.stepping].play()
                self.stepping +=1
                if self.player.x <=0:
                    self.player.x = 0

        if self.keys[key.RIGHT]:
            if self.player.x <= self.area.max_x:
                self.player.x +=1
                self.player.step[self.stepping].play()
                self.stepping +=1


