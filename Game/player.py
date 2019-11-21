from . import sounds, guns
from .classes import Player

step = sounds.step_glowny
beretta = guns.beretta
beretta.spare_ammunition = 5
eq = [beretta, guns.knife, guns.medpack]

player = Player(step=step, eq = eq)

