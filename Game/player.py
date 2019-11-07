from . import sounds, guns
from .classes import Player

step = sounds.step_glowny
parabellum = guns.parabellum
beretta = guns.beretta
beretta.spare_ammunition = [parabellum, parabellum, parabellum, parabellum]
eq = [beretta]
player = Player(step=step, eq = eq)

