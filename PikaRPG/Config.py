class Config:
	def __init__(self):
		self.name		= "PikaRPG"
		self.width		= 1024
		self.height		= 768
		self.fps		= 60
		self.tilesize	= 32

class Tiles:
	def __init__(self):
		self.player		= []
		self.player.append("assets/player_0.png")
		self.player.append("assets/player_1.png")
		self.player.append("assets/player_2.png")
		self.player.append("assets/player_3.png")

		self.obstacles	= []
		self.obstacles.append("assets/bush.png")
		self.obstacles.append("assets/tree_1.png")

		self.ground	= []
		self.ground.append("assets/grass.png")
		self.ground.append("assets/sand.png")
		self.ground.append("assets/grass_sand_left_right.png")
		self.ground.append("assets/grass_sand_top_bottom.png")

		self.npc	= []
		self.npc.append("assets/npc1_0.png")

class Colors:
	def __init__(self):
		self.DARKGREY	= (40, 40, 40)
		self.LIGHTGREY	= (100, 100, 100)
		self.RED		= (250, 50, 50)
		self.LIME		= (50, 250, 50)