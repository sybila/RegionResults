import numpy as np
import sympy
import sys
from sympy.parsing.sympy_parser import parse_expr
import libs

############################

def column(matrix, i):
    return [row[i] for row in matrix]

def samplePoints(function, params, keys):
	x, y = sympy.symbols(" ".join(keys))
	function = parse_expr(function)
	results = []

	for i in np.linspace(*params[keys[0]])[1:-1]:
		for j in np.linspace(*params[keys[1]])[1:-1]:
			results.append((i, j, function.subs({x: i, y: j})))

	return results

'''
python3 sample.py <function-to-sample> <parameters> <output_file> [params order]

where <parameters> is a dictionary of type:
	"param-name" : [From, To, Number]
	which will create a linear space 
	with interval (<From>, <To>) and <Number> samples.

Example:
	python3 sample.py '(k1)/(k1+2*k2)' '{"k1" : [5, 10, 10], "k2" : [0, 2, 10]}' sampling.svg 'k1 k2'
'''
if __name__ == '__main__':
	if len(sys.argv) == 5:
		keys = sys.argv[-1].split()
		output_file = sys.argv[-2]
		params = eval(sys.argv[-3])
		function = sys.argv[-4]
	else:
		output_file = sys.argv[-1]
		params = eval(sys.argv[-2])
		function = sys.argv[-3]
		keys = list(params.keys())

	points = samplePoints(function, params, keys)
	probs = column(points, 2)

	bounds = {"w_min": params[keys[0]][0], "w_max": params[keys[0]][1], 
			  "h_min": params[keys[1]][0], "h_max": params[keys[1]][1]}

	pic = libs.svg.Picture(bounds)
	pic.load_points(points, min(probs), max(probs), bounds)
	pic.save(output_file)