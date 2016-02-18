import random

class Apple:

	def __init__(self, pos_x, pos_y, size):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.size = size
		
	def generatePosition(self):
		self.pos_x = random.randint(0, 390)
		self.pos_y = random.randint(0, 290)
	