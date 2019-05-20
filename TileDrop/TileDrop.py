import pygame
from random import randint
import sys

sys.path.insert(0, "../lib/")
from colors import Colors

class Player:
	def __init__(self, width, height):
		self.size	= 50
		self.x		= width / 2
		self.y		= height - 2 * self.size

class Enemy:
	def __init__(self, width, height, speed):
		self.size	= 50
		self.x		= randint(0, width -self.size)
		self.y		= 0
		self.speed	= speed
		self.width	= width
		self.height	= height

	def update(self):
		if self.y >= 0 and self.y < self.height:
			self.y += self.speed
			return 0
		else:
			self.y = 0
			self.x = randint(0, self.width - self.size)
			return 1

class Game:
	def __init__(self, name, width, height):
		# Game Variables
		self.name	= name
		self.width	= width
		self.height	= height
		self.active	= True
		self.clock	= pygame.time.Clock()
		self.screen	= pygame.display.set_mode((width, height))
		self.colors	= Colors()
		self.score	= 0

		# Player
		self.player = Player(width, height)

		# Enemy
		self.enemy	= Enemy(width, height, 10)

		pygame.display.set_caption(name)
		pygame.display.flip()

	def detect_collision(self):
		if (self.enemy.x >= self.player.x and self.enemy.x < (self.player.x + self.player.size)) or \
			(self.player.x >= self.enemy.x and self.player.x < (self.enemy.x + self.enemy.size)):
			if (self.enemy.y >= self.player.y and self.enemy.y < (self.player.y + self.player.size)) or \
			(self.player.y >= self.enemy.y and self.player.y < (self.enemy.y + self.enemy.size)):
				self.active = False
				print("Final Score: %d" % (self.score))

	def draw(self):
		self.score += self.enemy.update()
		self.screen.fill(self.colors.black)
		pygame.draw.rect(self.screen, self.colors.red, (self.player.x, self.player.y, self.player.size, self.player.size))
		pygame.draw.rect(self.screen, self.colors.blue, (self.enemy.x, self.enemy.y, self.enemy.size, self.enemy.size))

def main():
	game	= Game("TileDrop", 300, 600)

	i = 0
	while game.active:
		for event in pygame.event.get():
			# Quit
			if event.type == pygame.QUIT:
				sys.exit()

		# Controls
		if event.type == pygame.KEYDOWN:
			x	= game.player.x
			y	= game.player.y
			if event.key == pygame.K_LEFT:
				if x - game.player.size >= 0:
					x	-= game.player.size
			elif event.key == pygame.K_RIGHT:
				if x + game.player.size <= game.width - game.player.size:
					x	+= game.player.size
			game.player.x	= x
			game.player.y	= y

		if i % 50 == 0:
			game.enemy.speed += 5

		game.detect_collision()
		game.draw()
		game.clock.tick(30)
		pygame.display.update()
		i += 1

if __name__ == "__main__":
	main()