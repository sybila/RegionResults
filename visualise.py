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

    for (x, y) in itertools.permutations(parser.params, 2):
        bounds = get_bounds(parser.regions, x, y)

        pic = libs.svg.Picture(bounds)
        pic.load_rectangles(parser.regions, x, y)
        print(pic)

        # print vars
        # pic.save(output_location + "out_{}_{}.svg".format(x, y))

    # print options

    # print end

HTML_start = """
<html>
<head>
  <title>Select Image</title>

    <script type="text/javascript">
  function loadImage() {
    x_axis = document.getElementById("x_axis")
    y_axis = document.getElementById("y_axis")

    var svg_name = x_axis.value.concat("_", y_axis.value)
    console.log(svg_name)

    fillImage(svg_name)

  }
  </script>

  <script type="text/javascript">
  function optionChanged(elem) {
    x_axis = document.getElementById("x_axis")
    y_axis = document.getElementById("y_axis")

    if (x_axis.value == y_axis.value){
    	if (elem.id == "x_axis"){
    		var index = y_axis.selectedIndex;
    		if (index + 1 >= y_axis.options.length){
    			y_axis.value = y_axis.options.item(0).value;
    		} else {
    			y_axis.value = y_axis.options.item(index + 1).value;
    		}
    	} else {
    		var index = x_axis.selectedIndex;
    		if (index + 1 >= x_axis.options.length){
    			x_axis.value = x_axis.options.item(0).value;
    		} else {
    			x_axis.value = x_axis.options.item(index + 1).value;
    		}
    	}
    }

    console.log(x_axis.value, y_axis.value)

    var svg_name = x_axis.value.concat("_", y_axis.value)

    fillImage(svg_name)

  }
  </script>

  <script type="text/javascript">
  function fillImage(svg_name) {
    var image = document.getElementById("plot");
"""

# var p_q = "data:image/svg+xml;utf8,<svg width='620' height='200' xmlns='http://www.w3.org/2000/svg'> <rect x='135' y='140' width='25' height='25' fill='green' /> </svg>"
#
# var q_p = "data:image/svg+xml;utf8,<svg width='620' height='200' xmlns='http://www.w3.org/2000/svg'> <rect x='135' y='140' width='25' height='25' fill='red' /> </svg>"
#
# var p_r = "data:image/svg+xml;utf8,<svg width='620' height='200' xmlns='http://www.w3.org/2000/svg'> <rect x='135' y='140' width='25' height='25' fill='blue' /> </svg>"
#
# var r_p = "data:image/svg+xml;utf8,<svg width='620' height='200' xmlns='http://www.w3.org/2000/svg'> <rect x='135' y='140' width='25' height='25' fill='orange' /> </svg>"
#
# var q_r = "data:image/svg+xml;utf8,<svg width='620' height='200' xmlns='http://www.w3.org/2000/svg'> <rect x='135' y='140' width='25' height='25' fill='yellow' /> </svg>"
#
# var r_q = "data:image/svg+xml;utf8,<svg width='620' height='200' xmlns='http://www.w3.org/2000/svg'> <rect x='135' y='140' width='25' height='25' fill='black' /> </svg>"

HTML_mid = """
    image.src = eval(svg_name);
  }
  </script>
</head>
<body onload="loadImage()">

<img id="plot">
"""

HTML_x_axis = """
"<label for="x_axis">X-axis</label>
<select id="x_axis" onchange="optionChanged(this);">
"""
# <option value="p" selected>p</option>
# <option value="q">q</option>
# <option value="r">r</option>

HTML_y_axis = """
</select>

<label for="y_axis">Y-axis</label>
<select id="y_axis" onchange="optionChanged(this);">
"""
# <option value="p">p</option>
# <option value="q" selected>q</option>
# <option value="r">r</option>

HTML_end = """
</select>

</body>
</html>"""
