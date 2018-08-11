import numpy as np
import cv2

image = cv2.imread('boruto.jpg')


print(cv2.add(np.uint8([200]), np.uint8 ([100])))
print(cv2.subtract(np.uint8([50]), np.uint8 ([100]))) 

#wrap around
print(np.uint8([200]) + np.uint8 ([100]))
print(np.uint8([50]) - np.uint8 ([100])) 

M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)

M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)
cv2.destroyAllWindows()
