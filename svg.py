COLORS = {-2: "#cc5700", -1: "red", 0: "gray", 1: "green", 2: "#1fb842"}

class Picture():
	def __init__(self, width, height):
		self.regions = []
		self.offset = width/20 if width < height else height/20
		self.lines = []
		self.texts = []
		self.header = '<svg width="' + str(width + self.offset) + '" height="' + str(height + self.offset) + '">\n'
		self.footer = '</svg>'
		self.add_axis_description(width, height)

	def load_rectangles(self, rectangles):
		for result in rectangles:
			self.add_rectangle(result.points, result.sat)

	# x1, x2, y1, y2
	def add_rectangle(self, points, result):
		points = list(map(lambda point: point + self.offset, points))
		self.regions.append('<rect x="{0}" y="{1}" width="{2}" height="{3}" style="fill:{4}" />'.\
				format(points[0], points[2], points[1]-points[0], points[3]-points[2], COLORS[result]))

	def add_axis_description(self, width, height):
		self.add_line(self.offset, self.offset, \
					  self.offset, self.offset + height)
		self.add_line(self.offset, self.offset, \
					  self.offset + width, self.offset)
		for i in range(11):
			y = self.offset + (height/10)*i
			self.add_line(self.offset - self.offset/5, y, self.offset, y)
			self.add_text(self.offset/10, y, "{0:.2f}".format((height/10)*i))

		for i in range(10):
			x = self.offset + (width/10)*i
			self.add_line(x, self.offset - self.offset/5, x, self.offset)
			self.add_text(x - self.offset/5, self.offset/3, "{0:.2f}".format((width/10)*i))

	def add_text(self, x, y, text):
		self.texts.append('<text x="{0}" y="{1}" font-size="{2}">{3}</text>'\
				  .format(x, y, self.offset/4, text))

	def add_line(self, x1, y1, x2, y2):
		self.lines.append('<line x1="{0}" y1="{1}" x2="{2}" y2="{3}" \
			style="stroke:black;stroke-width:{4}"/>'.format(x1, y1, x2, y2, self.offset/15))

	def save(self, filename):
		f = open(filename, "w")
		f.write(self.header)
		for region in self.regions:
			f.write(region)
		for line in self.lines:
			f.write(line)
		for text in self.texts:
			f.write(text)
		f.write(self.footer)
		f.close()