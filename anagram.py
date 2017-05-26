#!/usr/local/bin/python3

def anagram(str1,str2):
    str1List = list(str1.upper())
    str2List = list(str2.upper())
    print (str1List, str2List)
    if len(str1) != len(str2):
        print("They are not equal in length!")
    else:
        if str1List.sort() is str2List.sort():
            print("The two strings are anagrams")
        else:
            print("No, the two strings are not anagrams")

anagram(input("What's your first string? "),input("What's your second string? "))
