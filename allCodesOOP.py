#!/usr/local/bin/python3

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
        self.countDNABases(self.seq)
        self.calcGCContent(self.seq)
        self.testBase(self.seq)
        if self.istrue is False:
            print('The DNA sequence contains unknown characters')
        else:
            print('The DNA sequence contains only ACTG (no unknown characters)')

    def countDNABases(self,DNA):
        countA = DNA.upper().count('A')
        countT = DNA.upper().count('T')
        countG = DNA.upper().count('G')
        countC = DNA.upper().count('C')
        print("The amount of each base in the DNA sequence is: " + str(countA) + 'A, '+ str(countT) + 'T, '+ str(countG) + 'G, '+ str(countC) + 'C, ')

    def calcGCContent(self, DNA):
        baseLength = len(DNA)
        countGC = DNA.upper().count('C') + DNA.upper().count('G')
        GCPerc = round(countGC/baseLength * 100, 2)
        print ('The GC content in the DNA sequence is: ' + str(GCPerc) + '%')

    def testBase(self, DNA):
        bases = ['A','G','T','C']
        self.istrue = True
        for char in DNA.upper():
            if char in bases:
                continue
            else:
                self.istrue = False
                return self.istrue

a = dnaTests('ASDGCBFHDNSmshdncbvhgsdyfccgc')
