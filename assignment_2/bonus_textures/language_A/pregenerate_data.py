###
##
##
# This pre-calculates all the sampling points for the 4 different textures
# (points aren't necessarily unique)
# All pre-calculates the results of the image filter maps
# Everything is saved as binary blob (Python Pickle) to be used
# by the GP

import ConfigParser
import random
import pickle

from filter_functions import *
from scipy.misc import *

#generates the training points into 4 pickles and text files of coordinates
def generate_training_points():
	param_config = ConfigParser.ConfigParser()
	param_config.read("paramset.txt")
	quad1Percent = float(param_config.get("PointGen","quad1Percent")) / 100
	quad2Percent = float(param_config.get("PointGen","quad2Percent")) / 100
	quad3Percent = float(param_config.get("PointGen","quad3Percent")) / 100
	quad4Percent = float(param_config.get("PointGen","quad4Percent")) / 100
	pointSeed = int(param_config.get("PointGen","pointSeed"))
	random.seed(pointSeed)
	
	q1 = list()
	q2 = list()
	q3 = list()
	q4 = list()
	
	quad1_file = open("training_points/q1_points.txt","w")
	for rp in range(0,int( (256 * 256) * quad1Percent)):
		x = str(random.randint(0,256))
		y = str(random.randint(0,256))
		quad1_file.write(x + "," + y + "\n")
		q1.append([int(x),int(y)])
	quad1_file.close()
	pickle.dump(q1, open("training_points/q1.pkl", "wb"))

	quad2_file = open("training_points/q2_points.txt","w")
	for rp in range(0,int( (256 * 256) * quad2Percent)):
		x = str(random.randint(0,256))
		y = str(random.randint(0,256))
		quad2_file.write(x + "," + y + "\n")
		q2.append([int(x),int(y)])
	quad2_file.close()
	pickle.dump(q2, open("training_points/q2.pkl", "wb"))

	quad3_file = open("training_points/q3_points.txt","w")
	for rp in range(0,int( (256 * 256) * quad3Percent)):
		x = str(random.randint(0,256))
		y = str(random.randint(0,256))
		quad3_file.write(x + "," + y + "\n")
		q3.append([int(x),int(y)])
	quad3_file.close()
	pickle.dump(q3, open("training_points/q3.pkl", "wb"))

	quad4_file = open("training_points/q4_points.txt","w")
	for rp in range(0,int( (256 * 256) * quad4Percent)):
		x = str(random.randint(0,256))
		y = str(random.randint(0,256))
		quad4_file.write(x + "," + y + "\n")
		q4.append([int(x),int(y)])
	quad4_file.close()
	pickle.dump(q4, open("training_points/q4.pkl", "wb"))
	return q1, q2, q3, q4

####
###
#
# This will pre compute the filter results and save them as pickles for use by 
# the main program when evolving the GP
def gen_filter_data(q_in,t_in,label):
	
	q_avg3 = []		#AVG3
	q_std3 = []		#STD3
	q_min3 = []		#MIN3
	q_max3 = []		#MAX3

	q_avg5 = []		#AVG5
	q_std5 = []		#STD5
	q_min5 = []		#MIN5
	q_max5 = []		#MAX5

	q_avg7 = []		#AVG7
	q_std7 = []		#STD7
	q_min7 = []		#MIN7
	q_max7 = []		#MAX7

	q_avg9 = []		#AVG9
	q_std9 = []		#STD9
	q_min9 = []		#MIN9
	q_max9 = []		#MAX9
	
	q_avg11 = []	#AVG11
	q_std11 = []	#STD11
	q_min11 = []	#MIN11
	q_max11 = []	#MAX11
	
	for q in q_in:
		q_avg3.append(f_avg(3,q[0],q[1],t_in))
		q_std3.append(f_std(3,q[0],q[1],t_in))
		q_min3.append(f_min(3,q[0],q[1],t_in))
		q_max3.append(f_min(3,q[0],q[1],t_in))
		
		q_avg5.append(f_avg(5,q[0],q[1],t_in))
		q_std5.append(f_std(5,q[0],q[1],t_in))
		q_min5.append(f_min(5,q[0],q[1],t_in))
		q_max5.append(f_min(5,q[0],q[1],t_in))

		q_avg7.append(f_avg(7,q[0],q[1],t_in))
		q_std7.append(f_std(7,q[0],q[1],t_in))
		q_min7.append(f_min(7,q[0],q[1],t_in))
		q_max7.append(f_min(7,q[0],q[1],t_in))
		
		q_avg9.append(f_avg(9,q[0],q[1],t_in))
		q_std9.append(f_std(9,q[0],q[1],t_in))
		q_min9.append(f_min(9,q[0],q[1],t_in))
		q_max9.append(f_min(9,q[0],q[1],t_in))
		
		q_avg11.append(f_avg(11,q[0],q[1],t_in))
		q_std11.append(f_std(11,q[0],q[1],t_in))
		q_min11.append(f_min(11,q[0],q[1],t_in))
		q_max11.append(f_min(11,q[0],q[1],t_in))
		
	pickle.dump(q_avg3, open("filter_values/q"+label+"_avg3.pkl", "wb"))
	pickle.dump(q_std3, open("filter_values/q"+label+"_std3.pkl", "wb"))
	pickle.dump(q_min3, open("filter_values/q"+label+"_min3.pkl", "wb"))
	pickle.dump(q_max3, open("filter_values/q"+label+"_max3.pkl", "wb"))
	
	pickle.dump(q_avg5, open("filter_values/q"+label+"_avg5.pkl", "wb"))
	pickle.dump(q_std5, open("filter_values/q"+label+"_std5.pkl", "wb"))
	pickle.dump(q_min5, open("filter_values/q"+label+"_min5.pkl", "wb"))
	pickle.dump(q_max5, open("filter_values/q"+label+"_max5.pkl", "wb"))	
		
	pickle.dump(q_avg7, open("filter_values/q"+label+"_avg7.pkl", "wb"))
	pickle.dump(q_std7, open("filter_values/q"+label+"_std7.pkl", "wb"))
	pickle.dump(q_min7, open("filter_values/q"+label+"_min7.pkl", "wb"))
	pickle.dump(q_max7, open("filter_values/q"+label+"_max7.pkl", "wb"))		
		
	pickle.dump(q_avg9, open("filter_values/q"+label+"_avg9.pkl", "wb"))
	pickle.dump(q_std9, open("filter_values/q"+label+"_std9.pkl", "wb"))
	pickle.dump(q_min9, open("filter_values/q"+label+"_min9.pkl", "wb"))
	pickle.dump(q_max9, open("filter_values/q"+label+"_max9.pkl", "wb"))
	
	pickle.dump(q_avg11, open("filter_values/q"+label+"_avg11.pkl", "wb"))
	pickle.dump(q_std11, open("filter_values/q"+label+"_std11.pkl", "wb"))
	pickle.dump(q_min11, open("filter_values/q"+label+"_min11.pkl", "wb"))
	pickle.dump(q_max11, open("filter_values/q"+label+"_max11.pkl", "wb"))		
		

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
		
	print "Generating Training Points"
	q1, q2, q3, q4 = generate_training_points()
	
	print "Pre-Calculating scores for filters"

	print ".Texture 1"
	gen_filter_data(q1,t1,"1")
	print ".Texture 2"
	gen_filter_data(q2,t2,"2")
	print ".Texture 3"
	gen_filter_data(q3,t3,"3")
	print ".Texture 4"		
	gen_filter_data(q4,t4,"4")
