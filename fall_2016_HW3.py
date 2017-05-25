#!/usr/bin/python
#Created by Aaron Trautman
#DNA sequence
DNA = 'AGCAGCTTGAGT'  

#Prints the sequence
print("The DNA sequence is: " + DNA)

#Create global variables that have the amounts of each base in the DNA sequence
countA = DNA.count('A')
countG = DNA.count('G')
countT = DNA.count('T')
countC = DNA.count('C')

#Print the base amounts
print("The amount of each base in the DNA sequence is: " + str(countA) + 'A, '+ str(countT) + 'T, '+ str(countG) + 'G, '+ str(countC) + 'C, ')

#Search the DNA sequence for GCT and print accordingly
if DNA.find('GCT') >= 0:            
    print('GCT is in the DNA sequence')
else:
    print('GCT is not in the DNA sequence')
 
#Search the DNA sequence for ATC and print accordingly
if DNA.find('ATC') >= 0:           
    print('ATC is in the DNA sequence')
else:
    print('ATC is not in the DNA sequence')

#Replace the motif AGC with TCG and save as a new string DNAr
DNAr = DNA.replace('AGC','TCG') 

#Print the new DNA sequence
print('The new DNA sequence with AGC replaced is: ' + DNAr)             

#Split the string DNA
DNAs = DNA.split('G')        

#Prints the 3rd value in the resulting list
print('The 3rd value in the list split by G is: ' + DNAs[2]) 



