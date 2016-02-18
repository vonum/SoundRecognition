class Player:

	def __init__(self, pos_x, pos_y, size, step, orientation):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.size = size
		self.step = step
		self.orientation = orientation
		self.pos = []
		self.pos.append([pos_x, pos_y])
		self.score = 0
		
	def move(self):

		for i in range(len(self.pos) - 1, 0, -1):
			self.pos[i] = self.pos[i - 1]


		if self.orientation == 0:
			self.pos_y = self.pos_y + self.step
			if self.pos_y > 300:
				self.pos_y = 0
		elif self.orientation == 1:
			self.pos_y = self.pos_y - self.step
			if self.pos_y < 0:
				self.pos_y = 300
		elif self.orientation == 2:
			self.pos_x = self.pos_x + self.step
			if self.pos_x > 400:
				self.pos_x = 0
		else:
			self.pos_x = self.pos_x - self.step
			if self.pos_x < 0:
				self.pos_x = 400

		self.pos[0] = [self.pos_x, self.pos_y]
			
	def checkApple(self, ap):
		if ap.pos_x + ap.size < self.pos_x:
			return False
		if ap.pos_y + ap.size < self.pos_y:
			return False
		if ap.pos_y > self.pos_y + self.size:
			return False
		if ap.pos_x > self.pos_x + self.size:
			return False
			
		self.score += 1
		self.pos.append([self.pos[len(self.pos) - 1][0], self.pos[len(self.pos) - 1][1]])

		return True


			