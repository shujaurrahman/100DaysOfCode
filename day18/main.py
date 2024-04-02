import colorgram

colors=colorgram.extract("/Users/shujaurrahman/Desktop/Coding/100daysofcode/day18/image.jpg",30)
rgb_colors=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)
