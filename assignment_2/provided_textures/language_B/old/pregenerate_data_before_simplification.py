
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
import pickle

from filter_functions import *
from scipy.misc import *

#generates the testing points into 4 pickles and text files of coordinates
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
	
	print "Generating Testing Points"
	quad1_file = open("testing_points/q1_points.txt","w")
	for rp in range(0,int( (512 * 512) * quad1Percent)):
		x = str(random.randint(0,256))
		y = str(random.randint(0,256))
		quad1_file.write(x + "," + y + "\n")
		q1.append([int(x),int(y)])
	quad1_file.close()
	pickle.dump(q1, open("testing_points/q1.pkl", "wb"))

	quad2_file = open("testing_points/q2_points.txt","w")
	for rp in range(0,int( (512 * 512) * quad2Percent)):
		x = str(random.randint(0,256))
		y = str(random.randint(0,256))
		quad2_file.write(x + "," + y + "\n")
		q2.append([int(x),int(y)])
	quad2_file.close()
	pickle.dump(q2, open("testing_points/q2.pkl", "wb"))

	quad3_file = open("testing_points/q3_points.txt","w")
	for rp in range(0,int( (512 * 512) * quad3Percent)):
		x = str(random.randint(0,256))
		y = str(random.randint(0,256))
		quad3_file.write(x + "," + y + "\n")
		q3.append([int(x),int(y)])
	quad3_file.close()
	pickle.dump(q3, open("testing_points/q3.pkl", "wb"))

	quad4_file = open("testing_points/q4_points.txt","w")
	for rp in range(0,int( (512 * 512) * quad4Percent)):
		x = str(random.randint(0,256))
		y = str(random.randint(0,256))
		quad4_file.write(x + "," + y + "\n")
		q4.append([int(x),int(y)])
	quad4_file.close()
	pickle.dump(q4, open("testing_points/q4.pkl", "wb"))
	print "Done"
	return q1, q2, q3, q4

####
###
#
# This will pre compute the filter results and save them as pickles for use by 
# the main program when evolving the GP
def gen_filter_data(q1,q2,q3,q4,t1,t2,t3,t4):
	
	# retrieve these values from the pickles
	# Pre Calculate AVG3 scores for the 4 textures
	q1_avg3 = []
	q2_avg3 = []
	q3_avg3 = []
	q4_avg3 = []
	# Pre Calculate STD3 scores for each of the 4 texture
	q1_std3 = []
	q2_std3 = []
	q3_std3 = []
	q4_std3 = []
	# Pre Calculate MIN3 scores for each of the 4 texture
	q1_min3 = []
	q2_min3 = []
	q3_min3 = []
	q4_min3 = []
	# Pre Calculate MAX3 scores for each of the 4 texture
	q1_max3 = []
	q2_max3 = []
	q3_max3 = []
	q4_max3 = []

	#Pre Calculate AVG5 scores
	q1_avg5 = []
	q2_avg5 = []
	q3_avg5 = []
	q4_avg5 = []
	#Pre Calculate STD5 scores
	q1_std5 = []
	q2_std5 = []
	q3_std5 = []
	q4_std5 = []
	#Pre Calculate MIN5 scores
	q1_min5 = []
	q2_min5 = []
	q3_min5 = []
	q4_min5 = []
	#Pre Calculate MAX5 scores
	q1_max5 = []
	q2_max5 = []
	q3_max5 = []
	q4_max5 = []

	#Pre Calculate AVG7 scores
	q1_avg7 = []
	q2_avg7 = []
	q3_avg7 = []
	q4_avg7 = []
	#Pre Calculate STD7 scores
	q1_std7 = []
	q2_std7 = []
	q3_std7 = []
	q4_std7 = []
	#Pre Calculate MIN7 scores
	q1_min7 = []
	q2_min7 = []
	q3_min7 = []
	q4_min7 = []
	#Pre Calculate MAX7 scores
	q1_max7 = []
	q2_max7 = []
	q3_max7 = []
	q4_max7 = []

	#Pre Calculate AVG9 scores
	q1_avg9 = []
	q2_avg9 = []
	q3_avg9 = []
	q4_avg9 = []
	#Pre Calculate STD9 scores
	q1_std9 = []
	q2_std9 = []
	q3_std9 = []
	q4_std9 = []
	#Pre Calculate MIN9 scores
	q1_min9 = []
	q2_min9 = []
	q3_min9 = []
	q4_min9 = []
	#Pre Calculate MAX9 scores
	q1_max9 = []
	q2_max9 = []
	q3_max9 = []
	q4_max9 = []
	
	
	
	
	
	
	print "Pre-Calculating scores for filters"
	print ".Texture 1"
	for q in q1:
		q1_avg3.append(f_avg(3,q[0],q[1],t1))
		q1_std3.append(f_std(3,q[0],q[1],t1))
		q1_min3.append(f_min(3,q[0],q[1],t1))
		q1_max3.append(f_min(3,q[0],q[1],t1))
		
		q1_avg5.append(f_avg(5,q[0],q[1],t1))
		q1_std5.append(f_std(5,q[0],q[1],t1))
		q1_min5.append(f_min(5,q[0],q[1],t1))
		q1_max5.append(f_min(5,q[0],q[1],t1))

		q1_avg7.append(f_avg(7,q[0],q[1],t1))
		q1_std7.append(f_std(7,q[0],q[1],t1))
		q1_min7.append(f_min(7,q[0],q[1],t1))
		q1_max7.append(f_min(7,q[0],q[1],t1))
		
		q1_avg9.append(f_avg(9,q[0],q[1],t1))
		q1_std9.append(f_std(9,q[0],q[1],t1))
		q1_min9.append(f_min(9,q[0],q[1],t1))
		q1_max9.append(f_min(9,q[0],q[1],t1))
		
	pickle.dump(q1_avg3, open("filter_values/q1_avg3.pkl", "wb"))
	pickle.dump(q1_std3, open("filter_values/q1_std3.pkl", "wb"))
	pickle.dump(q1_min3, open("filter_values/q1_min3.pkl", "wb"))
	pickle.dump(q1_max3, open("filter_values/q1_max3.pkl", "wb"))
	
	pickle.dump(q1_avg5, open("filter_values/q1_avg5.pkl", "wb"))
	pickle.dump(q1_std5, open("filter_values/q1_std5.pkl", "wb"))
	pickle.dump(q1_min5, open("filter_values/q1_min5.pkl", "wb"))
	pickle.dump(q1_max5, open("filter_values/q1_max5.pkl", "wb"))	
		
	pickle.dump(q1_avg7, open("filter_values/q1_avg7.pkl", "wb"))
	pickle.dump(q1_std7, open("filter_values/q1_std7.pkl", "wb"))
	pickle.dump(q1_min7, open("filter_values/q1_min7.pkl", "wb"))
	pickle.dump(q1_max7, open("filter_values/q1_max7.pkl", "wb"))		
		
	pickle.dump(q1_avg3, open("filter_values/q1_avg3.pkl", "wb"))
	pickle.dump(q1_std3, open("filter_values/q1_std3.pkl", "wb"))
	pickle.dump(q1_min3, open("filter_values/q1_min3.pkl", "wb"))
	pickle.dump(q1_max3, open("filter_values/q1_max3.pkl", "wb"))		
		
		
	print ".Texture 2"
	for q in q2:
		q2_avg3.append(f_avg(3,q[0],q[1],t2))
		q2_std3.append(f_std(3,q[0],q[1],t2))
		q2_min3.append(f_min(3,q[0],q[1],t2))
		q2_max3.append(f_min(3,q[0],q[1],t2))
		
		q2_avg5.append(f_avg(5,q[0],q[1],t2))
		q2_std5.append(f_std(5,q[0],q[1],t2))
		q2_min5.append(f_min(5,q[0],q[1],t2))
		q2_max5.append(f_min(5,q[0],q[1],t2))

		q2_avg7.append(f_avg(7,q[0],q[1],t2))
		q2_std7.append(f_std(7,q[0],q[1],t2))
		q2_min7.append(f_min(7,q[0],q[1],t2))
		q2_max7.append(f_min(7,q[0],q[1],t2))
		
		q2_avg9.append(f_avg(9,q[0],q[1],t2))
		q2_std9.append(f_std(9,q[0],q[1],t2))
		q2_min9.append(f_min(9,q[0],q[1],t2))
		q2_max9.append(f_min(9,q[0],q[1],t2))

	print ".Texture 3"	
	for q in q3:
		q3_avg3.append(f_avg(3,q[0],q[1],t3))
		q3_std3.append(f_std(3,q[0],q[1],t3))
		q3_min3.append(f_min(3,q[0],q[1],t3))
		q3_max3.append(f_min(3,q[0],q[1],t3))
		
		q3_avg5.append(f_avg(5,q[0],q[1],t3))
		q3_std5.append(f_std(5,q[0],q[1],t3))
		q3_min5.append(f_min(5,q[0],q[1],t3))
		q3_max5.append(f_min(5,q[0],q[1],t3))

		q3_avg7.append(f_avg(7,q[0],q[1],t3))
		q3_std7.append(f_std(7,q[0],q[1],t3))
		q3_min7.append(f_min(7,q[0],q[1],t3))
		q3_max7.append(f_min(7,q[0],q[1],t3))
		
		q3_avg9.append(f_avg(9,q[0],q[1],t3))
		q3_std9.append(f_std(9,q[0],q[1],t3))
		q3_min9.append(f_min(9,q[0],q[1],t3))
		q3_max9.append(f_min(9,q[0],q[1],t3))

	print ".Texture 4"
	for q in q4:
		q4_avg3.append(f_avg(3,q[0],q[1],t4))
		q4_std3.append(f_std(3,q[0],q[1],t4))
		q4_min3.append(f_min(3,q[0],q[1],t4))
		q4_max3.append(f_min(3,q[0],q[1],t4))
		
		q4_avg5.append(f_avg(5,q[0],q[1],t4))
		q4_std5.append(f_std(5,q[0],q[1],t4))
		q4_min5.append(f_min(5,q[0],q[1],t4))
		q4_max5.append(f_min(5,q[0],q[1],t4))

		q4_avg7.append(f_avg(7,q[0],q[1],t4))
		q4_std7.append(f_std(7,q[0],q[1],t4))
		q4_min7.append(f_min(7,q[0],q[1],t4))
		q4_max7.append(f_min(7,q[0],q[1],t4))
		
		q4_avg9.append(f_avg(9,q[0],q[1],t4))
		q4_std9.append(f_std(9,q[0],q[1],t4))
		q4_min9.append(f_min(9,q[0],q[1],t4))
		q4_max9.append(f_min(9,q[0],q[1],t4))


if __name__ == "__main__":
	
	param_config = ConfigParser.ConfigParser()
	param_config.read("paramset.txt")

	t1n = str(param_config.get("textureFiles","texture1"))
	t2n = str(param_config.get("textureFiles","texture2"))
	t3n = str(param_config.get("textureFiles","texture3"))
	t4n = str(param_config.get("textureFiles","texture4"))

	t1 = imread(t1n)
	t2 = imread(t2n)
	t3 = imread(t3n)
	t4 = imread(t4n)
		
	q1, q2, q3, q4 = generate_testing_points()
	#gen_filter_data(q1,q2,q3,q4,t1,t2,t3,t4)
