#07-04-2019
#Name: DUSHYANT PANCHAL
#Roll no.: 2018033
#Section & Group: A7


import pandas as pd

def main():
	train=pd.read_excel("monks\\train1.xlsx", header=None)	#Read training dataset1
	test=pd.read_excel("monks\\test1.xlsx", header=None)	#Read testing dataset1
	a1=calc(train,test,1)
	train=pd.read_excel("monks\\train2.xlsx", header=None)	#Read training dataset2
	test=pd.read_excel("monks\\test2.xlsx", header=None)	#Read testing dataset2
	a2=calc(train,test,2)
	train=pd.read_excel("monks\\train3.xlsx", header=None)	#Read training dataset3
	test=pd.read_excel("monks\\test3.xlsx", header=None)	#Read testing dataset3
	a3=calc(train,test,3)

	return (a1,a2,a3)


def calc(train,test,ind):

	#Training
	probs_given_0=[[0,0,0],[0,0,0],[0,0],[0,0,0],[0,0,0,0],[0,0]]	#Probabilities given class 0
	probs_given_1=[[0,0,0],[0,0,0],[0,0],[0,0,0],[0,0,0,0],[0,0]]	#Probabilities given class 1


	n=len(train)

	count_0=0	#Total data of class 0
	count_1=0	#Total data of class 1

	for i in range(n):
		if(train[0][i]==0):	#For each row belonging to class 0
			count_0+=1
			for j in range(1,7):
				k=train[j][i]
				probs_given_0[j-1][k-1]+=1
		if(train[0][i]==1):	#For each row belonging to class 1
			count_1+=1
			for j in range(1,7):
				k=train[j][i]
				probs_given_1[j-1][k-1]+=1

	for i in range(1,7):	#Convert to the range of 0-1
		for j in range(len(probs_given_0[i-1])):
			probs_given_0[i-1][j]/=count_0
			probs_given_1[i-1][j]/=count_1


	#Testing begins
	m=len(test)
	correctlyClassified=0

	for i in range(m):
		prob_0=count_0/n	#Assume P(Ci)=1/n(Ci)
		prob_1=count_1/n
		classifiedAs=-1
		for j in range(1,7):
			k=test[j][i]
			prob_0*=probs_given_0[j-1][k-1]
			prob_1*=probs_given_1[j-1][k-1]

		#Test sample belongs to class with higher probability
		if(prob_1>prob_0):
			classifiedAs=1
		else:
			classifiedAs=0

		if(classifiedAs==test[0][i]):	#Check if correctly classified
			correctlyClassified+=1

	#Display the result
	print("===========MONKS-"+str(ind)+"===========")
	print("Correctly classified:",correctlyClassified)
	print("Total test samples:",m)
	accuracy=correctlyClassified/m
	print("Accuracy:",accuracy)
	print("=============================")

	return accuracy

if __name__=="__main__":
	main()