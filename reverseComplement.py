#!/usr/bin/python

import sys

sekky = input('Enter the sequence: ')
rev_sekky = ''
for x in sekky:
	if x == 'A':
		rev_sekky += 'T'
	elif x == 'T':
		rev_sekky += 'A'
	elif x == 'G':
		rev_sekky += 'C'
	elif x == 'C':
		rev_sekky += 'G'
	else:
		rev_sekky += '*'

print ('The reverse sequence is: ' + rev_sekky[::-1])

while True:
        print ('Type exit to exit.')
        response = input()
        if response == 'exit':
                sys.exit()
        else:
        	print ('You typed ' + response + '.')
