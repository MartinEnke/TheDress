import cv2

image = cv2.imread("The_dress_blueblackwhitegold.jpg")

# Convert to RGB and display
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("The Dress", image)
cv2.waitKey(0)
cv2.destroyAllWindows()




