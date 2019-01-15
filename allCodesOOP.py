#!/usr/bin/env python3

#Created by Aaron Trautman

"""These are the combination of all the codes that I have written,
rewritten in Object Oriented Programming style... It's a work in progress"""

#Test if two strings are anagrams..
class anagram():

    def __init__(self,str1,str2):
        self.str1 = str1
        self.str2 = str2
        self.test_anagram(self.str1,self.str2)

    def test_anagram(self,str1,str2):
        str1List = list(str1.upper())
        str2List = list(str2.upper())
        if len(str1) != len(str2):
            print("They are not equal in length!")
        else:
            if str1List.sort() is str2List.sort():
                print("The two strings are anagrams")
            else:
                print("No, the two strings are not anagrams")

class dnaTests():

    def __init__(self,dnaseq):
        self.seq = dnaseq

    def countDNABases(self):
        DNA = self.seq
        countA = DNA.upper().count('A')
        countT = DNA.upper().count('T')
        countG = DNA.upper().count('G')
        countC = DNA.upper().count('C')
        print("The amount of each base in the DNA sequence is: " + str(countA) + 'A, '+ str(countT) + 'T, '+ str(countG) + 'G, '+ str(countC) + 'C, ')

    def calcGCContent(self):
        DNA = self.seq
        baseLength = len(DNA)
        countGC = DNA.upper().count('C') + DNA.upper().count('G')
        GCPerc = round(countGC/baseLength * 100, 2)
        print ('The GC content in the DNA sequence is: ' + str(GCPerc) + '%')

    def testBase(self):
        DNA = self.seq
        bases = ['A','G','T','C']
        self.istrue = True
        for char in DNA.upper():
            if char in bases:
                continue
            else:
                self.istrue = False
                return self.istrue
        if self.istrue is False:
            print('The DNA sequence contains unknown characters')
        else:
            print('The DNA sequence contains only ACTG (no unknown characters)')

    def reverseSeq(self):
        rev_seq = ''
        for x in self.seq.upper():
        	if x == 'A':
        		rev_seq += 'T'
        	elif x == 'T':
        		rev_seq += 'A'
        	elif x == 'G':
        		rev_seq += 'C'
        	elif x == 'C':
        		rev_seq += 'G'
        	else:
        		rev_seq += '*'
        print ('The reverse sequence is: ' + rev_seq[::-1])

class fileParser:

    def __init__(self,infile):
        self.openFile(infile)

    def openFile(self, infile):
        with open(str(infile),'r') as readFile:
            self.file = readFile.readlines()

    def printLines(self):
        for line in self.file:
            line = line.strip()
            print(line, '\n')

class genBankParser():

    genInfo = {}        # Initialize dictionary
    filecount = 0       # Initialize amount of times GenBank is used
    def __init__(self, item):   #Init method takes a file called "item"
        self.number = self.filecount
        self.IncrementCount()
        self.file = item

    @classmethod        #Classmethod to count uses of GenBank
    def IncrementCount(self):
        self.filecount += 1

    #Genbank file parser to grab the organism, accession, and version
    def get_OrgAccVer(self):
        for line in self.file:      #Parse the file for the three dictionary keys and save the values
#            start = line.split()[0] #Grab the first item of each line
            line = line.strip()     #Remove the tabs
            if line.startswith('ORGANISM'):     #If line starts with value, add it to the value under specified key
                self.genInfo['Organism'] = str(line.split(' ')[2] + ' '+ line.split(' ')[3])        #Just to look pretty
            elif line.startswith('ACCESSION'):
                self.genInfo['Accession'] = line.replace('ACCESSION   ','')
            elif line.startswith('VERSION'):
                self.genInfo['GI'] = line.split(':')[1]
            else:
                continue

    def get_Exon(self):         #Grab the exons in the file
        with open(self.file, 'r') as innie:        #Open file
            lines = innie.readlines()
            count = 1       #Initialize the count to add to the exons
            for i in range(0, len(lines)):      #To be able to navigate through the file and grab lines other than the one it's on
                indiv = lines[i]                #Each line
                try:
                    indiv.split()[0]
                    if indiv.strip().split()[0] == 'exon' and 'exon' not in self.genInfo.keys():    #To make sure it's not overwriting an exon
                        exon = lines[i].strip().replace('..','-').replace('exon            ','')
                        gene = lines[i+1].strip().replace('\"','').split('=')[1]
                        self.genInfo['exon '+str(count)] = [gene, exon]          #Save gene and exon as dictionary value exon + count
                        count+= 1       #Add one to count "ah ah ah"
                    elif indiv.strip().split()[0] == 'exon' and 'exon '+str(count) in self.genInfo.keys():
                        exon = lines[i].strip().replace('..','-').replace('exon            ','')
                        gene = lines[i+1].strip().replace('\"','').split('=')[1]
                        self.genInfo['exon '+str(count)] = [gene, exon]
                        count+= 1
                except:
                    print("Is this a genbank file?")
                    break

    def get_Sequence(self):         #Grabs the sequence stored under the "ORIGIN" line
        with open(self.file, 'r') as innie:
            lines = innie.readlines()
            for i in range(0, len(lines)):          #To be able to navigate through the file and grab lines other than the one it's on
                    indiv = lines[i]                #Each line
                    if indiv.strip() == "ORIGIN":   #Starting at ORIGIN
                        origin = lines[i:]          #Grab the rest of the lines
                        bases = ['a', 'g','c','t']  #List of bases
                        seq = [i for n in origin for i in n if i in bases]  #List comprehensions to add bases to list seq
                        self.genInfo['Origin']= ''.join(seq)

    def printitems(self):      #printme method takes one arg, self
        for key in sorted(self.genInfo):        #Pretty printing for loop
            print(key, '->', self.genInfo[key]) #You've changed bro

    def seq_GC_content(self):       #Calculate gc content
        try:
            seq = self.genInfo['Origin'] #Take sequence stored in dictionary as Origin
            gc = dnaTests(seq)
            gc.calcGCContent
        except:
            print('No sequence stored under origin.. Are you really sure this is a GenBank file??')

class statsTests():

    def twoSampleTtest(self):
        import math
        import sys
        Mu_1 = input('Enter first (largest) mean: ')
        Mu_2 = input('Enter second (smallest) mean: ')

        std_dev1 = float(input('Enter first variance: '))
        std_dev2 = float(input('Enter second variance: '))

        N1 = int(input('Enter first sample size as an integer: '))
        N2 = int(input('Enter second sample size as an integer: '))

        #Compute difference of means
        Mu_12 = (float(Mu_1) - float(Mu_2))
        print ('The difference of the means is: ' + str(Mu_12) + '.')

        #Compute standard error or variance of the means
        var = math.sqrt(((N1-1)*(std_dev1 ** 2) + (N2-1)*(std_dev2 ** 2))/(N1+N2-2))
        print ('The variance of the means is: ' + str(var) + '.')

        #Compute degrees of freedom
        freed = (N1 + N2 - 2)
        print ('The degrees of freedom is: ' + str(freed) + '.')

        #Compute t-value
        t = Mu_12 / (var * math.sqrt(1/N1 + 1/N2))
        print ('The t value is: ' + str(t) + '.')

        #Compute p-value
        print ('')
        print('Go here and input your data to get your p-value: http://onlinestatbook.com/2/calculators/t_dist.html')
