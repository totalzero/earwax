import copy
from pyglet.window import key
from random import randint
from collections import Counter as counter
from . import sounds, player, guns
from .classes import speak
from .classes import Weapon, Ammo, Area, SpecialObject

class Gra:
    """cala logika gry, zawiera obiekty takie jak player, area, map, keys - ktore to sa instancjami klas o tej samej nazwie - obserwuje i nadzoruje wszystkie obiekty w grze, okresla ich wzajemne relacje, odpowiada za wszystko"""
    def __init__(self, keys, area, special, tasklog=''):
        self.tasklog = tasklog
        self.status = 'game'
        self.keys = keys
        self.player = player.player
        self.player.special = special
        self.area = area
        self.stepping = 0
        self.alert = sounds.aim
        self.celownik = 0
        self.modespace = False
        self.tab_focus = counter(self.player.eq)
        self.tab_iter = iter(self.tab_focus)
        self.tab_sound = sounds.tab_sound
        self.itemcontainer = []
        self.dooralert = sounds.dooralert
        self.exitcontainer=[]
        self.shiftcontainer = [self.itemcontainer, self.exitcontainer]
        self.shiftfocus = self.exitcontainer
        self.sound_shiftfocus = sounds.shiftfocus
        self.shiftcounter = 0
        self.focuscounter = 0
        self.sound_focus = sounds.focus
        self.focus = None


    def itemadder(self, item):
        itemalert = sounds.itemalert
        itemalert.play()
        speak((str(item.name)))
        if isinstance(item, Weapon) == True:
            self.itemcontainer.insert(0, item)
        else:
            self.itemcontainer.append(item)

    def next_area(self, area):
        self.player.aims.clear()
        self.player.main_aim = None
        self.itemcontainer.clear()
        self.exitcontainer.clear()
        duble = 0
        if len(area.exits) == 0:
            are = copy.deepcopy(self.area)
            are.x, are.y = 0, 0
            area.exits.append(are)
        for i in area.exits:
            if i.name == self.area.name:
                duble +=1
        if duble < 1:
            are = copy.deepcopy(self.area)
            are.x, are.y = 0, 0
            area.exits.append(are)

        self.area = area
        self.player.x, self.player.y = 0, 0
        for x in self.area.exits:
            if x.name == self.area.name:
                self.area.exits.remove(x)
        area.sound.play()


    def action(self, obj):
        if obj == None:
            speak(('co chcesz zrobic?'))
        if isinstance(obj, Area)==True:
            self.next_area(obj)
        if isinstance(obj, SpecialObject)==True:
            self.player.special +=1
            obj.sound.play()
            self.area.object.remove(obj)
            self.itemcontainer.remove(obj)

        if isinstance(obj, Weapon)==True:
            self.player.add_weapon(obj)
            self.area.object.remove(obj)
            self.itemcontainer.remove(obj)
            self.tab_focus = counter(self.player.eq)
            self.tab_iter = iter(self.tab_focus)
        if isinstance(obj, Ammo)==True:
            arg = []
            for x in self.player.eq:
                arg.append(x.name)
            if obj.type in arg:
                for x in self.player.eq:
                    if x.name == obj.type:
                        x.add_ammo()
                        self.itemcontainer.remove(obj)
                        self.area.object.remove(obj)
            else:
                speak(('nie masz broni do tej amunicji'))

    def npc_attacks(self, npc):
        a = bool(randint(0, 1))
        b = bool(randint(0, 1))
        c = bool(randint(0, 1))
        if a&b== True:
            npc.npc_attacks.play()
            if c==True:
                self.player.hp -=randint(0, 5)
                speak(('jestes pod ostrzalem'))

    def update(self):
        if self.player.special >=0:
            self.status = 'win'

        self.area.update()

        if self.stepping >= (len(self.player.step)-1):
            self.stepping = 0

        if self.celownik >= (len(self.player.aims)):
            self.celownik = 0

        if self.shiftcounter >=len(self.shiftcontainer):
            self.shiftcounter = 0

        if self.focuscounter >=len(self.shiftfocus):
            self.focuscounter = 0

        for location in self.area.exits:
            x = abs(self.player.x - location.x)
            y = abs(self.player.y - location.y)
            if (x<=3)&(y<=3):
                if not location in self.exitcontainer:
                    self.exitcontainer.append(location)
                    self.dooralert.play()
            else:
                if location in self.exitcontainer:
                    self.exitcontainer.remove(location)

        if self.keys[key.S]:
            speak((self.player.special))

        if self.keys[key.LSHIFT]:
            self.sound_shiftfocus.play()
            self.shiftfocus = self.shiftcontainer[self.shiftcounter]
            if self.shiftcounter == 0:
                speak(('przedmioty na ziemi'))
            if self.shiftcounter == 1:
                speak(('wyjscia z lokacji'))
            self.shiftcounter +=1

        if self.keys[key.F]:
            if len(self.shiftfocus)==0:
                speak(('tutaj nic nie ma'))
            else:
                self.sound_focus.play()
                self.focuscounter +=1
                self.focus = self.shiftfocus[(self.focuscounter -1)]
                speak((str(self.focus.name)))

        if self.keys[key.X]:
            speak((self.tasklog))

        if self.keys[key.ENTER]:
            self.action(self.focus)
            self.focus = None

        if self.keys[key.E]:
            for x in self.area.exits:
                speak((str(x.name), ':', str(x.x), str(x.y)))
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
            speak(('posiadasz w magazynku', str(self.player.current_weapon.missiles), 'pociskow'))
            speak(('do tego posiadasz ', str(self.player.current_weapon.spare_ammunition), 'zapasowych magazynkow'))

        if self.keys[key.R]:
            if (self.player.current_weapon.spare_ammunition > 0) & (self.player.current_weapon.is_reload==True):
                self.player.current_weapon.missiles = self.player.current_weapon.maxbullets
                self.player.current_weapon.spare_ammunition -=1
                self.player.current_weapon.reload_sound.play()
            else:
                speak(('brak amunicji'))

        if self.keys[key.D]:
            speak((self.area.desc))

        if self.keys[key.LCTRL]:
            try:
                self.player.current_weapon.fire(self.player)
                self.tab_focus = counter(self.player.eq)
                self.tab_iter = iter(self.tab_focus)
                self.area.update()
            except:
                pass

        if self.keys[key.TAB]:
            try:
                self.player.current_weapon = next(self.tab_iter)
                speak(self.player.current_weapon.name)
                self.tab_sound.play()
            except StopIteration:
                self.tab_iter = iter(self.tab_focus)
                self.tab_focus = counter(self.player.eq)


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

        if self.keys[key.Z]:
            speak(('x', str(self.player.x), 'y', str(self.player.y)))

        if self.keys[key.N]:
            for i in self.area.npcs:
                speak((str(i.name),':', str(i.x), str(i.y)))
            speak(('przeciwnikow w tej lokacji:', len(self.area.npcs), 'w twoim zasiegu:', len(self.player.aims)))
        if self.keys[key.C]:
            for i in self.area.object:
                speak((str(i.name), 'x:', str(i.x), 'y:', str(i.y)))

        if self.keys[key.M]:
            speak(((self.area.name)))

        if self.keys[key.O]:
            if len(self.exitcontainer) >0:
                self.player.aims.clear()
                self.player.main_aim = None
                self.itemcontainer.clear()
                if self.area in location.exits:
                    pass
                else:
                    self.area.x = 0
                    self.area.y = 0
                    location.exits.append(self.area)
                self.area = self.exitcontainer[0]
                self.player.x, self.player.y = 0, 0
                location.sound.play()
                self.exitcontainer.clear()
            else:
                speak(('tutaj nie ma drzwi'))


        if self.modespace == False:
            for i in self.area.npcs:
                x = abs(i.x - self.player.x)
                y = abs(i.y - self.player.y)
                if (x <= 5) & (y <=5):
                    if not i in self.player.aims:
                        self.alert.play()
                        self.player.aims.append(i)
                        i.walker = False
                else:
                    if i in self.player.aims:
                        self.player.aims.remove(i)
                        i.walker = True

        for x in self.player.aims:
            if x.aggresiv == True:
                self.npc_attacks(x)
                if self.player.main_aim == None:
                    self.player.main_aim = x

        self.area.update()

        for i in self.area.object:
        #pentla dodajaca itemy do self.itemcontainer
            x = abs(i.x - self.player.x)
            y = abs(i.y - self.player.y)
            if (x==0)&(y==0):
                if not i in self.itemcontainer:
                    self.itemadder(i)
            if (x>3)&(y>3):
                if i in self.itemcontainer:
                    self.itemcontainer.remove(i)

    def moving(self):
        if self.player.hp <=0:
            self.status = 'gameover'

        if self.keys[key.UP]:
            if self.player.y <= self.area.max_y:
                self.player.y +=1
                self.player.step[self.stepping].play()
                self.stepping +=1

        if self.keys[key.DOWN]:
            if self.player.y >0:
                self.player.step[self.stepping].play()
                self.stepping +=1
                self.player.y -=1
                if self.player.y < 0:
                    self.player.y = 0

        if self.keys[key.LEFT]:
            if self.player.x >0:
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




