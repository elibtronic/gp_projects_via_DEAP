###
##
##
#  This program will
#	- generate the 512 x 512 image maps for the best 2 GPs found
#	for each texture
#
#	- draw out according to:
#	- greeen: true positive
#	- black: true negative
#	- red: false positive
#	- yellow: false postive
#
#

from scipy.misc import imread,imsave
import numpy as np

pUsed = imread("brodatz/brodatz2x2.png")

pTrain = np.zeros([512,512,3], dtype=np.uint8)
pTrain.fill(255)

print "Texture 1 points"
for points in open("testing_points/q1_points.txt"):
	
	x = int(points.split(",")[0].strip("\n")) -1
	y = int(points.split(",")[1].strip("\n")) -1
	
	if x <= 0:
		x = 0
	if y <= 0:
		y = 0
	
	pTrain[x][y] = [175,0,255]

print "Texture 2 points"
for points in open("testing_points/q2_points.txt"):
	
	x = int(points.split(",")[0].strip("\n")) -1
	y = int(points.split(",")[1].strip("\n")) -1
	
	if x <= 0:
		x = 0
	if y <= 0:
		y = 0
	
	pTrain[x][y] = [175,0,255]

print "Texture 3 points"
for points in open("testing_points/q3_points.txt"):
	
	x = int(points.split(",")[0].strip("\n")) -1
	y = int(points.split(",")[1].strip("\n")) -1
	
	if x <= 0:
		x = 0
	if y <= 0:
		y = 0
	
	pTrain[x][y] = [175,0,255]

print "Texture 4 points"
for points in open("testing_points/q4_points.txt"):
	
	x = int(points.split(",")[0].strip("\n")) -1
	y = int(points.split(",")[1].strip("\n")) -1
	
	if x <= 0:
		x = 0
	if y <= 0:
		y = 0
	
	pTrain[x][y] = [175,0,255]


imsave("images/final.png",pTrain)
