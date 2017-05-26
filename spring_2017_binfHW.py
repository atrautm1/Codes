#!/usr/local/bin/python3
print("Aaron Trautman")
print("atrautm1@uncc.edu")

class GenBank:
    genInfo = {}        # Initialize dictionary
    filecount = 0       # Initialize amount of times GenBank is used
    def __init__(self, item):   #Init method takes a file called "item"
        self.number = self.filecount
        self.IncrementCount()
        self.file = item

    @classmethod        #Classmethod to count uses of GenBank
    def IncrementCount(self):
        self.filecount += 1

    def get_OrgAccVer(self):        # Parse file and grab the Organism, Accession, and Version
        with open(self.file, 'r') as innie:        #Open file
            lines = innie.readlines()
            for line in lines:      #Parse the file for the three dictionary keys and save the values
                start = line.split()[0] #Grab the first item of each line
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

    def calc_gc_content(self):       #Calculate gc content
        seq = self.genInfo['Origin'] #Take sequence stored in dictionary as Origin
        bases = ['g','c']       #List of bases
        gc = 0                  #Initial gc count
        for x in seq:           #For each item (x) in seq
            if x in bases:      #If it's found in bases
                gc += 1         #Add 1 to GC count
        gc_perc = (gc*100)/len(seq) #Formula for calculating gc_percent
        print('The gc content of the sequence is: ' + str(round(gc_perc,2))+'%')


g = GenBank('hw2_hla.gb')
g.get_OrgAccVer()
g.get_Sequence()
g.get_Exon()
g.printitems()
g.calc_gc_content()
print (g.filecount)
