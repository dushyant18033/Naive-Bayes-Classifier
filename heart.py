#07-04-2019
#Name: DUSHYANT PANCHAL
#Roll no.: 2018033
#Section & Group: A7




import pandas as pd


def main():
	train=pd.read_excel("heart\\trainDataAsExcel.xlsx", header=None)	#Train data
	test=pd.read_excel("heart\\testDataAsExcel.xlsx", header=None)		#Test data

	probs_given_0=list()	#Probabilities given class 0
	probs_given_1=list()	#Probabilities given class 1

	for i in range(len(train.columns)-1):	#Initialize count with 0
		probs_given_0.append([0,0])
		probs_given_1.append([0,0])

	n=len(train)

	count_0=0	#Count cases of class 0
	count_1=0	#Count cases of class 1

	for i in range(n):
		if(train[0][i]==0):	#If belongs to class 0
			count_0+=1
			for j in range(len(train.columns)-1):
				k=train[j+1][i]
				probs_given_0[j][k]+=1
		elif(train[0][i]==1):	#If belongs to class 1
			count_1+=1
			for j in range(len(train.columns)-1):
				k=train[j+1][i]
				probs_given_1[j][k]+=1

	for i in range(len(train.columns)-1):	#Reduce to range of 0-1
		probs_given_0[i][0]/=count_0
		probs_given_0[i][1]/=count_0
		probs_given_1[i][0]/=count_1
		probs_given_1[i][1]/=count_1


	#Testing begins
	m=len(test)
	correctlyClassified=0	#Count for correct classifications

	for i in range(m):
		prob_0=count_0/n	#Assuming P(Ci)=1/n(Ci)
		prob_1=count_1/n
		classifiedAs=-1
		for j in range(len(test.columns)-1):	#Check probability for each class
			k=test[j+1][i]
			prob_0*=probs_given_0[j][k]
			prob_1*=probs_given_1[j][k]

		if(prob_1>prob_0):	#Classify as one giving more probability
			classifiedAs=1
		else:
			classifiedAs=0

		if(classifiedAs==test[0][i]):	#If correctly classified, add to the count
			correctlyClassified+=1

	#Display the results
	print("============HEART============")
	print("Correctly classified:",correctlyClassified)
	print("Total test samples:",m)
	accuracy=correctlyClassified/m
	print("Accuracy:",accuracy)
	print("=============================")

	return accuracy


if __name__=="__main__":
	main()