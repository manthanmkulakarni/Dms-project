#main program

import cv2
import numpy as np
from PIL import Image
import crop
import subimage
import medgedet
import math

n=6
m=3
rows=n-m
cols=n
rwidth=50
cwidth=50
imgpath='/home/manthan/given.jpg'

medgedet.treshold(imgpath)

crop.cropm(imgpath,rows,cols,rwidth,cwidth)

subimage.getsubimg(rows,cols,rwidth,cwidth)

ar=np.zeros((rows,cols))
for i in range(rows):
    for j in range(cols):
        img = cv2.imread(('/home/manthan/subimages/subcells/cell'+str(j)+':'+str(i)+'.jpg'),0)
        img = cv2.medianBlur(img,5)
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,95,param1=15,param2=23,minRadius=1,maxRadius=0)
        if circles is None:
            ar[i][j]=1
ar=ar.astype(int)
for j in range(n-m):
    for i in range(m,n):
	if((i-3)==j):
	    ar[j][i]=1
	else:
	    ar[j][i]=0

print "The given Parity check matrix \nH= "+str(ar)



A=ar.T[:m]
two=np.full((1,n),2)


#To get agumented matrix  [A|I]
i=np.identity(m,dtype=int)
#Generator matrix
g=i
g=np.concatenate((g,np.array(A)),axis=1)

print "The generator matrix [A|I] is:"
print "G= "+str(g)

size=int(math.pow(2,m))
M=np.full((size,m),0)
C=np.full((size,n),0)

#To generate all combinations for message word  

for i in range(size):
    binary=(np.binary_repr(i,width=m))
    for j in range(m):
        M[i][j]=int(binary[j])
        
print "\nThe code words for the given message words\n"
for i in range(size):
    C[i]=np.dot(M[i],g)    #generating the codewords
    C[i]=np.remainder(C[i],two)
    print ("E("+str(M[i])+")---->"+str(C[i]))
    



