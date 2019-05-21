import pygame as pg
import Events as ev
import Draw as draw
import Sprites as sp
import Tilemap as tmap
vec = pg.math.Vector2

''' Sprites Indexes '''
# 0 : Bush

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
		self.config		= config

		self.clock		= pg.time.Clock()
		self.status		= True
		self.screen		= pg.display.set_mode((self.width, self.height))
		self.sprites	= pg.sprite.Group()
		self.walls		= pg.sprite.Group()
		self.load_map()
		for row, tiles in enumerate(self.map.data):
			for col, tile in enumerate(tiles):
				if tile == "P":
					self.p_pos = vec(col, row)
				else:
					sp.Ground(self, col, row)
				if tile == "1":
					sp.Wall(self, col, row)

		self.player = sp.Player(self, self.p_pos.x, self.p_pos.y)
		self.camera = tmap.Camera(self, self.map.width, self.map.height)

		pg.key.set_repeat(500, 100)
		pg.display.set_caption(self.name)

	def load_map(self):
		self.map = tmap.Map(self, "spawn.txt")
		self.player_img = pg.image.load("assets/" + self.config.player_0).convert_alpha()
		self.sp_array = []
		self.sp_array.append(pg.image.load("assets/" + self.config.sprite_bush).convert_alpha())
		self.sp_array.append(pg.image.load("assets/" + self.config.sprite_grass).convert_alpha())

	def loop(self):
		while self.status:
			self.dt	= self.clock.tick(self.fps) / 1000
			ev.handle(self)
			draw.draw(self)
