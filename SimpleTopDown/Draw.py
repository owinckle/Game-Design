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
	game.sprites.update()
	for sprite in game.sprites:
		game.screen.blit(sprite.image, game.camera.apply(sprite))
	game.camera.update(game.player)
	pg.display.flip()
