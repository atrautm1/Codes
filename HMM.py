#!/anaconda/bin/python3

"""This was a basic attempt at a hidden markov model using python.. 
I never got around to completing it, but I thought it was interesting 
to show. I wrote it to help with calculating HMM probabilities for a
Molecular Sequence Analysis course."""

#List of probabilities
A1 = 0.5
A2 = 0.05
B = 0.95
C = 0.9
D = 0.045
E = 0.095
F = 0.005

fairDict = {'1':1/6,'2':1/6,'3':1/6,'4':1/6,'5':1/6,'6':1/6}
loadDict = {'1':1/10,'2':1/10,'3':1/10,'4':1/10,'5':1/10,'6':1/2}

thingamabob = input("Enter thingamabob here: ")

fairProbsf = []
loadProbsf = []

initialfairProbf = fairDict.get(thingamabob[0])*1*A1
initialloadProbf = loadDict.get(thingamabob[0])*1*A2
fairProbsf.append(initialfairProbf)
loadProbsf.append(initialloadProbf)

count = 1

while count < len(thingamabob):
    if count == 1:
        fairProbsf.append(fairDict.get(thingamabob[count])*(initialfairProbf*B+(A1*E)))
        loadProbsf.append(loadDict.get(thingamabob[count])*(initialloadProbf*C+(A2*D)))
        count = count + 1
    else:
        fairProbsf.append(fairDict.get(thingamabob[count])*(fairProbsf[count-1]*B+A1*E))
        loadProbsf.append(loadDict.get(thingamabob[count])*(loadProbsf[count-1]*C+A2*D))
        count = count + 1

endProbf = (loadProbsf[len(loadProbsf)-1]*F)+(fairProbsf[len(fairProbsf)-1]*F)

pathF = []
count = 0
while count < len(thingamabob):
        if float(fairProbsf[count]) > float(loadProbsf[count]):
            pathF.append("F")
            count += 1
        else:
            pathF.append("L")
            count += 1

print ("Fair Probabilities (forward): " + str(fairProbsf))
print ("Loaded Probabilities (forward): " + str(loadProbsf))
print("End Probability (forward): " + str(endProbf))
print(pathF)
#Start reverse code
fairProbsR = []
loadProbsR = []

initialfairProbR = F
initialloadProbR = F
fairProbsR.append(initialfairProbR)
loadProbsR.append(initialloadProbR)

count = len(thingamabob)-1
othercount = 1

while count > 0:
    if count == len(thingamabob):
        fairProbsR.append(fairDict.get(thingamabob[count])*(initialfairProbR*B+(A1*E)))
        loadProbsR.append(loadDict.get(thingamabob[count])*(initialloadProbR*C+(A2*D)))
        count = count - 1
    else:
        fairProbsR.append(fairDict.get(thingamabob[count])*(fairProbsR[othercount-1]*B+(A1*E)))
        loadProbsR.append(loadDict.get(thingamabob[count])*(loadProbsR[othercount-1]*C+(A2*D)))
        count = count - 1
        othercount += 1

endProbR = (loadProbsR[len(loadProbsR)-1]*F)+(fairProbsR[len(fairProbsR)-1]*F)

pathR = []
count = 0
while count < len(thingamabob):
    for item in fairProbsR:
        if float(fairProbsR[count]) > float(loadProbsR[count]):
            pathR.append("F")
            count += 1
        else:
            pathR.append("L")
            count += 1

fairProbsR = fairProbsR[::-1]
loadProbsR = loadProbsR[::-1]


print ("Fair Probabilities (reverse): " + str(fairProbsR))
print ("Loaded Probabilities (reverse): " + str(loadProbsR))
print("End Probability (reverse): " + str(endProbR))
print(pathR)

#start combined probabilities

count = 0
faircombProbs = []
loadcombProbs = []
while count < len(fairProbsR):
    faircombProbs.append(float((float(fairProbsR[count])*float(fairProbsf[count]))/float(endProbf)))
    loadcombProbs.append(float((float(loadProbsR[count])*float(loadProbsf[count]))/float(endProbf)))
    count += 1

combPath = []
cnt = 0

while cnt < len(faircombProbs):
    if faircombProbs[cnt] > loadcombProbs[cnt]:
        combPath.append("F")
        cnt += 1
    else:
        combPath.append("L")
        cnt += 1

print("The combined fair probabilities are: " + str(faircombProbs))
print("The combined loaded probabilities are: " + str(loadcombProbs))
print(combPath)
