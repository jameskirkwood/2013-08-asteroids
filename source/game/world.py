import pygletembed as pyglet
from game.util import dist

class WorldObject(pyglet.sprite.Sprite):
	def __init__(self,*args,**kwargs):
		super(WorldObject,self).__init__(*args,**kwargs)
		self.xvel,self.yvel=0.0,0.0
		self.alive=True
		self.new_obj_buffer=[]
		
	def update(self,dt):
		self.x+=self.xvel*dt
		self.y+=self.yvel*dt
		self.screenwrap()

	def screenwrap(self):
		minx=-self.image.width/2
		miny=-self.image.height/2
		maxx=800+self.image.width/2
		maxy=600+self.image.height/2
		if self.x<minx:
			self.x=maxx
		elif self.x>maxx:
			self.x=minx
		if self.y<miny:
			self.y=maxy
		elif self.y>maxy:
			self.y=miny

	def touches(self,obj):
		min_d=self.image.width/2*self.scale+obj.image.width/2*obj.scale
		d=dist(self.position,obj.position)
		return d<=min_d

	def hit(self,obj):
		if type(self)!=type(obj):
			self.alive=False