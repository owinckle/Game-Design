import sys
import pygame as pg

def handle(game):
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()

		if event.type == pg.KEYDOWN:
			if event.key == pg.K_ESCAPE:
				sys.exit()