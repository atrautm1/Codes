#!//anaconda/bin/python3

f = open("hw5.vcf.out", 'w')				# New file to write data to
g = []										# Empty list to place file
with open('hw5.vcf') as file:				# Open the file as file
	for line in file:						# For each line in the file
		if line.startswith(('#C','20')):	# If the line starts with #C and/or 20
			g.append(line.split('\t'))		# Append the line to the list splitting it at the tab
		else:								# Otherwise, continue iterating through the lines
			continue

for col in g:								# For each col in list "g"
	d = ''									# Empty string d to append ancestral allele
	i = 9									# Numerical value to start the counting
	while i in range(9,20):					# While loop because I'm lazy
		d += col[i].split(':')[0]+'\t'		# Split string by the ":" and add ancestral allele sequence to "d"
		i = i+1								# So that "while" doesn't go on forever
	e = ''.join(col[0]+':'+col[1])
	f.write(col[2]+"\t"+e+'\t'+				# write the columns to the new file
		col[3]+'\t'+col[4]+"\t"+d + '\n')	
f.close()



 