import random

class Apple:

	def __init__(self, size):
		self.pos_x = random.randint(0, 390)
		self.pos_y = random.randint(0, 290)
		self.size = size
		
	def generatePosition(self):
		self.pos_x = random.randint(0, 390)
		self.pos_y = random.randint(0, 290)
	