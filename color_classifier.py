from flask import Flask, request

app = Flask(__name__)

# A function to classify RGB hex color into the given categories
def classify_color(hex_color):
    hex_color = hex_color.lstrip('#')  # Remove '#' if present
    if len(hex_color) != 6:
        return "invalid"  # Handle invalid input
    try:
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    except ValueError:
        return "invalid"
    # Color classification logic
    if r > 200 and g < 100 and b < 100:
        return "red"
    elif r > 200 and g > 150 and b < 50:
        return "orange"
    elif r > 200 and g > 200 and b < 50:
        return "yellow"
    elif r < 100 and g > 200 and b < 100:
        return "green"
    elif r < 100 and g < 100 and b > 200:
        return "blue"
    elif r > 40 and g < 200 and b > 70:
        return "violet"
    elif r > 120 and g < 100 and b > 100:
        return "pink"
    elif (r > 40 and r < 180) and abs(g - b) < 20:
        return "brown"
    elif r > 200 and g > 200 and b > 200:
        return "white"
    elif r < 50 and g < 50 and b < 50:
        return "black"
    elif abs(r - g) < 20 and abs(g - b) < 20:
        return "grey"
    else:
        return "unknown"

@app.route('/<hex_color>')
def classify(hex_color):
    color_name = classify_color(hex_color)
    return color_name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
