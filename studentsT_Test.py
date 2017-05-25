#!/anaconda/bin/python3/
#This program takes two means and variances, and performs a student's t-test on them
#Used to compare qPCR data of two samples

import math
import sys
Mu_1 = input('Enter first (largest) mean: ')
Mu_2 = input('Enter second (smallest) mean: ')

std_dev1 = float(input('Enter first variance: '))
std_dev2 = float(input('Enter second variance: '))

N1 = int(input('Enter first sample size as an integer: '))
N2 = int(input('Enter second sample size as an integer: '))

#Compute difference of means
Mu_12 = (float(Mu_1) - float(Mu_2))
print ('The difference of the means is: ' + str(Mu_12) + '.')

#Compute standard error or variance of the means
var = math.sqrt(((N1-1)*(std_dev1 ** 2) + (N2-1)*(std_dev2 ** 2))/(N1+N2-2))
print ('The variance of the means is: ' + str(var) + '.')

#Compute degrees of freedom
freed = (N1 + N2 - 2)
print ('The degrees of freedom is: ' + str(freed) + '.')

#Compute t-value
t = Mu_12 / (var * math.sqrt(1/N1 + 1/N2))
print ('The t value is: ' + str(t) + '.')

#Compute p-value
print ('')
print('Go here and input your data to get your p-value: http://onlinestatbook.com/2/calculators/t_dist.html')

while True:
        print ('Type exit to exit.')
        response = input()
        if response == 'exit':
                sys.exit()
        else:
        	print ('You typed ' + response + '.')
