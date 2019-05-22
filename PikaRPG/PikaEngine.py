import pygame as pg
from Config import *
from Events import *
from Player import *
from Mapping import *
from Scenes import *
vec = pg.math.Vector2

class PikaEngine():
	def __init__(self):
		self.config		= Config()
		self.tiles		= Tiles()
		self.colors		= Colors()
		self.running	= True
		self.clock		= pg.time.Clock()
		self.screen		= pg.display.set_mode((self.config.width, self.config.height))
		pg.display.set_caption(self.config.name)
		self.init_sprites()
		self.currentMap	= "init.txt"
		self.currentScene	= scene_start()
		self.load("init.txt")

	def init_sprites(self):
		self.sprites	= pg.sprite.Group()
		self.obstacles	= pg.sprite.Group()
		self.ground		= pg.sprite.Group()
		self.npc		= pg.sprite.Group()
		self.objects	= pg.sprite.Group()
		self.teleporter	= pg.sprite.Group()

	def load(self, map):
		self.map		= Map(self, map)
		self.currentMap	= map
		npc_index		= 0
		for row, tiles in enumerate(self.map.data):
			for col, tile in enumerate(tiles):
				if ord(tile) >= 97 and ord(tile) <= 122:
					Ground(self, col, row, ord(tile) - 97)
				else:
					Ground(self, col, row, self.currentScene.default_ground)
				if ord(tile) >= 49 and ord(tile) <= 57:
					Obstacle(self, col, row, ord(tile) - 49)
				if ord(tile) >= 65 and ord(tile) <= 90:
					if tile == "P":
						self.p_pos = vec(col, row)
					elif tile == "N":
						Npc(self, col, row, npc_index)
						npc_index += 1
					elif tile == "X":
						Teleporter(self, col, row)
					else:
						Objects(self, col, row, ord(tile) - 65)
		self.player	= Player(self, self.p_pos.x, self.p_pos.y)

	def draw(self):
		self.screen.fill(self.colors.DARKGREY)
		self.sprites.draw(self.screen)
		self.player.update()
		pg.display.flip()

	def loop(self):
		while self.running:
			self.dt	= self.clock.tick(self.config.fps) / 1000
			key_events(self)
			self.draw()