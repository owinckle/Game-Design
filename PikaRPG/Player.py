import pygame as pg
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups	= game.sprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game	= game
		self.image	= pg.image.load(game.tiles.player[0]).convert_alpha()
		self.rect	= self.image.get_rect()
		self.vel	= vec(0, 0)
		self.pos	= vec(x, y) * game.config.tilesize
		self.speed	= 150

	def collide_with_walls(self, direction):
		if direction == "x":
			hits = pg.sprite.spritecollide(self, self.game.obstacles, False)
			if hits:
				if self.vel.x > 0:
					self.pos.x = hits[0].rect.left - self.rect.width
				if self.vel.x < 0:
					self.pos.x = hits[0].rect.right
				self.vel.x = 0
				self.rect.x = self.pos.x
		if direction == "y":
			hits = pg.sprite.spritecollide(self, self.game.obstacles, False)
			if hits:
				if self.vel.y > 0:
					self.pos.y = hits[0].rect.top - self.rect.height
				if self.vel.y < 0:
					self.pos.y = hits[0].rect.bottom
				self.vel.y =0
				self.rect.y = self.pos.y

	def get_keys(self):
		self.vel	= vec(0, 0)
		keys		= pg.key.get_pressed()

		if keys[pg.K_DOWN] or keys[pg.K_s]:
			self.vel.y	= self.speed
			self.image	= pg.image.load(self.game.tiles.player[0]).convert_alpha()

		if keys[pg.K_RIGHT] or keys[pg.K_d]:
			self.vel.x	= self.speed
			self.image	= pg.image.load(self.game.tiles.player[1]).convert_alpha()

		if keys[pg.K_UP] or keys[pg.K_z]:
			self.vel.y	= -self.speed
			self.image	= pg.image.load(self.game.tiles.player[2]).convert_alpha()

		if keys[pg.K_LEFT] or keys[pg.K_q]:
			self.vel.x	= -self.speed
			self.image	= pg.image.load(self.game.tiles.player[3]).convert_alpha()

		if self.vel.x	!= 0 and self.vel.y != 0:
			self.vel	*= 0.7071

	def scene(self):
		if self.pos.y > self.game.config.height:
			self.game.currentScene.next_scene(self.game, y=1)

		if self.pos.y < 0 - self.game.config.tilesize:
			self.game.currentScene.next_scene(self.game, y=-1)

		if self.pos.x > self.game.config.width:
			self.game.currentScene.next_scene(self.game, x=1)

		if self.pos.x < 0 - self.game.config.tilesize:
			self.game.currentScene.next_scene(self.game, x=-1)

		if pg.sprite.spritecollide(self, self.game.objects, False):
			self.game.currentScene.next_scene(self.game, inside=1)

		if pg.sprite.spritecollide(self, self.game.teleporter, False):
			self.game.currentScene.next_scene(self.game, teleporter=1)

	def update(self):
		self.get_keys()
		self.pos += self.vel * self.game.dt
		self.rect.x = self.pos.x
		self.collide_with_walls("x")
		self.rect.y = self.pos.y
		self.collide_with_walls("y")
		self.scene()
