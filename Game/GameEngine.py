from pyglet.window import key
from random import randint
from collections import Counter as counter
from . import sounds, player, guns, areas
from .classes import speak
from .classes import Weapon, Ammo, Area

baza = areas.baza1

class Gra:
    """cala logika gry, zawiera obiekty takie jak player, area, map, keys - ktore to sa instancjami klas o tej samej nazwie - obserwuje i nadzoruje wszystkie obiekty w grze, okresla ich wzajemne relacje, odpowiada za wszystko"""
    def __init__(self, keys, area = baza):
        self.keys = keys
        self.player = player.player
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
        self.shiftcounter = 0
        self.focuscounter = 0
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
        if self.area in area.exits:
            pass
        else:
            self.area.x = 0
            self.area.y = 0
            area.exits.append(self.area)
        self.area = area
        self.player.x, self.player.y = 0, 0
        area.sound.play()
        self.exitcontainer.clear()



    def action(self, obj):
        if isinstance(obj, Area)==True:
            self.next_area(obj)
        if isinstance(obj, Weapon)==True:
            self.player.add_weapon(obj)
        if isinstance(obj, Ammo)==True:
            if obj.type in self.player.eq:
                self.player.eq[obj.type].add_ammo(obj)



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

        if self.keys[key.ENTER]:
            self.action(self.focus)


        if self.keys[key.LSHIFT]:
            self.shiftfocus = self.shiftcontainer[self.shiftcounter]
            if self.shiftcounter == 0:
                speak(('przedmioty na ziemi'))
            if self.shiftcounter == 1:
                speak(('wyjscia z lokacji'))
            self.shiftcounter +=1




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
#            try:
                speak(('posiadasz w magazynku', str(self.player.current_weapon.missiles), 'pociskow'))
                speak(('do tego posiadasz ', str(len(self.player.current_weapon.spare_ammunition)), 'zapasowych magazynkow'))
#            except:
#                speak(('brak amunicji do tej broni'))

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
            self.focuscounter +=1
            self.focus = self.shiftfocus[(self.focuscounter -1)]
            speak((str(self.focus.name)))


        if self.keys[key.Z]:
            speak(('x', str(self.player.x), 'y', str(self.player.y)))

        if self.keys[key.N]:
            for i in self.area.npcs:
                speak((str(i.name),':', str(i.x), str(i.y)))

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




