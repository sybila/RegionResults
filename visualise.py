import libs
import sys
import itertools


def get_bounds(regions, x, y):
    x_max = max(list(map(lambda result: result.projection(x)[1], regions)))
    y_max = max(list(map(lambda result: result.projection(y)[1], regions)))

    x_min = min(list(map(lambda result: result.projection(x)[0], regions)))
    y_min = min(list(map(lambda result: result.projection(y)[0], regions)))

    return {"x_min": x_min, "x_max": x_max, "y_min": y_min, "y_max": y_max}


'''
python3 visualise.py <Storm-output-in-a-file> <output-svg-file>

Example:
    python3 visualise.py example/storm_stdout.txt picture.svg
'''
if __name__ == '__main__':
    filename = sys.argv[-2]
    output_location = sys.argv[-1]

    parser = libs.parsing.Parser()
    parser.parse_file(filename)

    for (x,y) in itertools.permutations(parser.params, 2):
        bounds = get_bounds(parser.regions, x, y)

        pic = libs.svg.Picture(bounds)
        pic.load_rectangles(parser.regions, x, y)
        pic.save(output_location + "out_{}_{}.svg".format(x, y))
