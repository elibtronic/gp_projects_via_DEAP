##
# Visually draw out the training points on the 4 textures to see how they
# look
#

from scipy.misc import imread,imsave
import numpy as np
import pickle


pTrain = np.zeros([512,512,3], dtype=np.uint8)
pTrain.fill(255)

print "Texture 1 points"
for p in pickle.load(open( "training_points/q1.pkl", "rb" )):
	
	x = p[0]
	y = p[1]
	
	pTrain[x][y] = [175,0,255]
	
print "Texture 2 points"
for p in pickle.load(open( "training_points/q2.pkl", "rb" )):
	
	x = p[0]
	y = p[1] + 255 
	

	pTrain[x][y] = [175,0,255]
	
print "Texture 3 points"
for p in pickle.load(open( "training_points/q3.pkl", "rb" )):
	
	x = p[0] + 255
	y = p[1] 
	

	pTrain[x][y] = [175,0,255]
	
print "Texture 4 points"
for p in pickle.load(open( "training_points/q4.pkl", "rb" )):
	
	x = p[0] + 255
	y = p[1] + 255
	

	pTrain[x][y] = [175,0,255]
	
imsave("images/training_points.png",pTrain)
