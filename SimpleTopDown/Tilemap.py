import pygame as pg

class Map:
	def __init__(self, game, filename):
		self.data = []
		self.game = game
		with open("maps/" + filename, "r") as f:
			for line in f:
				self.data.append(line.strip())

		self.tilewidth	= len(self.data[0])
		self.tileheight	= len(self.data)
		self.width		= self.tilewidth * self.game.tilesize
		self.height		= self.tileheight * self.game.tilesize

class Camera:
	def __init__(self, game, width, height):
		self.camera	= pg.Rect(0, 0, width, height)
		self.game	= game
		self.width	= width
		self.height	= height

	def apply(self, entity):
		return entity.rect.move(self.camera.topleft)

	def update(self, target):
		x	= -target.rect.x + int(self.game.width / 2)
		y	= -target.rect.y + int(self.game.height / 2)

		x	= min(0, x) # left limit
		y	= min(0, y) # top limit
		x	= max(-(self.width - self.game.width), x) # right limit
		y	= max(-(self.height - self.game.height), y) # bottom limit
		self.camera = pg.Rect(x, y, self.width, self.height)