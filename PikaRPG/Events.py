import pygame as pg
import sys

def key_events(game):
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()

		if event.type == pg.KEYDOWN:
			if event.key == pg.K_ESCAPE:
				sys.exit()
			if event.key == pg.K_e:
				game.currentScene.dialogue(game)
