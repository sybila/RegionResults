COLORS = {-2: "orange", -1: "red", 0: "gray", 1: "green", 2: "blue"}

class Picture():
	def __init__(self, width, height):
		self.regions = []
		#lines = []
		self.header = '<svg width="' + str(width) + '" height="' + str(height) + '">\n'
		self.footer = '</svg>'

	def load_rectangles(self, rectangles):
		for result in rectangles:
			self.add_rectangle(result.points, result.sat)

	# x1, x2, y1, y2
	def add_rectangle(self, points, result):
		self.regions.append('<rect x="{0}" y="{1}" width="{2}" height="{3}" style="fill:{4}" />'.\
				format(points[0], points[2], points[1]-points[0], points[3]-points[2], COLORS[result]))

	def save(self, filename):
		f = open(filename, "w")
		f.write(self.header)
		#for line in lines:
		#	f.write(line)
		for region in self.regions:
			f.write(region)
		f.write(self.footer)
		f.close()