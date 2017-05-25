def anagram(str1,str2):
    str1List = list(str1.upper())
    str2List = list(str2.upper())
    print (str1List, str2List)
    if len(str1) != len(str2):
        print("They not equal")
    else:
#        for x in str1.upper():
#            str1List.append(x)
#            print (str1List)
#        for z in str2.upper():
#            str2List.append(z)
#            print (str2List)
        if str1List.sort() is str2List.sort():
            print("The two strings are anagrams")
        else:
            print("Nein!")

anagram(input("What's your first string? "),input("What's your second string? "))
