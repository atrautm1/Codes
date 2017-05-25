#!usr/bin/python

#Create the dictionary of amino acids

aminoDict = {'Ala' : ['GCU', 'GCC', 'GCA', 'GCG'], 'Arg' : ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'Asn' : ['AAU', 'AAC'], 'Asp' : ['GAU', 'GAC'], 'Cys' : ['UGU', 'UGC'], 'Gln' : ['CAA', 'CAG'], 'Glu' : ['GAA', 'GAG'], 'Gly' : ['GGU', 'GGC', 'GGA', 'GGG'], 'His' : ['CAU', 'CAC'], 'Ile' : ['AUU', 'AUC', 'AUA'], 'Leu': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], 'Lys' : ['AAA', 'AAG'], 'Met' : ['AUG'], 'Phe' : ['UUU', 'UUC'], 'Pro' : ['CCU', 'CCC', 'CCA', 'CCG'], 'Ser' : ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 'Thr' : ['ACU', 'ACC', 'ACA', 'ACG'], 'Trp' : 'UGG', 'Tyr' : ['UAU', 'UAC'], 'Val' : ['GUU', 'GUC', 'GUA', 'GUG'], 'START' : ['AUG'], 'STOP' : ['UAA', 'UGA', 'UAG']}

#For each key in the sorted dictionary, print the key, codons, and amount of codons

for key in sorted(aminoDict):
	print(key, aminoDict[key], len(aminoDict[key]))

