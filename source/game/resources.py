import pygletembed as pyglet

pyglet.resource.path=["../resources"]
print pyglet.resource.reindex()

player_image=pyglet.resource.image("ship.png")
missile_image=pyglet.resource.image("missile.png")
asteroid_image=pyglet.resource.image("asteroid.png")
flame_image=pyglet.resource.image("flame.png")

def imgRotCentre(image):
	image.anchor_x=image.width/2
	image.anchor_y=image.height/2

for image in [player_image,missile_image,asteroid_image]:
	imgRotCentre(image)

flame_image.anchor_x=flame_image.width+player_image.width/2
flame_image.anchor_y=flame_image.height/2