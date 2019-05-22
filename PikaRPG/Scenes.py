import pygame as pg

class scene_start():
	def __init__(self):
		self.npc	= []
		self.npc.append("assets/npc1_0.png")
		self.default_ground = 0

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
			print("Hello World")

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