import numpy as np
import sympy
from sympy.parsing.sympy_parser import parse_expr
import svg

def column(matrix, i):
    return [row[i] for row in matrix]

def samplePoints(range_x, num_x, range_y, num_y, function, symbols):
	x, y = sympy.symbols(symbols)
	function = parse_expr(function)
	results = []

	for i in np.linspace(range_x[0], range_x[1], num_x)[1:-1]:
		for j in np.linspace(range_y[0], range_y[1], num_y)[1:-1]:
			results.append((i, j, function.subs({x: i, y: j})))

	return results

function = "(k1)/(k1+2*k2)"
symbols = "k1 k2"
range_k1 = [5, 10]
range_k2 = [0, 2]
num_k1 = 100
num_k2 = 100

points = samplePoints(range_k1, num_k1, range_k2, num_k2, function, symbols)
probs = column(points, 2)

normalisation = True

pic = svg.Picture(*range_k1, *range_k2)
pic.load_points(points, max(probs), min(probs), normalisation)
pic.save("out.svg")