#
# Calculates the average average fitness score for the 10 runs of
# each training set provided as command line arguments

import sys

if __name__ == "__main__":
	rsum = 0.0
	sfile = sys.argv[1]
	count = float(sys.argv[2])

	sf = open(sfile,"r")
	for s in sf:
		val = s.split(",")[2]
		try:
			rsum += abs(float(val))/count
		except:
			print val

	print str(rsum/count),
