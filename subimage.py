#subimage converter from detected matrix

def getsubimg(rows,cols,rwidth,cwidth):
	import cv2
	import numpy as np
	from PIL import Image
	image=Image.open('/home/manthan/cropped1.jpg')
	image=image.convert('L')
	image=np.array(image)


	k=0
	image=Image.fromarray(image)
	for i in range(cols):
	    cropimg=image.crop((i*cwidth,0,(i+1)*cwidth,rows*50))
	    cropimg.save(('/home/manthan/subimages/cell'+str(k)+".jpg"))
	    k=k+1


	for j in range(cols):
	    image=Image.open('/home/manthan/subimages/cell'+str(j)+'.jpg')
	    image=image.convert('L')
	    image=np.array(image)
	    size=image.shape
	    image=Image.fromarray(image)
	    for i in range(rows):
		cropimg=image.crop((0,i*rwidth,cwidth,(i+1)*rwidth))
		cropimg.save(('/home/manthan/subimages/subcells/cell'+str(j)+':'+str(i)+".jpg"))
