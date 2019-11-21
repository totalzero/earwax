import pyglet

pyglet.resource.path = ['/Resources', '../Resources', 'Resources']
pyglet.resource.reindex()

#inicjacja wszystkich dzwiekow w grze
itemalert = pyglet.resource.media('itemalert.wav', streaming=False)
getammo = pyglet.resource.media('getammo.wav', streaming=False)
aim = pyglet.resource.media('cel.wav', streaming=False)
tab_sound = pyglet.resource.media('weapons/unduck.wav', streaming=False)
zoomin = pyglet.resource.media('weapons/snajper/zoomin.wav', streaming=False)
zoomout = pyglet.resource.media('weapons/snajper/zoomout.wav', streaming=False)
dooralert = pyglet.resource.media('dooralert.wav', streaming=False)
shiftfocus = pyglet.resource.media('shiftfocus.wav', streaming=False)
focus = pyglet.resource.media('focus.wav', streaming=False)




beretta ={
'fire':pyglet.resource.media('weapons/beretta/fire.wav', streaming=False),
'aimsat':pyglet.resource.media('weapons/beretta/aims_at.wav', streaming=False),
'get':pyglet.resource.media('weapons/beretta/GET_WEAPON.wav', streaming=False),
'reload':pyglet.resource.media('weapons/beretta/reload.wav', streaming=False),
'empty':pyglet.resource.media('weapons/beretta/empty.wav', streaming=False)
}

macarow = {
'fire':pyglet.resource.media('weapons/macarov/fire.wav', streaming=False),
'aimsat':pyglet.resource.media('weapons/macarov/aims_at.wav', streaming=False),
'get':pyglet.resource.media('weapons/macarov/GET_WEAPON.wav', streaming=False),
'reload':pyglet.resource.media('weapons/macarov/reload.wav', streaming=False),
'empty':pyglet.resource.media('weapons/macarov/empty.wav', streaming=False)
}

ak47 = {
'fire':pyglet.resource.media('weapons/ak47/fire.wav', streaming=False),
'aimsat':pyglet.resource.media('weapons/ak47/aims_at.wav', streaming=False),
'get':pyglet.resource.media('weapons/ak47/GET_WEAPON.wav', streaming=False),
'reload':pyglet.resource.media('weapons/ak47/reload.wav', streaming=False),
'empty':pyglet.resource.media('weapons/ak47/empty.wav', streaming=False)
}

barret={
'fire':pyglet.resource.media('weapons/snajper/fire.wav', streaming=False),
'get':pyglet.resource.media('weapons/snajper/GET_WEAPON.wav', streaming=False),
'reload':pyglet.resource.media('weapons/snajper/reload.wav', streaming=False),
'empty':pyglet.resource.media('weapons/snajper/empty.wav', streaming=False),
'aimsat':pyglet.resource.media('weapons/snajper/aims_at.wav', streaming=False)
}

mp4 = {
'fire':pyglet.resource.media('weapons/mp4/fire.wav', streaming=False),
'reload':pyglet.resource.media('weapons/mp4/reload.wav', streaming=False),
'empty':pyglet.resource.media('weapons/mp4/empty.wav', streaming=False),
'get':pyglet.resource.media('weapons/mp4/GET_WEAPON.wav', streaming=False),
'aimsat':pyglet.resource.media('weapons/mp4/aims_at.wav', streaming=False)
}

pp19 = {
'fire':pyglet.resource.media('weapons/pp19/fire.wav', streaming=False),
'empty':pyglet.resource.media('weapons/pp19/empty.wav', streaming=False),
'reload':pyglet.resource.media('weapons/pp19/reload.wav', streaming=False),
'get':pyglet.resource.media('weapons/pp19/GET_WEAPON.wav', streaming=False),
'aimsat':pyglet.resource.media('weapons/pp19/aims_at.wav', streaming=False)
}

knife = {
'fire':pyglet.resource.media('weapons/knife/fire.wav', streaming=False),
'aimsat':pyglet.resource.media('weapons/knife/aims_at.wav', streaming=False)
}

dragunow = {
'fire':pyglet.resource.media('weapons/dragunow/fire.wav', streaming=False),
'aimsat':pyglet.resource.media('weapons/dragunow/aims_at.wav', streaming=False),
'get':pyglet.resource.media('weapons/dragunow/GET_WEAPON.wav', streaming=False),
'empty':pyglet.resource.media('weapons/dragunow/empty.wav', streaming=False),
'reload':pyglet.resource.media('weapons/dragunow/reload.wav', streaming=False)
}

medpack = {
'fire':pyglet.resource.media('weapons/medpack/fire.wav', streaming=False)
}

grenade ={
'fire':pyglet.resource.media('weapons/grenade/fire.wav', streaming=False),
'aimsat':pyglet.resource.media('weapons/grenade/aims_at.wav', streaming=False),
'get':pyglet.resource.media('weapons/grenade/GET_WEAPON.wav', streaming=False)
}

mg4={
'fire':pyglet.resource.media('weapons/mg4/fire.wav', streaming=False),
'empty':pyglet.resource.media('weapons/mg4/empty.wav', streaming=False),
'reload':pyglet.resource.media('weapons/mg4/reload.wav', streaming=False),
'get':pyglet.resource.media('weapons/mg4/GET_WEAPON.wav', streaming=False),
'aimsat':pyglet.resource.media('weapons/mg4/aims_at.wav', streaming=False)
}

doors = {
1:pyglet.resource.media('doors/door1.wav', streaming=False),
2:pyglet.resource.media('doors/door2.wav', streaming=False),
3:pyglet.resource.media('doors/door3.wav', streaming=False)
}

npc = {
'injured':[pyglet.resource.media('npc/injured/1.wav', streaming=False),
pyglet.resource.media('npc/injured/2.wav', streaming=False),
pyglet.resource.media('npc/injured/3.wav', streaming=False),
pyglet.resource.media('npc/injured/4.wav', streaming=False)],
'died':[pyglet.resource.media('npc/died/1.wav', streaming=False),
pyglet.resource.media('npc/died/2.wav', streaming=False),
pyglet.resource.media('npc/died/3.wav', streaming=False),
pyglet.resource.media('npc/died/4.wav', streaming=False)],

'treninginjured':[pyglet.resource.media('npc/trening/injured/1.wav', streaming=False),
pyglet.resource.media('npc/trening/injured/2.wav', streaming=False),
pyglet.resource.media('npc/trening/injured/3.wav', streaming=False),
pyglet.resource.media('npc/trening/injured/4.wav', streaming=False)],

'treningdied':[pyglet.resource.media('npc/trening/died/1.wav', streaming=False),
pyglet.resource.media('npc/trening/died/2.wav', streaming=False),
pyglet.resource.media('npc/trening/died/3.wav', streaming=False),
pyglet.resource.media('npc/trening/died/4.wav', streaming=False)],

'fire':pyglet.resource.media('npc/fire.wav', streaming=False)
}


step_glowny = [pyglet.resource.media('steps/glowny/1.wav', streaming=False),
pyglet.resource.media('steps/glowny/2.wav', streaming=False),
pyglet.resource.media('steps/glowny/3.wav', streaming=False),
pyglet.resource.media('steps/glowny/4.wav', streaming=False),
pyglet.resource.media('steps/glowny/5.wav', streaming=False),
pyglet.resource.media('steps/glowny/6.wav', streaming=False),
pyglet.resource.media('steps/glowny/7.wav', streaming=False),
pyglet.resource.media('steps/glowny/8.wav', streaming=False)]
