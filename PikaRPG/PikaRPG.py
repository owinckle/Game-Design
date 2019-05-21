import pygame as pg
from Config import Config
from Game import Game

def main():
	config	= Config("config")
	game	= Game(config)
	game.loop()

if __name__ == "__main__":
	main()