
# look at all rows from training/testing data to generate the confusion matrix
# categories

print "Good Bad Confusion Matrix"
print "\n"
print " TP | FN"
print " FP | TN"

true_positive = 0.0
true_negative = 0.0
false_positive = 0.0
false_negative = 0.0
total_rows = 0.0

for l in open("confusion_matrix_training.csv","r"):
	total_rows += 1
	e = round(float(l.split(",")[0].strip("\n")))
	a = round(float(l.split(",")[1].strip("\n")))

	#6 - 10 is 'good' wine
	if a >= 6:
		if e >= 6:
			true_positive += 1
		else:
			false_positive += 1
	else: #0 - 5 is 'bad' wine
		if e <= 5:
			true_negative += 1
		else:
			false_negative += 1



print "\nTraining_data\n"
print str(true_positive) + " | " + str(false_negative)
print str(false_positive) + " | " + str(true_negative)

true_positive = 0.0
true_negative = 0.0
false_positive = 0.0
false_negative = 0.0
total_rows = 0.0

for l in open("confusion_matrix_testing.csv","r"):
	total_rows += 1
	e = round(float(l.split(",")[0].strip("\n")))
	a = round(float(l.split(",")[1].strip("\n")))
	
	#6 - 10 is 'good' wine
	if a >= 6:
		if e >= 6:
			true_positive += 1
		else:
			false_positive += 1
	else: #0 - 5 is 'bad' wine
		if e <= 5:
			true_negative += 1
		else:
			false_negative += 1

print "\nTesting_data\n"
print str(true_positive) + " | " + str(false_negative)
print str(false_positive) + " | " + str(true_negative)
print "\n"


