class Region():
    def __init__(self, area, sat):
        self.area = area
        self.sat = sat

    def projection(self, param):
        return self.area[param]

    def __str__(self):
        return str(self.area) + " " + str(self.sat)
