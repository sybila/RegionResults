COLORS = {-2: "#cc5700", -1: "red", 0: "gray", 1: "green", 2: "#1fb842"}

class Picture():
	def __init__(self, w_min, w_max, h_min, h_max):
		self.regions = []
		self.w_min, self.w_max, self.h_min, self.h_max = w_min, w_max, h_min, h_max
		width = w_max - w_min
		height = h_max - h_min
		self.offset = width/10 if width < height else height/10
		self.x_scale, self.y_scale = self.calculate_scales(width, height)
		self.lines = []
		self.texts = []
		self.header = '<svg width="' + str(width*self.x_scale + self.offset) + '" height="' + str(height*self.y_scale + self.offset) + '">\n'
		self.footer = '</svg>'
		self.add_axis_description(width*self.x_scale, height*self.y_scale, width, height)

	def calculate_scales(self, width, height):
		if height > width:
			return height/width, 1
		else:
			return 1, width/height

	def load_rectangles(self, rectangles):
		for result in rectangles:
			self.add_rectangle(result.points, result.sat)

	# x1, x2, y1, y2
	def add_rectangle(self, points, result):
		x = points[0]*self.x_scale + self.offset - self.w_min
		y = points[2]*self.y_scale + self.offset - self.h_min
		width = (points[1]-points[0])*self.x_scale
		height = (points[3]-points[2])*self.y_scale
		self.regions.append('<rect x="{0}" y="{1}" width="{2}" height="{3}" style="fill:{4}" />'.\
				format(x, y, width, height, COLORS[result]))

	def add_axis_description(self, width, height, text_width, text_height):
		self.add_line(self.offset, self.offset, \
					  self.offset, self.offset + height)
		self.add_line(self.offset, self.offset, \
					  self.offset + width, self.offset)
		for i in range(11):
			y = self.offset + (height/10)*i
			self.add_line(self.offset - self.offset/5, y, self.offset, y)
			self.add_text(self.offset/20, y, "{0:.2f}".format(self.h_min + (text_height/10)*i))

		for i in range(10):
			x = self.offset + (width/10)*i
			self.add_line(x, self.offset - self.offset/5, x, self.offset)
			self.add_text(x - self.offset/5, self.offset/3, "{0:.2f}".format(self.w_min + (text_width/10)*i))

	def add_text(self, x, y, text):
		self.texts.append('<text x="{0}" y="{1}" font-size="{2}">{3}</text>'\
				  .format(x, y, self.offset/3, text))

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