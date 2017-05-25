#!//anaconda/bin/python3
import time
#Step 1. Filter out unnecessary text
start1 = time.time()
with open('m130929_024849_42213_c100518541910000001823079209281311_s1_p0.1.subreads.fastq', 'r') as old_dna, open('data.txt', 'w') as new_dna:
    for line in old_dna:
        if line.startswith(('A', 'G', 'C', 'T')):
		# If the line starts with a DNA base(taken as a tuple), write it to the new file
            new_dna.write(line)
        else:
		# Otherwise continue
            continue
end1 = time.time()
print ("The time to write the first file is: "+ str(end1-start1)+"seconds")

#Step 2. Define function makeKmers
def makeKmers(DNA, k):
    kmerList = []
	# Blank list in which kmers are appended
    n = len(DNA)
	# Length of the string
    if n >= k:
        for i in range(0, n-k+1):
		# Create kmers for range 0-(n-k+1) and append them to the blank list
            kmerList.append(DNA[i:i+k])
        return kmerList
    else:
        kmerList.append(DNA)
        return kmerList

#Step 3. Make kmers for every sequence
start3 = time.time()
kmerDNAlist = []
g = 40

with open('data.txt', 'r') as new_dna:
    for line in new_dna:
        line = line.rstrip()
        kmerDNAlist.append(makeKmers(line, g))
end3 = time.time()
print ("The time to make the kmers was: " + str(end3-start3)+"seconds")

#Step 4. Construct De-Bruijn dictionary
start4= time.time()

edges = [i for s in kmerDNAlist for i in s]
edges = list(set(edges))
debruijn_graph={}

for edge in edges:
    frm = edge[:len(edge)-1]
    to = edge[1:]
    if frm in debruijn_graph:
        debruijn_graph[frm].append(to)
    else:
        debruijn_graph[frm]=[to]

for val in debruijn_graph.values():
    val.sort()
with open('debruijn_graph.txt', 'w') as debruijn:
    for k,v in sorted(debruijn_graph.items()):
        debruijn.write(k+' -> '+','.join(v) + "\n")

end4 = time.time()

print ("The time to make the debruijn graph was: "+ str(end4-start4)+"seconds")
