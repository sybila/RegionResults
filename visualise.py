import libs
import sys
import itertools


'''
python3 visualise.py <Storm-output-in-a-file> <output-html-file>

Example:
    python3 visualise.py example/storm_stdout.txt picture.html
'''
if __name__ == '__main__':
    filename = sys.argv[-2]
    output_location = sys.argv[-1]

    parser = libs.parsing.Parser()
    parser.parse_file(filename)

    # print start
    f = open(output_location, "w")
    f.write(libs.html.HTML_start)

    for (x, y) in itertools.permutations(parser.params, 2):
        bounds = libs.region.get_bounds(parser.regions, x, y)

        pic = libs.svg.Picture(bounds)
        pic.load_rectangles(parser.regions, x, y)
        # print vars
        f.write('\t\t\tvar {}_{} = "data:image/svg+xml;utf8,{}"\n'.format(x, y, pic))
        pic.save("out_{}_{}.svg".format(x, y))

    # print mid
    f.write(libs.html.HTML_mid)
    f.write(libs.html.HTML_x_axis)

    # print x-axis options
    f.write(libs.html.print_option(parser.params[0], True))
    for param in parser.params[1:]:
        f.write(libs.html.print_option(param))

    f.write(libs.html.HTML_y_axis)
    f.write(libs.html.print_option(parser.params[0]))
    f.write(libs.html.print_option(parser.params[1], True))
    for param in parser.params[2:]:
        f.write(libs.html.print_option(param))

    # print end
    f.write(libs.html.HTML_end)
