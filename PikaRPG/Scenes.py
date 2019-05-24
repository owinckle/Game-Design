import pygame as pg
import time

class scene_start():
	def __init__(self):
		self.npc	= []
		self.npc.append("assets/npc1_0.png")
		self.npc.append("assets/npc2_0.png")
		self.default_ground = 0

		# Animation Vars
		self.npc_anim_1 = 0
		self.npc_anim_bool_1 = False
		self.npc_anim_speed = 1
		self.npc_iter = 160

	def next_scene(self, game, x=0, y=0, inside=0):
		if x != 0 or y != 0 or inside != 0:
			game.init_sprites()
			if y == 1:
				game.currentScene = scene_start_outskirt()
				game.load("start_outskirt.txt")
			if inside == 1:
				game.currentScene = scene_town_house()
				game.load("town_house.txt")

	def dialogue(self, game):
		hits = pg.sprite.spritecollide(game.player, game.npc, False)
		if hits:
			for npc in hits:
				if npc.idx == 0:
					print("Hello World")
				elif npc.idx == 1:
					print("I am an NPC")
					npc.image = pg.image.load(self.npc[1]).convert_alpha()

	def animate(self, game):
		for npc in game.npc:
			if npc.idx == 1:
				if self.npc_anim_bool_1 == False:
					npc.image = pg.image.load("assets/npc2_1.png").convert_alpha()
				else:
					npc.image = pg.image.load("assets/npc2_3.png").convert_alpha()
				if self.npc_anim_1 < self.npc_iter and self.npc_anim_bool_1 == False:
					npc.rect.x += self.npc_anim_speed
					self.npc_anim_1 += 1
					if self.npc_anim_1 == self.npc_iter:
						self.npc_anim_bool_1 = True
				elif self.npc_anim_bool_1 == True:
					npc.rect.x -= self.npc_anim_speed
					self.npc_anim_1 -= 1
					if self.npc_anim_1 == 0:
						self.npc_anim_bool_1 = False

class scene_town_house():
	def __init__(self):
		self.npc	= []
		self.default_ground = 4
		self.teleporter		= "assets/wooden_floor.png"

	def next_scene(self, game, x=0, y=0, teleporter=0):
		if x != 0 or y != 0 or teleporter != 0:
			game.init_sprites()
			if teleporter == 1:
				game.currentScene = scene_start()
				game.load("init.txt")

class scene_start_outskirt():
	def __init__(self):
		self.npc	= []
		self.default_ground = 0

	def next_scene(self, game, x=0, y=0):
		if x != 0 or y != 0:
			game.init_sprites()
			if y == -1:
				game.currentScene = scene_start()
				game.load("start.txt")