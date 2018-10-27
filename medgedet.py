#matrix edge detection


def treshold(path):
	import cv2
	import numpy as np
	from PIL import Image
	image = cv2.imread(path)
	#image=image.convert('L')
	image=np.array(image)
	# resize image so it can be processed
	# choose optimal dimensions such that important content is not lost
	shape=image.shape
	image = cv2.resize(image, (800,800) )

	# creating copy of original image
	orig = image.copy()

	# convert to grayscale and blur to smooth
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(image, (3, 3), 0)

	edged = cv2.Canny(blurred, 0, 50)
	th2 = cv2.adaptiveThreshold(edged,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
		    cv2.THRESH_BINARY,11,5)
	th2 = cv2.GaussianBlur(th2, (11, 11), 0)
	th2 = cv2.adaptiveThreshold(th2,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
		    cv2.THRESH_BINARY,51,5)
	edges=Image.fromarray(th2)
	edges.save('/home/manthan/matrixr.jpg')
	edges.show()

