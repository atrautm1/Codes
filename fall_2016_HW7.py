#!/anaconda/bin/python3/
import hw7module

with open(input("Enter name of file to count GC content: "),'r') as readme, open("hw7.out",'w') as makeme:
    makeme.write("Aaron Trautman")
    gcTotal = 0                                                                     #Initialize the counts "ah ah ah"
    seqTotal = 0
    for line in readme.readlines():
        if line.startswith(">"):                                                    #Skip the header
            continue
        else:
            line = line.rstrip()                                                    #Strip the newline characters
            gcTotal += hw7module.gcCounter(line)                                    #For each line, add the gcCount from the module
            seqTotal += len(line)                                                   #Add the length of the line to the sequnce total
    gcPerc = round((gcTotal/seqTotal)*100,2)                                              #Calculate GC percentage
    makeme.write("\nThe GC content of the sequence is: " + str(gcPerc) + "% \n")       #Write it to the new file
