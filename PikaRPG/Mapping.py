import pygame as pg
vec = pg.math.Vector2

class Obstacle(pg.sprite.Sprite):
	def __init__(self, game, x, y, type):
		self.groups	= game.sprites, game.obstacles
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game	= game
		self.image	= pg.image.load(game.tiles.obstacles[type]).convert_alpha()
		self.rect	= self.image.get_rect()
		self.pos	= vec(x, y)
		self.rect.x	= x * game.config.tilesize
		self.rect.y	= y * game.config.tilesize

class Ground(pg.sprite.Sprite):
	def __init__(self, game, x, y, type):
		self.groups	= game.sprites, game.ground
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game	= game
		self.type	= type
		self.image	= pg.image.load(game.tiles.ground[type]).convert_alpha()
		self.rect	= self.image.get_rect()
		self.pos	= vec(x, y)
		self.rect.x	= x * game.config.tilesize
		self.rect.y	= y * game.config.tilesize

class Objects(pg.sprite.Sprite):
	def __init__(self, game, x, y, type):
		self.groups	= game.sprites, game.objects
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game	= game
		self.image	= pg.image.load(game.tiles.objects[type]).convert_alpha()
		self.rect	= self.image.get_rect()
		self.pos	= vec(x, y)
		self.rect.x	= x * game.config.tilesize
		self.rect.y	= y * game.config.tilesize

class Npc(pg.sprite.Sprite):
	def __init__(self, game, x, y, idx):
		self.groups	= game.sprites, game.npc
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game	= game
		self.idx	= idx
		self.image	= pg.image.load(game.currentScene.npc[idx]).convert_alpha()
		self.rect	= self.image.get_rect()
		self.pos	= vec(x, y)
		self.rect.x	= x * game.config.tilesize
		self.rect.y	= y * game.config.tilesize

class Teleporter(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups	= game.sprites, game.teleporter
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game	= game
		self.image	= pg.image.load(game.currentScene.teleporter).convert_alpha()
		self.rect	= self.image.get_rect()
		self.pos	= vec(x, y)
		self.rect.x	= x * game.config.tilesize
		self.rect.y	= y * game.config.tilesize 

class Map:
	def __init__(self, game, filename):
		self.data = []
		self.game = game
		with open("maps/" + filename, "r") as f:
			for line in f:
				self.data.append(line.strip())