import random, math
import pyglet
from . import resources, world
class Asteroid(world.WorldObject):
	def __init__(self,*args,**kwargs):
		super(Asteroid,self).__init__(
			resources.asteroid_image,*args,**kwargs)
		self.rotspeed=(random.random()*2-1)*60

	def hit(self,obj):
		if type(obj)==Asteroid:
			sizeratio=float(obj.scale)/self.scale
			if sizeratio>1:
				self.alive=False
			dx=self.x-obj.x
			dy=self.y-obj.y
			disp=math.sqrt(dx**2+dy**2)+0.0001
			prefdisp=self.image.width/2*self.scale+obj.image.width/2*obj.scale
			self.x=obj.x+dx/disp*prefdisp
			self.y=obj.y+dy/disp*prefdisp
			magnvel=math.sqrt(self.xvel**2+self.yvel**2)

			self.xvel+=dx*sizeratio*0.9
			self.yvel+=dy*sizeratio*0.9
		else:
			self.alive=False
		if not self.alive and self.scale>0.15:
			offspring=random.randint(2,5)
			self.xvel/=offspring
			self.yvel/=offspring
			for i in range(offspring):
				new_asteroid=Asteroid(
					x=self.x,y=self.y,batch=self.batch)
				new_asteroid.rotation=random.randint(0,360)
				new_asteroid.xvel=(
					(random.random()*2-1)*70+self.xvel)
				new_asteroid.yvel=(
					(random.random()*2-1)*70+self.yvel)
				new_asteroid.scale=self.scale/math.sqrt(offspring)
				self.new_obj_buffer.append(new_asteroid)

	def update(self,dt):
		super(Asteroid,self).update(dt)
		self.rotation+=self.rotspeed*dt