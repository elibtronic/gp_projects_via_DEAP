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

for f in sorted(os.listdir('./logs/t1')):
	if f.endswith(".txt"):
		cLogAVG = open("./logs/t1_avg_"+f,"w")
		cLogBEST = open("./logs/t1_best_"+f,"w")
		cLog = open("./logs/t1/"+f,"r")
		cLog.readline()
		cLog.readline()
		cLog.readline()
		cLogAVG.write(f+"\n")
		cLogBEST.write(f+"\n")
		for l in cLog:
			dp = l.split("\t")
			cLogAVG.write(dp[2]+"\n")
			cLogBEST.write(dp[4]+"\n")

for f in sorted(os.listdir('./logs/t2')):
	if f.endswith(".txt"):
		cLogAVG = open("./logs/t2_avg_"+f,"w")
		cLogBEST = open("./logs/t2_best_"+f,"w")
		cLog = open("./logs/t2/"+f,"r")
		cLog.readline()
		cLog.readline()
		cLog.readline()
		cLogAVG.write(f+"\n")
		cLogBEST.write(f+"\n")
		for l in cLog:
			dp = l.split("\t")
			cLogAVG.write(dp[2]+"\n")
			cLogBEST.write(dp[4]+"\n")

for f in sorted(os.listdir('./logs/t3')):
	if f.endswith(".txt"):
		cLogAVG = open("./logs/t3_avg_"+f,"w")
		cLogBEST = open("./logs/t3_best_"+f,"w")
		cLog = open("./logs/t3/"+f,"r")
		cLog.readline()
		cLog.readline()
		cLog.readline()
		cLogAVG.write(f+"\n")
		cLogBEST.write(f+"\n")
		for l in cLog:
			dp = l.split("\t")
			cLogAVG.write(dp[2]+"\n")
			cLogBEST.write(dp[3]+"\n")

for f in sorted(os.listdir('./logs/t4')):
	if f.endswith(".txt"):
		cLogAVG = open("./logs/t4_avg_"+f,"w")
		cLogBEST = open("./logs/t4_best_"+f,"w")
		cLog = open("./logs/t4/"+f,"r")
		cLog.readline()
		cLog.readline()
		cLog.readline()
		cLogAVG.write(f+"\n")
		cLogBEST.write(f+"\n")
		for l in cLog:
			dp = l.split("\t")
			cLogAVG.write(dp[2]+"\n")
			cLogBEST.write(dp[4]+"\n")
