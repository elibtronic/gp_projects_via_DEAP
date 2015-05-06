#Helper script that spits out
#log data in columnar form, suitable for manipulation

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
