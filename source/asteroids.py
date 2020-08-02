from game import pygletembed as pyglet
from game import resources, load, player

#init window
game_window=pyglet.window.Window(800,600)
g_hud=pyglet.graphics.Batch()
g_sprites=0
g_sprites=pyglet.graphics.Batch()
score=0
scoreDisp=pyglet.text.Label(text='Score: 0',x=10,y=575,batch=g_hud)
lvlnameDisp=pyglet.text.Label(text='Kuiper Belt, 115, 0:12',x=400,y=575,anchor_x='center',batch=g_hud)
lives=load.lives(8,batch=g_hud)

#init world
player_sprite=player.Player(x=400,y=300,batch=g_sprites)
game_window.push_handlers(player_sprite.key_handler)
game_window.push_handlers(player_sprite)
asteroids=load.asteroids(6,player_sprite.position,batch=g_sprites)
world_objects=[player_sprite]+asteroids
print(world_objects)

#define mechanics
def update_all(dt):
	new_obj_buffer=[]
	for i in xrange(len(world_objects)):
		for j in xrange(i+1,len(world_objects)):
			objA=world_objects[i]
			objB=world_objects[j]
			if objA.alive and objB.alive:
				if objA.touches(objB):
					objA.hit(objB)
					objB.hit(objA)
	for each in world_objects:
		each.update(dt)
		if len(each.new_obj_buffer)>0:
			new_obj_buffer+=each.new_obj_buffer
			each.new_obj_buffer=[]
	for each in [obj for obj in world_objects if not obj.alive]:
		each.delete()
		world_objects.remove(each)
	world_objects.extend(new_obj_buffer)

@game_window.event
def on_draw():
	game_window.clear()
	g_hud.draw()
	g_sprites.draw()

#start game
print('\nASTERIODS START\n')
if __name__=='__main__':
	pyglet.clock.schedule_interval(update_all,1.0/120)
	pyglet.app.run()