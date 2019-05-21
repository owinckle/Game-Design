import utils

class Config:
	def __init__(self, filename):
		lines	= utils.readFile(filename)

		if lines:
			# Attributes
			array	= ["name", "width", "height", "fps", "tilesize", "player_speed"]

			# Loop & set config
			for line in lines:
				self.line = line

				# Remove comment & new line
				line = line.replace("\n", "").split("#")[0]

				# Check for "set"
				if line.count("set "):
					line = line.split("set")[1]
				else:
					line = ""

				# Remove white spaces
				line = line.replace(" ", "").replace("\t", "")

				for x in array:
					# Check if attribute is valid
					tmp = checkMatch(line, x)

					# Check if line is valid
					if line != tmp and tmp != "":
						setattr(self, x, tmp)

def checkMatch(string, substring):
	# Append ="
	substring += "=\""

	# Check if the occurence of the attribute matched is on the far left
	if string.count(substring) and string.split(substring)[0] == "":
		string = string.split(substring)[1]
	else:
		return string

	# Check if the closing ["] is the last character
	if string.count("\"") == 1 and string.split("\"")[1] == "":
		string = string.split("\"")[0]
	else:
		string = ""
	return string
