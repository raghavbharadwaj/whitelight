import sys
import os
import cv2
import numpy as np

def changepixel(img,b,g,r):
	height,width,depth = img.shape
	for i in range(0,height):
		for j in range(0,width):
			img[i][j][0]=min(255,img[i][j][0]/b)
			img[i][j][1]=min(255,img[i][j][1]/g)
			img[i][j][2]=min(255,img[i][j][2]/r)
	cv2.imwrite('new_image.bmp',img)
	
def main():
	image = cv2.imread(sys.argv[1])
	blue,red,green = cv2.mean(image)[0:3]
	red = red/128
	sblue= blue/128
	sgreen =green/128
	print(sred)
	print(sblue)
	print(sgreen)
	changepixel(image,sblue,sgreen,sred)
main()

