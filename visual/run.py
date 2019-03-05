import svg
import parsing
import sys

def get_max_results(regions):
	w_max = max(list(map(lambda result: result.get_max_x(), regions)))
	h_max = max(list(map(lambda result: result.get_max_y(), regions)))

	w_min = min(list(map(lambda result: result.get_min_x(), regions)))
	h_min = min(list(map(lambda result: result.get_min_y(), regions)))

	return w_min, w_max, h_min, h_max

filename = sys.argv[-2]
output_name = sys.argv[-1]

parser = parsing.Parser()
parser.parse_file(filename)

w_min, w_max, h_min, h_max = get_max_results(parser.regions)

pic = svg.Picture(w_min, w_max, h_min, h_max)
pic.load_rectangles(parser.regions)
pic.save(output_name)