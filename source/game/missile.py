import world, resources, asteroid

class Missile(world.WorldObject):
	def __init__(self,*args,**kwargs):
		super(Missile,self).__init__(
			resources.missile_image,*args,**kwargs)

	def kill(self,dt):
		self.alive=False

	def hit(self,obj):
		if type(obj)==asteroid.Asteroid:
			if obj.scale>=0.25:
				self.alive=False
		else:
			self.alive=False
