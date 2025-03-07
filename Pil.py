from PIL import Image

image = Image.open("The_dress_blueblackwhitegold.jpg")
image.show()


# Get dominant colors
from collections import Counter

pixels = list(image.getdata())
most_common_colors = Counter(pixels).most_common(5)
print("Most Common Colors:", most_common_colors)
