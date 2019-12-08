# https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/

import cv2

img = cv2.imread('d:\\srk_1.jpg')
height = img.shape[0]
width = img.shape[1]

for row in range(0, width):
	for column in range(0, height):
		print(img[column][row])


