#!//anaconda/bin/python3
import time

start = time.time()
#Open both in and outfiles
with open("hw5.vcf", 'r') as infile, open("hw6.out",'w') as outfile:
        #Iterate through the lines
    for line in infile:
        #Remove the end text
        line=line.rstrip()
            #If the line starts with ##, ignore
        if line.startswith("##"):
            continue
            #Make a header for the line that starts with #
        elif line.startswith('#'):
            header = line.split('\t')
            #Write header line
            outfile.write(header[2]+"\t"+header[3]+"\t"+header[4]+"\t"+'RAF'+"\n")
        else:
            #Split the lines by the tabs
            newcol = line.split("\t")
            #Empty list to put the genotypes
            newlist = []
            for things in newcol[9:]:
                #Split the list by the colons
                alleles = things.split(':')
                #Append the first item to the "newlist"
                newlist.append(alleles[0])
            #Count homozygous alleles(*2) and add to both types of heterozygous alleles
            #divided by the amount of samples (n = 11; len(newlist)) and save as "num"
            num = ((newlist.count("0|0")*2) + newlist.count("0|1") + newlist.count("1|0"))/(2*len(newlist))
            #Write the columns into the outfile
            outfile.write(newcol[2]+'\t'+newcol[3]+'\t'+newcol[4]+'\t' + str(num)+"\n")
            #Write the columns into the outfile

end = time.time()

print ("the time was: " + str(end - start))
