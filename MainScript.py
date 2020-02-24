#07-04-2019
#Name: DUSHYANT PANCHAL
#Roll no.: 2018033
#Section & Group: A7



import pandas as pd

#Importing scripts for all datasets
import tic_tac_toe
import heart
import soybean
import landing_control
import monks


#List for names of datasets
Datasets=["Tic-Tac-Toe Endgame Data Set","SPECT Heart Data Set","Soybean (Small) Data Set","Shuttle Landing Control Data Set","MONK's Problems Data Set 1","MONK's Problems Data Set 2","MONK's Problems Data Set 3"]

#List for accuracy calculated
k=monks.main()
Accuracy=[tic_tac_toe.main(),heart.main(),soybean.main(),landing_control.main(),k[0],k[1],k[2]]

#Dictionary to be used as dataframe
Results={'Datasets':Datasets, 'Accuracy':Accuracy}

#Write the results to an excel file
df=pd.DataFrame(Results)
writer=pd.ExcelWriter('Accuracy Table.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()