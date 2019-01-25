class Result():
	def __init__(self, points, sat):
		self.points = points
		self.sat = sat

	def get_max_x(self):
		return self.points[1]

	def get_max_y(self):
		return self.points[3]

	def __str__(self):
		return str(self.points) + " " + str(self.sat)
