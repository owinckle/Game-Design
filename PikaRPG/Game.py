import pygame as pg
import Events as ev
import Draw as draw
import Sprites as sp

class Game():
	def __init__(self, config):
		self.name		= config.name
		self.width		= int(config.width)
		self.height		= int(config.height)
		self.fps		= int(config.fps)
		self.tilesize	= int(config.tilesize)
		self.p_speed	= int(config.player_speed)
		self.gridwidth	= self.width / self.tilesize
		self.gridheight	= self.height / self.tilesize

		self.clock		= pg.time.Clock()
		self.status		= True
		self.screen		= pg.display.set_mode((self.width, self.height))
		self.sprites	= pg.sprite.Group()
		self.walls		= pg.sprite.Group()
		self.load_map()
		for row, tiles in enumerate(self.map_data):
			for col, tile in enumerate(tiles):
				if tile == "1":
					sp.Wall(self, col, row)
				if tile == "P":
					self.player = sp.Player(self, col, row)

		pg.key.set_repeat(500, 100)
		pg.display.set_caption(self.name)

	def load_map(self):
		self.map_data	= []
		with open("maps/spawn.txt", "r") as f:
			for line in f:
				self.map_data.append(line)

	def loop(self):
		while self.status:
			self.dt	= self.clock.tick(self.fps) / 1000
			ev.handle(self)
			draw.draw(self)
