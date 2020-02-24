#07-04-2019
#Name: DUSHYANT PANCHAL
#Roll no.: 2018033
#Section & Group: A7



import pandas as pd


def main():
	data=pd.read_excel("soybean\\dataAsExcel.xlsx",header=None)	#Read data

	n=len(data)

	#Lists for storing probabilities
	prob_givenD1=list()
	prob_givenD2=list()
	prob_givenD3=list()
	prob_givenD4=list()

	#Initialize counts with 0
	for i in range(len(data.columns)-1):
		k=max(data[i])
		a1=list()
		a2=list()
		a3=list()
		a4=list()
		for j in range(k+1):
			a1.append(0)
			a2.append(0)
			a3.append(0)
			a4.append(0)

		prob_givenD1.append(a1)
		prob_givenD2.append(a2)
		prob_givenD3.append(a3)
		prob_givenD4.append(a4)

	
	#Count cases for different classes
	count1=0
	count2=0
	count3=0
	count4=0

	for i in range(n):
		if(data[35][i]=="D1"):	#If class D1
			count1+=1
			for j in range(len(data.columns)-1):
				k=data[j][i]
				prob_givenD1[j][k]+=1
		elif(data[35][i]=="D2"):	#If class D2
			count2+=1
			for j in range(len(data.columns)-1):
				k=data[j][i]
				prob_givenD2[j][k]+=1
		elif(data[35][i]=="D3"):	#If class D3
			count3+=1
			for j in range(len(data.columns)-1):
				k=data[j][i]
				prob_givenD3[j][k]+=1
		elif(data[35][i]=="D4"):	#If class D4
			count4+=1
			for j in range(len(data.columns)-1):
				k=data[j][i]
				prob_givenD4[j][k]+=1


	#Leave-one-out begins
	
	correctlyClassified=0
	for i in range(n):

		probs=[0,0,0,0]
		classifiedAs=-1
		actualClass=data[data.columns[-1]][i]

		if(actualClass=="D1"):
			probs[0]=(count1-1)/(n-1)
			probs[1]=count2/(n-1)
			probs[2]=count3/(n-1)
			probs[3]=count4/(n-1)
			for j in range(len(data.columns)-1):	#Check probability for each class
				k=data[j][i]
				probs[0]*=(prob_givenD1[j][k]-1)/(n-1)
				probs[1]*=prob_givenD2[j][k]/(n-1)
				probs[2]*=prob_givenD3[j][k]/(n-1)
				probs[3]*=prob_givenD4[j][k]/(n-1)
		elif(actualClass=="D2"):
			probs[0]=count1/(n-1)
			probs[1]=(count2-1)/(n-1)
			probs[2]=count3/(n-1)
			probs[3]=count4/(n-1)
			for j in range(len(data.columns)-1):	#Check probability for each class
				k=data[j][i]
				probs[0]*=prob_givenD1[j][k]/(n-1)
				probs[1]*=(prob_givenD2[j][k]-1)/(n-1)
				probs[2]*=prob_givenD3[j][k]/(n-1)
				probs[3]*=prob_givenD4[j][k]/(n-1)
		elif(actualClass=="D3"):
			probs[0]=count1/(n-1)
			probs[1]=count2/(n-1)
			probs[2]=(count3-1)/(n-1)
			probs[3]=count4/(n-1)
			for j in range(len(data.columns)-1):	#Check probability for each class
				k=data[j][i]
				probs[0]*=prob_givenD1[j][k]/(n-1)
				probs[1]*=prob_givenD2[j][k]/(n-1)
				probs[2]*=(prob_givenD3[j][k]-1)/(n-1)
				probs[3]*=prob_givenD4[j][k]/(n-1)
		elif(actualClass=="D4"):
			probs[0]=count1/(n-1)
			probs[1]=count2/(n-1)
			probs[2]=count3/(n-1)
			probs[3]=(count4-1)/(n-1)
			for j in range(len(data.columns)-1):	#Check probability for each class
				k=data[j][i]
				probs[0]*=prob_givenD1[j][k]/(n-1)
				probs[1]*=prob_givenD2[j][k]/(n-1)
				probs[2]*=prob_givenD3[j][k]/(n-1)
				probs[3]*=(prob_givenD4[j][k]-1)/(n-1)
		

		classifiedAs=probs.index(max(probs))	#Assign class which gave highest probability
		className="D"+str(classifiedAs+1)

		if(className==actualClass):	#If correctly classified, add to the count
			correctlyClassified+=1


	#Display the results
	print("===========SOYBEAN===========")
	print("Correctly classified:",correctlyClassified)
	print("Total test samples:",n)
	accuracy=correctlyClassified/n
	print("Accuracy:",accuracy)
	print("=============================")

	return accuracy


if __name__=="__main__":
	main()