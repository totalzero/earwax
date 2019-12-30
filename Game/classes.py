import pyglet
import Tolk
from pyglet.window import key
from random import randint
from collections import Counter as counter
from . import sounds



Tolk.load()
def speak(args):
#funkcja obslugujaca mowe - speak(argument) i wymawia to co jest w argument
    Tolk.output(str(args))

class Player:
    """glowna gracza definiujaca playera, zawiera obsluge ekwipunku, pozycji (x y), hp, exp, cele(aim i main aim), oraz obsluge dzwieku krokow"""
    def __init__(self, x=0, y=0, step=[], eq = [], hp=500, aims=[], main_aim=None, current_weapon=None, special=-1):
        self.special = special
        self.x = 0
        self.y = 0
        self.step = step
        self.eq = eq
        self.hp = hp
        self.aims = aims
        self.main_aim = main_aim
        self.current_weapon = current_weapon

    def add_weapon(self, weapon):
        """metoda dodajaca itemek do ekwipunku, obslugiwana z metody update w definicji klawisza F"""
        self.eq.append(weapon)
        weapon.get_sound.play()

class Area:
    def __init__(self, desc = '', max_x=100, max_y=100, name = None, object=[], npcs=[], exits=[], sound=sounds.doors[1], x=0, y=0):
        self.sound = sound
        self.x = x
        self.y = y
        self.exits = exits
        self.max_x = max_x
        self.max_y = max_y
        self.name = name
        self.desc = desc
        self.object = object
        self.npcs = npcs

    def update(self):
        for i in self.npcs:
            i.update()
            if i.x > self.max_x:
                i.x = self.max_x
            if i.y > self.max_y:
                i.y = self.max_y
            if i.life == False:
                self.npcs.remove(i)


class Location:
    def __init__(self, name='examplelocation', desc='this is a example location', x=10, y=10, object = [], npcs=[], exits=[]):
        self.name = name
        self.desc = desc
        self.x = x
        self.y = y
        self.object = object
        self.npcs = npcs
        self.max_x = 25
        self.max_y = 25
        self.exits = exits
        self.destroyed = False

    def update(self):
        for x in self.npcs:
            x.update()
            if x.life == False:
                self.npcs.remove(x)
            if x.x > self.max_x:
                x.x = self.max_x
            if x.y > self.max_y:
                x.y = self.max_y

class Exit:
    def __init__(self, name='examplexit', x=0, y=0,area=None, sound=None):
        self.name = name
        self.x = x
        self.y = y
        self.area = area
        self.sound = sound

class SpecialObject:
    def __init__(self, name = 'skrzynka', x=0, y=0, sound = sounds.specialobj):
        self.name = name
        self.x = x
        self.y = y
        self.sound = sound

class Weapon:
    def __init__(self, name, desc='', missiles = 20, is_reload=True, x=0, y=0, damage=100, get_sound=None, fire_sound=None, reload_sound=None, empty_sound=None, aims_at=None, spare_ammunition=0, maxbullets=20):
        self.name = name
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
        self.spare_ammunition = spare_ammunition
        self.maxbullets = maxbullets

    def add_ammo(self):
        getammo = sounds.getammo
        self.spare_ammunition +=1
        getammo.play()

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
                if player.main_aim.hp <=0:
                    player.main_aim.died[randint(0, 4)].play()
                    player.main_aim.life = False
                    player.aims.remove(player.main_aim)
                    player.main_aim = None
                    if player.main_aim.special == True:
                        player.special +=1
                    player.aims.remove(player.main_aim)
                    if len(player.aims) > 0:
                        player.main_aim = player.aims[0]
                    else:
                        player.main_aim = None
        except:
            pass

    def mode(self, player, area, modespace):
        pass

class Ammo:
    def __init__(self, x, y, name, desc, bullets, type=None):
        self.x = x
        self.y = y
        self.name = name
        self.desc = desc
        self.bullets = bullets
        self.type = type

class Pistols(Weapon):
    pass

class Carabines(Weapon):
    pass

class Knifes(Weapon):
    def fire(self, player):
        fire1 = pyglet.resource.media('weapons/knife/1.wav', streaming=False)
        miss = bool(randint(0, 1))
        if (player.main_aim == None) or (miss == True) or (self.missiles <=0):
            self.fire_sound.play()
        else:
            fire1.play()
            player.main_aim.hp -= randint(1, self.damage)
            player.main_aim.injured[randint(0, 4)].play()
            if player.main_aim.hp <=0:
                player.main_aim.life = False
                player.aims.remove(player.main_aim)
                if len(player.aims) > 0:
                    player.main_aim = player.aims[0]
                else:
                    player.main_aim = None
                if player.main_aim.special == True:
                    player.special +=1
                player.main_aim.died[randint(0, 4)].play()
                player.aims.remove(player.main_aim)
                player.main_aim = None

class Medpack(Weapon):
    def fire(self, player):
        if self.missiles >0:
            self.fire_sound.play()
            player.hp = 5000
            self.missiles -=1
            if self.spare_ammunition >0:
                self.missiles +=1
                self.spare_ammunition -=1
        else:
            speak(('nie masz apteczek'))

class Grenades(Weapon):
    def fire(self, player):
        if self.missiles <=0:
            speak(('nie masz granatow'))
        else:
            player.main_aim = None
            self.missiles -=1
            if self.spare_ammunition >0:
                self.missiles +=1
                self.spare_ammunition -=1
            odtwarzacz = pyglet.media.Player()
            odtwarzacz.queue(self.fire_sound)
            for x in player.aims:
                x.life = False
                if x.special == True:
                    player.special +=1
                odtwarzacz.queue(x.died[0])
            odtwarzacz.play()
            player.aims.clear()

#male wytlumaczenie do kodu powyzej
#tutaj obsluga dzwieku jest poprzez klase Player(), dlatego ze nie wiem juz kompletnie jak zrobic, zeby dzwiek umierania npc byl w calosci po dzwieku wybuchu granatu
#ma to dzialac w ten sposob ze - dodaje sie dzwieki do kolejki(odtwarzacz.queue(dzwiek)), nastepnie na koncu skryptu odpala sie cala kolejke .play()

class Snajper(Weapon):
    def fire(self, player):
        miss = bool(randint(0, 1))
        if self.missiles >0:
            self.fire_sound.play()
            self.missiles -=1
        else:
            self.empty_sound.play()
        try:
            if (player.main_aim == None) or (self.missiles <=0):
                pass
            else:
                player.main_aim.hp -= randint(51, self.damage)
                player.main_aim.injured[randint(0, 4)].play()
                if player.main_aim.hp <=0:
                    player.main_aim.died[randint(0, 4)].play()
                    player.main_aim.life = False
                    if player.main_aim.special == True:
                        player.special +=1
                    player.aims.remove(player.main_aim)
                    if len(player.aims) > 0:
                        player.main_aim = player.aims[0]
                    else:
                        player.main_aim = None
        except:
            pass

    def mode(self, player, area, modespace):
        zoomin = sounds.zoomin
        zoomout = sounds.zoomout
        if modespace == True:
            player.aims.clear()
            player.main_aim = None
            player.aims.extend(area.npcs)
            zoomin.play()
        if modespace == False:
            player.aims.clear()
            player.main_aim = None
            zoomout.play()



class Npc:
    def __init__(self, desc='', aggresiv=False, walker=False, special=False, x=0, y=0, hp=100, name='', life=True):
        self.special = special
        self.npc_attacks = sounds.npc['fire']
        self.name = name
        self.desc = desc
        self.x = x
        self.y = y
        self.hp = hp
        self.aggresiv = aggresiv
        self.walker = walker
        self.injured = sounds.npc['injured']
        self.died = sounds.npc['died']
        self.life = life

    def update(self):
        """tutaj obslugiwane jest poruszanie sie, najpierw sprawdza czy pozycja npc nie jest mniejsza od 0, jezeli tak to rowna ja 0, nastepnie losuje czy ma sie poruszyc, jezeli tak to sprawdza czy atrybut walker jest prawdziwy, wtedy losuje o ile ma sie poruszyc, zakres od -2 do 2"""
        if self.x<0:
            self.x = 0

        if self.y <0:
            self.y = 0

        if bool(randint(0, 1))==True:
            if self.walker == True:
                self.x += randint(-2, 2)
                self.y += randint(-2, 2)

