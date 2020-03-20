from .region import *
from fractions import Fraction

RESULTS = {"ExistsViolated": -2, "CenterViolated": -2, "AllViolated": -1,
           "Unknown": 0, "ExistsBoth": 0,
           "AllSat": 1, "CenterSat": 2, "ExistsSat": 2}


class Parser():
    def __init__(self):
        self.regions = []
        self.params = []

    def parse_file(self, filename):
        input_file = open(filename, "r")
        start = False
        for line in input_file.readlines():
            if line.rstrip():
                if "Command line arguments" in line:
                    self.params = self.get_params(line)
                elif "Region results:" in line:
                    start = True
                elif "Region refinement" in line:
                    start = False
                elif start:
                    self.regions.append(self.parse_region(line))

    def parse_region(self, line):
        region, sat = line.split(";")[0], line.split(";")[1]
        parts = region.split(",")

        points = dict()

        for part in parts:
            fractions = part.split("<=")
            values = (float(Fraction(fractions[0])), float(Fraction(fractions[2])))
            points[fractions[1]] = values

        for key in RESULTS.keys():
            if key in sat:
                return Region(points, RESULTS[key])

    def get_params(self, line):
        params = []
        ranges = line.split("--region '")[1].split("' --refine")[0]
        parts = ranges.split(",")
        for part in parts:
            names = part.split("<=")
            params.append(names[1])
        return params
