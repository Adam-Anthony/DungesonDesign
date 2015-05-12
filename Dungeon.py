import random as rand

class Start:
	
	start = rand.randint(1,10)
	left = rand.randint(1,20)
	right = rand.randint(1,20)

class Passage:

	def __init__(self):
		self.path = rand.randint(1,20)

class Door:
	def __init__(self):
		self.material = rand.randint(1,20)
		self.beyond = rand.randint(1,20)

class Chamber:
	def __init__(self):
		self.types = rand.randint(1,20)
		self.exits = rand.randint(1,20)

class Display:
	g = [0,0,0,0,0,0,0,0,0,0,0]
	mapg = [g,g,g,g,g,g,g,g,g,g,g]

