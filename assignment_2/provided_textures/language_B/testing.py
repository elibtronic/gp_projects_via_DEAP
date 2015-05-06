#
# This will iterate through all the GPs found during evolution
# and generate images on the 4 texture grid
# will also calculate confusion matrix data (for testing only) for each of the runs
# 
#

from scipy.misc import imread,imsave
import pickle
import numpy as np

texToFind = 4
seed = 9

#1 true positive
#2 true negative
#3 false postive
#4 false negative

q1 = pickle.load(open("testing/tex"+str(texToFind)+"_"+str(seed)+"_q1.pkl","rb"))
q2 = pickle.load(open("testing/tex"+str(texToFind)+"_"+str(seed)+"_q2.pkl","rb"))
q3 = pickle.load(open("testing/tex"+str(texToFind)+"_"+str(seed)+"_q3.pkl","rb"))
q4 = pickle.load(open("testing/tex"+str(texToFind)+"_"+str(seed)+"_q4.pkl","rb"))

t1_tpoints = pickle.load(open("training_points/q1.pkl","rb"))
t2_tpoints = pickle.load(open("training_points/q2.pkl","rb"))
t3_tpoints = pickle.load(open("training_points/q3.pkl","rb"))
t4_tpoints = pickle.load(open("training_points/q4.pkl","rb"))

t1_image = np.zeros([255,255,3], dtype=np.uint8)
t2_image = np.zeros([255,255,3], dtype=np.uint8)
t3_image = np.zeros([255,255,3], dtype=np.uint8)
t4_image = np.zeros([255,255,3], dtype=np.uint8)

t1_image.fill(255)
t2_image.fill(255)
t3_image.fill(255)
t4_image.fill(255)

#t1_image.reshape(255,255,3)


tp_count = 0
tn_count = 0
fp_count = 0
fn_count = 0

print "Generating texture files and confusion data"

#texture 1
print "Texture 1"
for x in range(255):
	for y in range(255):
		if q1[x][y] == 1.0: 
			t1_image[x][y] = [0,255,0]
			if not [x,y] in t1_tpoints:
				tp_count += 1
		if q1[x][y] == 2.0:
			t1_image[x][y] = [0,0,0]
			if not [x,y] in t1_tpoints:
				tn_count += 1
		if q1[x][y] == 3.0:
			t1_image[x][y] = [255,255,0]
			if not [x,y] in t1_tpoints:
				fp_count += 1
		if q1[x][y] == 4.0:
			t1_image[x][y] = [255,0,0]
			if not [x,y] in t1_tpoints:
				fn_count += 1
imsave("images/textoFind_"+str(texToFind)+"_seed_"+str(seed)+"_t1.png",t1_image)

#texture 2
print "Texture 2"
for x in range(255):
	for y in range(255):
		if q2[x][y] == 1.0: 
			t2_image[x][y] = [0,255,0]
			if not [x,y] in t2_tpoints:
				tp_count += 1
		if q2[x][y] == 2.0:
			t2_image[x][y] = [0,0,0]
			if not [x,y] in t2_tpoints:
				tn_count += 1
		if q2[x][y] == 3.0:
			t2_image[x][y] = [255,255,0]
			if not [x,y] in t2_tpoints:
				fp_count += 1
		if q2[x][y] == 4.0:
			t2_image[x][y] = [255,0,0]
			if not [x,y] in t2_tpoints:
				fn_count += 1
imsave("images/textoFind_"+str(texToFind)+"_seed_"+str(seed)+"_t2.png",t2_image)

#texture 3
print "Texture 3"
for x in range(255):
	for y in range(255):
		if q3[x][y] == 1.0: 
			t3_image[x][y] = [0,255,0]
			if not [x,y] in t3_tpoints:
				tp_count += 1
		if q3[x][y] == 2.0:
			t3_image[x][y] = [0,0,0]
			if not [x,y] in t3_tpoints:
				tn_count += 1
		if q3[x][y] == 3.0:
			t3_image[x][y] = [255,255,0]
			if not [x,y] in t3_tpoints:
				fp_count += 1
		if q3[x][y] == 4.0:
			t3_image[x][y] = [255,0,0]
			if not [x,y] in t3_tpoints:
				fn_count +=1
imsave("images/textoFind_"+str(texToFind)+"_seed_"+str(seed)+"_t3.png",t3_image)

#texture 4
print "Texture 4"
for x in range(255):
	for y in range(255):
		if q4[x][y] == 1.0: 
			t4_image[x][y] = [0,255,0]
			if not [x,y] in t4_tpoints:
				tp_count += 1
		if q4[x][y] == 2.0:
			t4_image[x][y] = [0,0,0]
			if not [x,y] in t4_tpoints:
				tn_count += 1
		if q4[x][y] == 3.0:
			t4_image[x][y] = [255,255,0]
			if not [x,y] in t4_tpoints:
				fp_count += 1
		if q4[x][y] == 4.0:
			t4_image[x][y] = [255,0,0]
			if not [x,y] in t4_tpoints:
				fn_count += 1
imsave("images/textoFind_"+str(texToFind)+"_seed_"+str(seed)+"_t4.png",t4_image)

con_file = open("confusion/con_data.csv", "a")
con_file.write(str(texToFind)+","+str(seed)+","+str(tp_count)+","+str(tn_count)+","+str(fp_count)+","+str(fn_count)+"\n")
con_file.close()

print ".Complete"






