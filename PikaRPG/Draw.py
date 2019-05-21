import pygame as pg
from Colors import *

def grid(game):
	for x in range(0, game.width, game.tilesize):
		pg.draw.line(game.screen, LIGHTGREY, (x, 0), (x, game.height))

	for y in range(0, game.height, game.tilesize):
		pg.draw.line(game.screen, LIGHTGREY, (0, y), (game.width, y))

def draw(game):
	game.screen.fill(DARKGREY)
	grid(game)
	game.player.update()
	game.sprites.draw(game.screen)
	pg.display.flip()
