class Player:

	def __init__(self, pos_x, pos_y, size, step, orientation):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.size = size
		self.step = step
		self.orientation = orientation
		
	def move(self):
		if self.orientation == 0:
			self.pos_y = self.pos_y + self.step
		elif self.orientation == 1:
			self.pos_y = self.pos_y - self.step
		elif self.orientation == 2:
			self.pos_x = self.pos_x + self.step
		else:
			self.pos_x = self.pos_x - self.step
			
	def checkApple(self, ap):
		if ap.pos_x + ap.size < self.pos_x:
			return False
		if ap.pos_y + ap.size < self.pos_y:
			return False
		if ap.pos_y > self.pos_y + self.size:
			return False
		if ap.pos_x > self.pos_x + self.size:
			return False
			
		return True
			