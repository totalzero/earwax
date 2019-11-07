from pyglet.window import key
from random import randint
from collections import Counter as counter
from . import sounds, player, guns, areas
from .classes import speak
from .classes import Weapon

class Gra:
    """cala logika gry, zawiera obiekty takie jak player, area, map, keys - ktore to sa instancjami klas o tej samej nazwie - obserwuje i nadzoruje wszystkie obiekty w grze, okresla ich wzajemne relacje, odpowiada za wszystko"""
    def __init__(self, keys):

        self.keys = keys
        self.player = player.player
        self.area = areas.baza1
        self.stepping = 0
        self.alert = sounds.aim
        self.celownik = 0
        self.modespace = False
        self.tab_focus = counter(self.player.eq)
        self.tab_iter = iter(self.tab_focus)
        self.tab_sound = sounds.tab_sound
        self.itemcounter = []

    def itemadder(self, item):
        itemalert = sounds.itemalert
        itemalert.play()
        if isinstance(item, Weapon) == True:
            itemcounter[0] = item
        else:
            self.itemcounter.append(item)


    def open_door(self, name_loc):
        self.area = self.mapa[name_loc]

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
            if len(self.itemcounter) >0:
                for i in itemcounter:
                    if i.type in self.player.eq:
                        self.player.current_weapon.add_ammo(i)
                        self.area.remove(i)
                        self.itemcounter.remove(i)
            else:
                self.player.add_weapon(i)


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
            try:
                for location in self.area.object:
                    x = abs(location.x - self.player.x)
                    y = abs(location.y - self.player.y)
                    if (x<=3)& (y<=3):
                        self.player.aims.clear()
                        self.player.main_aim = None
                        self.itemcounter.clear()
                        self.area = location
                        location.sound.play()
            except:
                speak(('gdzie chcesz wejsc?'))



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




