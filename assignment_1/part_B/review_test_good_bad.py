
#Calculate how tell the testing did using bad/good designation 0 - 5 , 6 - 10
#Does this be reading through data created for each run
import os
print "\n Training Data Matching 0-5, 6-10 \n"
running_total = 0.0
total_runs = 0.0
for f in sorted(os.listdir('./data/training/')):
	total_runs += 1
	if f.endswith(".txt"):
		correct = 0
		total_lines = 1
		for l in open("./data/training/"+f,"r"):
			total_lines += 1
			p = float(l.split(",")[0].strip("\n"))
			a = float(l.split(",")[1].strip("\n"))
			
			if p <= 5:
				p = 0
			else:
				p = 1
				
			if a <= 5:
				a = 0
			else:
				a = 1
			
 			if ( p == a):
				correct += 1
		print str(f) + "\t" + str( float(correct)/float(total_lines)* 100)+"% accurate"
		running_total += float(correct)/float(total_lines)* 100

print "\nTraining Average Average " + str(running_total / total_runs) + "%"

#Now the Testing data

print "\n Testing Data Matching 0-5, 6 - 10 \n"
running_total = 0.0
total_runs = 0.0
for f in sorted(os.listdir('./data/testing/')):
	total_runs += 1
	if f.endswith(".txt"):
		correct = 0
		total_lines = 1
		for l in open("./data/testing/"+f,"r"):
			total_lines += 1
			p = float(l.split(",")[0].strip("\n"))
			a = float(l.split(",")[1].strip("\n"))
			
			if p <= 5:
				p = 0
			else:
				p = 1
				
			
			if a <= 5:
				a = 0
			else:
				a = 1
			
 			if ( p == a):
				correct += 1
		print str(f) + "\t" + str( float(correct)/float(total_lines)* 100)+"% accurate"
		running_total += float(correct)/float(total_lines)* 100

print "\nTesting Average Average " + str(running_total / total_runs) + "%"
