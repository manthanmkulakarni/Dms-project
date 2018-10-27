#cropping of detected matrix


def cropm(path,rows,cols,rwidth,cwidth):
	import cv2
	import numpy as np
	from PIL import Image
	def rectify(h):
	    h = h.reshape((4,2))
	    hnew = np.zeros((4,2),dtype = np.float32)

	    add = h.sum(1)
	    hnew[0] = h[np.argmin(add)]
	    hnew[2] = h[np.argmax(add)]

	    diff = np.diff(h,axis = 1)
	    hnew[1] = h[np.argmin(diff)]
	    hnew[3] = h[np.argmax(diff)]

	    return hnew

	image = cv2.imread('/home/manthan/matrixr.jpg')
	#image=image.convert('L')
	image=np.array(image)
	# resize image so it can be processed
	# choose optimal dimensions such that important content is not lost
	shape=image.shape
	image = cv2.resize(image, (800,800) )

	# creating copy of original image
	orig = Image.open(path)
	orig=orig.resize((800,800))
	orig=np.array(orig)

	# convert to grayscale and blur to smooth
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(image, (3, 3), 0)
	#blurred = cv2.medianBlur(gray, 5)

	# apply Canny Edge Detection
	edged = cv2.Canny(blurred, 0, 50)
	orig_edged = edged.copy()

	# find the contours in the edged image, keeping only the
	# largest ones, and initialize the screen contour
	(o,contours, _) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]


	# get approximate contour
	for c in contours:
	    p = cv2.arcLength(c, True)
	    approx = cv2.approxPolyDP(c, 0.02 * p, True)

	    if len(approx) == 4:
		target = approx
		break


	# mapping target points to 800x800 quadrilateral
	approx = rectify(target)
	pts2 = np.float32([[0,0],[800,0],[800,800],[0,800]])

	M = cv2.getPerspectiveTransform(approx,pts2)
	dst = cv2.warpPerspective(orig,M,(800,800))
	outline=Image.fromarray(dst)
	outline=outline.resize((cols*cwidth,rows*rwidth))
	outline.show()
	outline.save("/home/manthan/cropped1.jpg")





