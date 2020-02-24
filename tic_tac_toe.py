#07-04-2019
#Name: DUSHYANT PANCHAL
#Roll no.: 2018033
#Section & Group: A7



import pandas as pd


def main():
	data=pd.read_excel("tic-tac-toe\\dataAsExcel.xlsx", header=None)	#Read the data

	n=len(data)	#Total data entries

	#C0 - positive
	#C1 - negative
	#xi - x,o,b

	#Lists for storing probabilities for each case of class positive
	x_given_pos=[0,0,0,0,0,0,0,0,0]
	o_given_pos=[0,0,0,0,0,0,0,0,0]
	b_given_pos=[0,0,0,0,0,0,0,0,0]

	#Lists for storing probabilities for each case of class negative
	x_given_neg=[0,0,0,0,0,0,0,0,0]
	o_given_neg=[0,0,0,0,0,0,0,0,0]
	b_given_neg=[0,0,0,0,0,0,0,0,0]

	
	count_pos=0	#Count cases for class positive
	count_neg=0	#Count cases for class negative

	for i in range(n):
		if(data[9][i][0]=='p'):	#If class positive
			count_pos+=1
			for j in range(9):
				if(data[j][i]=='x'):
					x_given_pos[j]+=1
				elif(data[j][i]=='o'):
					o_given_pos[j]+=1
				elif(data[j][i]=='b'):
					b_given_pos[j]+=1

		elif(data[9][i][0]=='n'):	#If class negative
			count_neg+=1
			for j in range(9):
				if(data[j][i]=='x'):
					x_given_neg[j]+=1
				elif(data[j][i]=='o'):
					o_given_neg[j]+=1
				elif(data[j][i]=='b'):
					b_given_neg[j]+=1


	#Leave-one-out begins
	CorrectlyClassified=0

	for i in range(n):
		prob_pos=0
		prob_neg=0
		classifiedTo=''

		actualClass=data[9][i][0]

		if(actualClass=='p'):
			prob_pos=(count_pos-1)/(n-1)
			prob_neg=count_neg/(n-1)
			for j in range(9):	#Find probability for each class
				if(data[j][i]=='x'):
					prob_pos*=(x_given_pos[j]-1)/(count_pos-1)
					prob_neg*=x_given_neg[j]/count_neg
				elif(data[j][i]=='o'):
					prob_pos*=(o_given_pos[j]-1)/(count_pos-1)
					prob_neg*=o_given_neg[j]/count_neg
				elif(data[j][i]=='b'):
					prob_pos*=(b_given_pos[j]-1)/(count_pos-1)
					prob_neg*=b_given_neg[j]/count_neg
		elif(actualClass=='n'):
			prob_pos=count_pos/(n-1)
			prob_neg=(count_neg-1)/(n-1)
			for j in range(9):	#Find probability for each class
				if(data[j][i]=='x'):
					prob_pos*=(x_given_pos[j])/(count_pos)
					prob_neg*=(x_given_neg[j]-1)/(count_neg-1)
				elif(data[j][i]=='o'):
					prob_pos*=(o_given_pos[j])/(count_pos)
					prob_neg*=(o_given_neg[j]-1)/(count_neg-1)
				elif(data[j][i]=='b'):
					prob_pos*=(b_given_pos[j])/(count_pos)
					prob_neg*=(b_given_neg[j]-1)/(count_neg-1)
		
		if(prob_pos>prob_neg):	#Classify as class giving greater probability
			classifiedTo='p'
		else:
			classifiedTo='n'

		if(classifiedTo==actualClass):	#If correctly classified, add to the count
			CorrectlyClassified+=1

	#Display results
	print("=========TIC-TAC-TOE=========")
	print("Correctly classified: ",CorrectlyClassified)
	print("Total test samples: ",n)
	accuracy=CorrectlyClassified/n
	print("Accuracy: ",accuracy)
	print("=============================")

	return accuracy

if __name__=="__main__":
	main()