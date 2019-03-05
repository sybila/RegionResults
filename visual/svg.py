COLORS = {-2: "#cc5700", -1: "red", 0: "gray", 1: "green", 2: "#1fb842"}

class Picture():
	def __init__(self, w_min, w_max, h_min, h_max):
		self.regions = []
		self.w_min, self.w_max, self.h_min, self.h_max = w_min, w_max, h_min, h_max
		self.width = w_max - w_min
		self.height = h_max - h_min
		self.offset = self.width/3 if self.width < self.height else self.height/3
		self.x_scale, self.y_scale = self.calculate_scales()
		self.lines = []
		self.texts = []
		self.points = []
		self.header = '<svg width="' + str(self.width*self.x_scale + self.offset) + '" height="' + str(self.height*self.y_scale + self.offset) + '">\n'
		self.footer = '</svg>'
		self.add_axis_description(self.width*self.x_scale, self.height*self.y_scale)

	def calculate_scales(self):
		if self.height > self.width:
			return self.height/self.width, 1
		else:
			return 1, self.width/self.height

	def load_rectangles(self, rectangles):
		for result in rectangles:
			self.add_rectangle(result.points, result.sat)

	def load_points(self, points):
		for (x, y, value) in points:
			self.add_point(x, y, self.colorify(value))

	# x1, x2, y1, y2
	def add_rectangle(self, points, result):
		x = points[0]*self.x_scale + self.offset - self.w_min
		y = points[2]*self.y_scale + self.offset - self.h_min
		width = (points[1]-points[0])*self.x_scale
		height = (points[3]-points[2])*self.y_scale
		self.regions.append('<rect x="{0}" y="{1}" width="{2}" height="{3}" style="fill:{4}" />'.\
				format(x, y, width, height, COLORS[result]))

	def add_axis_description(self, scaled_width, scaled_height):
		self.add_line(self.offset, self.offset, \
					  self.offset, self.offset + scaled_height)
		self.add_line(self.offset, self.offset, \
					  self.offset + scaled_width, self.offset)
		for i in range(11):
			y = self.offset + (scaled_height/10)*i
			self.add_line(self.offset - self.offset/5, y, self.offset, y)
			self.add_text(self.offset/20, y, "{0:.2f}".format(self.h_min + (self.height/10)*i))

		for i in range(10):
			x = self.offset + (scaled_width/10)*i
			self.add_line(x, self.offset - self.offset/5, x, self.offset)
			self.add_text(x - self.offset/5, self.offset/2, "{0:.2f}".format(self.w_min + (self.width/10)*i))

	def add_text(self, x, y, text):
		self.texts.append('<text x="{0}" y="{1}" font-size="{2}">{3}</text>'\
				  .format(x, y, self.offset/4, text))

	def add_line(self, x1, y1, x2, y2):
		self.lines.append('<line x1="{0}" y1="{1}" x2="{2}" y2="{3}" \
			style="stroke:black;stroke-width:{4}"/>'.format(x1, y1, x2, y2, self.offset/30))

	def add_point(self, x, y, color):
		self.points.append('<circle cx="{0}" cy="{1}"\
			 r="f" stroke="black" stroke-width="1" fill="{2}" />'.format(x, y, color))

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

	def colorify(self, value):
		return #some color