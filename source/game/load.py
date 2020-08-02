import random, math
import pygletembed as pyglet
import resources, world, asteroid

def d(a=(0,0),b=(0,0)):
	return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def asteroids(n,pos,batch=None):
	asteroids=[]
	for i in range(n):
		x,y=pos
		while d((x,y),pos)<200:
			x=random.randint(0,800)
			y=random.randint(0,600)
		new_asteroid=asteroid.Asteroid(x=x,y=y,
			batch=batch)
		new_asteroid.rotation=random.randint(0,360)
		new_asteroid.xvel=random.random()*70
		new_asteroid.yvel=random.random()*70
		asteroids.append(new_asteroid)
	return asteroids

def lives(n,batch=None):
	lives=[]
	for i in range(n):
		life=pyglet.sprite.Sprite(
			img=resources.player_image,x=785-30*i,y=585,
			batch=batch)
		life.scale=0.5
		life.rotation=-60
		lives.append(life)
	return lives