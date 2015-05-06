
#Calculate how tell the testing did matching exact scores
#done by opening the data files generated during the run and computing values
import os
print "\nTraining Data Matching Actual Choice\n"
running_total = 0.0
total_runs = 0
for f in sorted(os.listdir('./data/training/')):
	total_runs += 1
	if f.endswith(".txt"):
		correct = 0
		total_lines = 1
		for l in open("./data/training/"+f,"r"):
			total_lines += 1
			p = round(float(l.split(",")[0]))
			a = round(float(l.split(",")[1]))
 			if ( p - a == 0):
				correct += 1
		print str(f) + "\t" + str( float(correct)/float(total_lines)* 100)+"% accurate"
		running_total += float(correct)/float(total_lines)* 100
		
print "Training Average Average " + str(running_total / total_runs) + "%"

#Repeat the Process on the Testing Data
print "\nTesting Data Matching Actual Choice\n"
running_total = 0.0
total_runs = 0
for f in sorted(os.listdir('./data/testing/')):
	total_runs += 1
	if f.endswith(".txt"):
		correct = 0
		total_lines = 1
		for l in open("./data/testing/"+f,"r"):
			total_lines += 1
			p = round(float(l.split(",")[0]))
			a = round(float(l.split(",")[1]))
 			if ( p - a == 0):
				correct += 1
		print str(f) + "\t" + str( float(correct)/float(total_lines)* 100)+"% accurate"
		running_total += float(correct)/float(total_lines)* 100
		
print "Testing Average Average " + str(running_total / total_runs) + "%"
	
