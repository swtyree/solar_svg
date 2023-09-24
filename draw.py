import math
from pathlib import Path

import drawsvg as draw

# initialize drawing
d = draw.Drawing(1000, 1000, origin="center")

# set white background
d.append(draw.Rectangle(-500, -500, 1000, 1000, fill="white", stroke_width=0))

# set up each body
solar_system = [
    {"name": "Sun", "radius": 0.55, "distance": 0.0, "x": 0.0, "y": 0.0},
    {"name": "Mercury", "radius": 0.07, "distance": 1.2**0, "x": -7.0, "y": 5.0},
    {"name": "Venus", "radius": 0.12, "distance": 1.2**1, "x": -1.0, "y": -1.0},
    {"name": "Earth", "radius": 0.12, "distance": 1.2**2, "x": 0, "y": 1.0},
    {"name": "Mars", "radius": 0.08, "distance": 1.2**3, "x": 2.0, "y": 1.0},
    {"name": "Asteroid Belt", "radius": None, "distance": 1.2**4, "x": 1.0, "y": 1.0},
    {"name": "Jupiter", "radius": 0.24, "distance": 1.2**5, "x": 1.0, "y": 1.0},
    {"name": "Saturn", "radius": 0.2, "distance": 1.2**6, "x": 1.0, "y": -1.0},
    {
        "name": "Saturn's Rings",
        "radius": 0.22 * 1.3,
        "distance": 1.2**6,
        "x": 1.0,
        "y": -1.0,
    },
    {"name": "Uranus", "radius": 0.17, "distance": 1.2**7, "x": 0.0, "y": 1.0},
    {"name": "Neptune", "radius": 0.17, "distance": 1.2**8, "x": -1.0, "y": -1.0},
]

# draw each body
idx = 0
for body in solar_system:
    # get distance
    distance = 115 * body["distance"] - 40
    idx += 1 if body["name"] != "Saturn" else 0

    # draw orbit
    if body["distance"] and body["name"] not in ["Sun", "Saturn's Rings"]:
        d.append(
            draw.Circle(
                0,
                0,
                distance,
                fill="none",
                stroke_width=3.0,
                stroke="black",
                stroke_dasharray="10,5" if body["name"] == "Asteroid Belt" else None,
                stroke_linecap="round",
            ),
        )

    # draw body
    if body["radius"]:
        # normalize x, y
        x, y = body["x"], body["y"]
        if body["name"] != "Sun":
            __r = math.sqrt(x**2 + y**2)
            x, y = x / __r, y / __r

        # draw
        d.append(
            draw.Circle(
                distance * x,
                distance * -y,
                100 * body["radius"],
                fill="black" if not body["name"] == "Saturn's Rings" else "none",
                stroke_width=0 if not body["name"] == "Saturn's Rings" else 11,
                stroke="black" if body["name"] == "Saturn's Rings" else "none",
            ),
        )


# save output
output_fn = Path("solar_system.svg")
d.save_png(str(output_fn))
print(f"Saved to {output_fn}")
try:
    output_fn_png = Path("solar_system.png")
    d.save_svg(str(output_fn_png))
    print(f"Saved to {output_fn_png}")
except Exception as e:
    print("Could not save to png.")
    print(e)
