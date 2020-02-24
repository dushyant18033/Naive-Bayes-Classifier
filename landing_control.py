#07-04-2019
#Name: DUSHYANT PANCHAL
#Roll no.: 2018033
#Section & Group: A7



import pandas as pd


def main():
	data=pd.read_excel("landing-control\\dataAsExcel.xlsx",header=None)	#Read the dataset

	#classes 1,2

	probs_given_1=[[0,0],[0,0,0,0],[0,0],[0,0],[0,0,0,0],[0,0]]	#Probabilities for class 1
	probs_given_2=[[0,0],[0,0,0,0],[0,0],[0,0],[0,0,0,0],[0,0]]	#Probabilities for class 2

	n1=0	#Count cases of class 1
	n2=0	#Count cases of class 2

	n=len(data)

	for i in range(n):
		if(data[0][i]==1):	#For each row of class 1 type
			n1+=1
			for j in range(1,7):
				if(data[j][i]=='*'):
					for k in range(len(probs_given_1[j-1])):
						probs_given_1[j-1][k]+=1
				else:
					k=data[j][i]
					probs_given_1[j-1][k-1]+=1
		elif(data[0][i]==2):	#For each row of class 2 type
			n2+=1
			for j in range(1,7):
				if(data[j][i]=='*'):
					for k in range(len(probs_given_2[j-1])):
						probs_given_2[j-1][k]+=1
				else:
					k=data[j][i]
					probs_given_2[j-1][k-1]+=1


	#Leave-one-out begins
	correctlyClassified=0

	for i in range(n):
		prob1=0
		prob2=0
		actualClass=data[0][i]

		if(actualClass==1):
			prob1=(n1-1)/(n-1)
			prob2=n2/(n-1)
			for j in range(6):
				k=data[j+1][i]
				if(k!='*'):
					prob1*=(probs_given_1[j][k-1]-1)/(n1-1)
					prob2*=probs_given_2[j][k-1]/n2
		elif(actualClass==2):
			prob1=n1/(n-1)
			prob2=(n2-1)/(n-1)
			for j in range(6):
				k=data[j+1][i]
				if(k!='*'):
					prob1*=probs_given_1[j][k-1]/n1
					prob2*=(probs_given_2[j][k-1]-1)/(n2-1)

		
		classifiedAs=0	#Classify as class giving more probability
		if(prob1>=prob2):
			classifiedAs=1
		else:
			classifiedAs=2

		if(classifiedAs==actualClass):	#If correctly classified, add to the count
			correctlyClassified+=1

	#Display results
	print("=======LANDING-CONTROL=======")
	print("Correctly classified:",correctlyClassified)
	print("Total test samples:",n)
	accuracy=correctlyClassified/n
	print("Accuracy:",accuracy)
	print("=============================")

	return accuracy

if __name__=="__main__":
	main()