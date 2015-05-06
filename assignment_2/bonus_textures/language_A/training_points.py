
#
# This will generate specified percentage amount of points in all four
# images to be used for training
# writes our results into text files

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
	for rp in range(0,int( (512 * 512) * quad1Percent)):
		x = str(random.randint(0,256))
		y = str(random.randint(0,256))
		quad1_file.write(x + "," + y + "\n")
		q1.append([int(x),int(y)])
	quad1_file.close()

	quad2_file = open("testing_points/q2_points.txt","w")
	for rp in range(0,int( (512 * 512) * quad2Percent)):
		x = str(random.randint(0,256))
		y = str(random.randint(0,256))
		quad2_file.write(x + "," + y + "\n")
		q2.append([int(x),int(y)])
	quad2_file.close()

	quad3_file = open("testing_points/q3_points.txt","w")
	for rp in range(0,int( (512 * 512) * quad3Percent)):
		x = str(random.randint(0,256))
		y = str(random.randint(0,256))
		quad3_file.write(x + "," + y + "\n")
		q3.append([int(x),int(y)])
	quad3_file.close()

	quad4_file = open("testing_points/q4_points.txt","w")
	for rp in range(0,int( (512 * 512) * quad4Percent)):
		x = str(random.randint(0,256))
		y = str(random.randint(0,256))
		quad4_file.write(x + "," + y + "\n")
		q4.append([int(x),int(y)])
	quad4_file.close()

	return q1, q2, q3, q4

