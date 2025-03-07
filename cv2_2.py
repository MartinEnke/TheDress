
import cv2
import numpy as np
import matplotlib.pyplot as plt
import requests

USE_LOCAL_IMAGE = True

if USE_LOCAL_IMAGE:
    image_path = "The_dress_blueblackwhitegold.jpg"
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load the image from {image_path}")
        exit()
else:
    url = "https://upload.wikimedia.org/wikipedia/en/e/e7/The_dress_blueblackwhitegold.jpg"
    response = requests.get(url)
    if response.status_code == 200:
        image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    else:
        print("Error: Could not download the image.")
        exit()

# convert to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


plt.imshow(image)
plt.axis('off')
plt.show()

# Avg color
average_color = np.mean(image, axis=(0, 1))
print("Average Color (RGB):", average_color)

