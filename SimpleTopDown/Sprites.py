import pygame as pg
from Colors import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups	= game.sprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game	= game
		self.image	= game.player_img
		self.rect	= self.image.get_rect()
		self.vel	= vec(0, 0)
		self.pos	= vec(x, y) * game.tilesize

	def get_keys(self):
		self.vel	= vec(0, 0)
		keys	= pg.key.get_pressed()
		if keys[pg.K_LEFT] or keys[pg.K_q]:
			self.vel.x	= -self.game.p_speed
			self.image = pg.image.load("assets/" + self.game.config.player_3).convert_alpha()
		if keys[pg.K_RIGHT] or keys[pg.K_d]:
			self.vel.x	= self.game.p_speed
			self.image = pg.image.load("assets/" + self.game.config.player_1).convert_alpha()
		if keys[pg.K_UP] or keys[pg.K_z]:
			self.vel.y	= -self.game.p_speed
			self.image = pg.image.load("assets/" + self.game.config.player_2).convert_alpha()
		if keys[pg.K_DOWN] or keys[pg.K_s]:
			self.vel.y	= self.game.p_speed
			self.image = pg.image.load("assets/" + self.game.config.player_0).convert_alpha()
		if self.vel.x != 0 and self.vel.y != 0:
			self.vel *= 0.7071

	def collide_with_walls(self, direction):
		if direction == "x":
			hits = pg.sprite.spritecollide(self, self.game.walls, False)
			if hits:
				if self.vel.x > 0:
					self.pos.x = hits[0].rect.left - self.rect.width
				if self.vel.x < 0:
					self.pos.x = hits[0].rect.right
				self.vel.x = 0
				self.rect.x = self.pos.x
		if direction == "y":
			hits = pg.sprite.spritecollide(self, self.game.walls, False)
			if hits:
				if self.vel.y > 0:
					self.pos.y = hits[0].rect.top - self.rect.height
				if self.vel.y < 0:
					self.pos.y = hits[0].rect.bottom
				self.vel.y =0
				self.rect.y = self.pos.y

	def update(self):
		self.get_keys()
		self.pos += self.vel * self.game.dt
		self.rect.x = self.pos.x
		self.collide_with_walls("x")
		self.rect.y = self.pos.y
		self.collide_with_walls("y")

class Wall(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups	= game.sprites, game.walls
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game	= game
		self.image	= game.sp_array[0]
		self.rect	= self.image.get_rect()
		self.x		= x
		self.y		= y
		self.rect.x	= x * game.tilesize
		self.rect.y	= y * game.tilesize

class Ground(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.sprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game	= game
		self.image	= game.sp_array[1]
		self.rect	= self.image.get_rect()
		self.x		= x
		self.y		= y
		self.rect.x	= x * game.tilesize
		self.rect.y	= y * game.tilesize
