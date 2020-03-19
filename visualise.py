import libs
import sys


def get_max_results(regions):
    w_max = max(list(map(lambda result: result.get_max_x(), regions)))
    h_max = max(list(map(lambda result: result.get_max_y(), regions)))

    w_min = min(list(map(lambda result: result.get_min_x(), regions)))
    h_min = min(list(map(lambda result: result.get_min_y(), regions)))

    return w_min, w_max, h_min, h_max


'''
python3 visualise.py <Storm-output-in-a-file> <output-svg-file>

Example:
    python3 visualise.py example/storm_stdout.txt picture.svg
'''
if __name__ == '__main__':
    filename = sys.argv[-2]
    output_name = sys.argv[-1]

    parser = libs.parsing.Parser()
    parser.parse_file(filename)

    w_min, w_max, h_min, h_max = get_max_results(parser.regions)
    bounds = {"w_min": w_min, "w_max": w_max, "h_min": h_min, "h_max": h_max}

    pic = libs.svg.Picture(bounds)
    pic.load_rectangles(parser.regions, bounds)
    pic.save(output_name)
