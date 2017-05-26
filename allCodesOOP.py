#!/usr/local/bin/python3

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
