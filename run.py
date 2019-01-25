import svg
import parsing
import sys

def get_max_results(regions):
	width = max(list(map(lambda result: result.get_max_x(), regions)))
	height = max(list(map(lambda result: result.get_max_y(), regions)))
	return width, height

filename = sys.argv[-2]
output_name = sys.argv[-1]

parser = parsing.Parser()
parser.parse_file(filename)

width, height = get_max_results(parser.regions)

pic = svg.Picture(width, height)
pic.load_rectangles(parser.regions)
pic.save(output_name)