import random as rand

class Start:
	
	def __init__(self):
		self.start = rand.randint(1,10)
		self.left = rand.randint(1,20)
		self.right = rand.randint(1,20)

class Passage:

	def __init__(self):
		self.path = rand.randint(1,20)

class Door:
	material = rand.randint(1,20)
	beyond = rand.randint(1,20)

class Chamber:
	types = rand.randint(1,20)
	exits = rand.randint(1,20)

class Display:
	g = [0,0,0,0,0,0,0,0,0,0,0]
	mapg = [g,g,g,g,g,g,g,g,g,g,g]
