from .result import *
from fractions import Fraction

RESULTS = {"ExistsViolated": -2, "AllViolated": -1, "AllSat": 1, "Unknown": 0, "ExistsSat": 2}

class Parser():
	def __init__(self):
		self.regions = []

	def parse_file(self, filename):
		input_file = open(filename, "r")
		start = False
		for line in input_file.readlines():
			if line.rstrip():
				if "Region results:" in line:
					start = True
				elif "Region refinement" in line:
					start = False
				elif start:
					self.regions.append(self.parse_region(line))

	def parse_region(self, line):
		region, sat = line.split(";")[0], line.split(";")[1]
		parts = region.split(",")

		points = []
		
		for part in parts:
			fractions = part.split("<=")
			points.append(float(Fraction(fractions[0])))
			points.append(float(Fraction(fractions[2])))

		for key in RESULTS.keys():
			if key in sat:
				return Result(points, RESULTS[key])
