#Helper script that spits out
#ParamSet 1
#--Average Fitness of ten runs, for each of the 50 gens (plus initial)
#--Best Fitness of ten runs, for each of the 50 gens (plus initial)
#ParamSet 2
#--Average Fitness of ten runs, for each of the 50 gens (plus initial)
#--Best Fitness of ten runs, for each of the 50 gens (plus initial)
#
# The idea is to write out this into textfiles where bash script
# will call paste to put data together
import os

for f in sorted(os.listdir('./logs')):
	if f.endswith(".txt"):
		cLogAVG = open("./logs/A_"+f,"w")
		cLogBEST = open("./logs/B_"+f,"w")
		cLog = open("./logs/"+f,"r")
		cLog.readline()
		cLog.readline()
		cLog.readline()
		cLogAVG.write(f+"\n")
		cLogBEST.write(f+"\n")
		for l in cLog:
			dp = l.split("\t")
			cLogAVG.write(dp[2]+"\n")
			cLogBEST.write(dp[4]+"\n")
