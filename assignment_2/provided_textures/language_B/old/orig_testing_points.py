
#
# This will generate specified percentage amount of points in all four
# quandrants of 512 x 512, quartered texture
#
# saves list of these in 'test_points.txt'
# assuming starting topleft 0,0. 
# X increases left to right
# Y increase top to bottom
# points aren't necessarily unique

import ConfigParser
import random

def generate_testing_points():
	param_config = ConfigParser.ConfigParser()
	param_config.read("paramset.txt")
	quad1Percent = float(param_config.get("PointGen","quad1Percent")) / 100
	quad2Percent = float(param_config.get("PointGen","quad2Percent")) / 100
	quad3Percent = float(param_config.get("PointGen","quad3Percent")) / 100
	quad4Percent = float(param_config.get("PointGen","quad4Percent")) / 100
	pointSeed = int(param_config.get("PointGen","pointSeed"))
	random.seed(pointSeed)
	
	q1 = q2 = q3 = q4 = list()
	
	quad1_file = open("testing_points/q1_points.txt","w")
	#Texture 1 between 0,0 256,0
	for rp in range(0,int( (512 * 512) * quad1Percent)):
		x = str(random.randint(0,256))
		y = str(random.randint(0,256))
		quad1_file.write(x + "," + y + "\n")
		q1.append([int(x),int(y)])
	quad1_file.close()

	#Texture 2 between 257,0 512,256
	quad2_file = open("testing_points/q2_points.txt","w")
	for rp in range(0,int( (512 * 512) * quad2Percent)):
		x = str(random.randint(257,512))
		y = str(random.randint(0,256))
		quad2_file.write(x + "," + y + "\n")
		q2.append([int(x),int(y)])
	quad2_file.close()

	#Texture 3 between 0,257 257,512
	quad3_file = open("testing_points/q3_points.txt","w")
	for rp in range(0,int( (512 * 512) * quad3Percent)):
		x = str(random.randint(0,257))
		y = str(random.randint(257,512))
		quad3_file.write(x + "," + y + "\n")
		q3.append([int(x),int(y)])
	quad3_file.close()

	##Texture 4 between 257,257 512,512
	quad4_file = open("testing_points/q4_points.txt","w")
	for rp in range(0,int( (512 * 512) * quad4Percent)):
		x = str(random.randint(257,512))
		y = str(random.randint(257,512))
		quad4_file.write(x + "," + y + "\n")
		q4.append([int(x),int(y)])
	quad4_file.close()

	return q1, q2, q3, q4

