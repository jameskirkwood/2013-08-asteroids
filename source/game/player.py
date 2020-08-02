import math
import pygletembed as pyglet
from pyglet.window import key
import resources, world, missile, asteroid

class Player(world.WorldObject):
	def __init__(self,*args,**kwargs):
		super(Player,self).__init__(
			img=resources.player_image,*args,**kwargs)
		self.thrust=300
		self.rotspeed=200
		self.key_handler=key.KeyStateHandler()
		self.flame_sprite=pyglet.sprite.Sprite(
			img=resources.flame_image,*args,**kwargs)
		self.flame_sprite.visible=False
		self.muzvel=200.0

	def delete(self):
		self.flame_sprite.delete()
		super(Player,self).delete()

	def on_key_press(self,symbol,modifiers):
		if symbol==key.SPACE:
			self.fire()

#	def on_key_release(self,symbol,modifiers):

	def update(self,dt):
		super(Player,self).update(dt)
		if self.key_handler[key.LEFT]:
			self.rotation-=self.rotspeed*dt
		if self.key_handler[key.RIGHT]:
			self.rotation+=self.rotspeed*dt
		if self.key_handler[key.UP]:
			rad=-math.radians(self.rotation)
			self.xvel+=math.cos(rad)*self.thrust*dt
			self.yvel+=math.sin(rad)*self.thrust*dt
			self.flame_sprite.visible=True
			self.flame_sprite.rotation=self.rotation
			self.flame_sprite.x=self.x
			self.flame_sprite.y=self.y
		else:
			self.flame_sprite.visible=False

	def fire(self):
		rad=-math.radians(self.rotation)
		r=self.image.width/2+resources.missile_image.width/2+3
		x=self.x+math.cos(rad)*r
		y=self.y+math.sin(rad)*r
		new_missile=missile.Missile(x,y,batch=self.batch)
		xvel=self.xvel+math.cos(rad)*self.muzvel
		yvel=self.yvel+math.sin(rad)*self.muzvel
		new_missile.xvel=xvel
		new_missile.yvel=yvel
		new_missile.rotation=self.rotation
		self.new_obj_buffer.append(new_missile)

	def hit(self,obj):
		if ((type(obj)==asteroid.Asteroid and obj.scale>0.4)
			or type(obj)!=asteroid.Asteroid):
			self.alive=False