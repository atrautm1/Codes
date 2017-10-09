#!/usr/local/bin/python3

#Change to whatever you call your file
infile = open('blastResultsAA', 'r')

infileRead = infile.readlines()

blastList= []
blastDict = {}
for i in range(0,len(infileRead)):
    line = infileRead[i]
    if line.startswith('\n'):
        blastList.append(blastDict)
        blastDict = {}
    else:
        organism = line.strip().split(':')[0]
        score = int(line.strip().split('K')[1].split('   ')[1])
        if organism in blastDict.keys():
            continue
        else:
            blastDict[organism] = score

blastDictTot = {}

for x in blastList:
    for key,value in x.items():
        if key in blastDictTot.keys():
            blastDictTot[key] += value
        else:
            blastDictTot[key] = value

#Change to whatever you want to call your new file
outfile = open('editedBlastResultsAA.txt', 'w')

for k,v in blastDictTot.items():
    total = blastDictTot['gmx']
    elem = blastDictTot[k]
    perc = round((elem / total * 100),2)
    outfile.write(k + '\t' + str(v) + '\t' + str(perc) + '%' + '\n')


outfile.close()
infile.close()
