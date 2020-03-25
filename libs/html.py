def print_option(option, selected=False):
    return "\t<option value='{0}'{1}>{0}</option>\n".format(option, " selected" if selected else "")

HTML_start = """
<html>
<head>
    <title>Select Image</title>

    <script type="text/javascript">
        function loadImage() {
            x_axis = document.getElementById("x_axis")
            y_axis = document.getElementById("y_axis")

            var svg_name = x_axis.value.concat("_", y_axis.value)

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

            var svg_name = x_axis.value.concat("_", y_axis.value)
            fillImage(svg_name)
        }
    </script>

    <script type="text/javascript">
        function fillImage(svg_name) {
            var image = document.getElementById("plot");
"""

HTML_mid = """
            image.src = eval(svg_name);
        }
    </script>
</head>
<body onload="loadImage()">
<img id="plot">
"""

HTML_x_axis = """
<label for="x_axis">X-axis</label>
<select id="x_axis" onchange="optionChanged(this);">
"""

HTML_y_axis = \
"""</select>

<label for="y_axis">Y-axis</label>
<select id="y_axis" onchange="optionChanged(this);">
"""

HTML_end = \
"""</select>

</body>
</html>"""
