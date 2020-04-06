import libs
import sys
import itertools
import numpy as np


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

    # lin spaces of admissible values for all parameters
    spaced_dims = {key: np.linspace(parser.bounds[key][0], parser.bounds[key][1], 10) for key in parser.params}

    if len(parser.params) <= 2:
        f.write(libs.html.HTML_start_2d)
    else:
        f.write(libs.html.HTML_start_more_d_1)
        f.write("\t\t\tvar dims = {}\n".format(["dim_{}".format(i) for i in range(len(parser.params) - 2)]))
        f.write("\t\t\tvar params = {}\n".format(parser.params))
        for param in spaced_dims:
            f.write("\t\t\tvar {} = {}\n".format(param, list(spaced_dims[param])))
        f.write(libs.html.HTML_start_more_d_2)
        f.write("\t\t\tvar dims = {}".format(["dim_{}".format(i) for i in range(len(parser.params) - 2)]))
        f.write(libs.html.HTML_start_more_d_3)

    for (x, y) in itertools.permutations(parser.params, 2):
        bounds = parser.get_bounds(x, y)

        # extract all other dimensions
        other_dims = {param: parser.bounds[param] for param in parser.bounds.keys() - {x, y}}
        if other_dims:
            # ordered parameter names
            ordered_params = sorted(other_dims)
            # prepare possible positions for all params
            position_dims = {key: list(range(10)) for key in other_dims.keys()}
            # combinations of all positions of all params
            combinations = itertools.product(*(position_dims[name] for name in ordered_params))

            # values correspond to param names in  ordered_names
            for values in combinations:
                dims = {ordered_params[i]: values[i] for i in range(len(ordered_params))}
                dims_values = {param: spaced_dims[param][dims[param]] for param in ordered_params}

                dims_label = "_".join([param + "_" + str(dims[param]) for param in dims])

                pic = libs.svg.Picture(bounds)
                pic.load_rectangles(parser.regions, x, y, dims_values)
                # print vars
                f.write('\t\t\tvar {}_{}_{} = "data:image/svg+xml;utf8,{}"\n'.format(x, y, dims_label, pic))
        else:
            pic = libs.svg.Picture(bounds)
            pic.load_rectangles(parser.regions, x, y, dict())
            # print vars
            f.write('\t\t\tvar {}_{} = "data:image/svg+xml;utf8,{}"\n'.format(x, y, pic))

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
    f.write(libs.html.HTML_end_1)

    # print other dimensions
    if len(parser.params) > 2:
        f.write(libs.html.HTML_other_dim)
        for i in range(len(parser.params) - 2):
            f.write(libs.html.HTML_dim_options.format(i, parser.params[i+2]))
            values = spaced_dims[parser.params[i+2]]
            for j in range(len(values)):
                f.write(libs.html.print_fixed_option(j, values[j]))
            f.write(libs.html.HTML_dim_options_end)

    # print end
    f.write(libs.html.HTML_end_2)
