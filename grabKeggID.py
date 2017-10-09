#!/usr/local/bin/python3


#Grab kegg gene ids for NCBI accession numbers..

import requests as req, bs4, re

#infile = open('keggpathtogene.txt', 'r')
#infileLines = infile.readlines()

#keggDict = {}

#for line in infileLines:
#    pathway = line.split('\t')[0]
#    gene = line.strip().split('\t')[1]
#    if pathway in keggDict.keys():
#        keggDict[pathway].append(gene)
#    else:
#        keggDict[pathway] = [gene]


#for k,v in keggDict.items():
#    print(k, ' -> ', v, '\n')

infile = open('editedGenes.txt', 'r')
infileLines = infile.readlines()

geneList = []
for line in infileLines:
    geneList.append(line.strip())

infile.close()

outfile = open('mapKeggtoAcc2.txt', 'w')

for gene in geneList:
  ncbi = req.get('https://www.ncbi.nlm.nih.gov/gene/?term='+gene+'%20')
  site = bs4.BeautifulSoup(ncbi.text, "html.parser")
  elemList = site.select('span[class="geneid"]')
#  elemList = site.select('li a span')
  print(elemList)
  kegg_id = re.findall(': \d+', str(elemList))[0].replace(': ','')
#  kegg_id = re.findall('ath:.*?\d[^<]*', str(elemList))[0].replace('ath:','')
  outfile.write(gene + '\t' + kegg_id + '\n')

outfile.close()
