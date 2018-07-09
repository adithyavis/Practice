#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    l1=t1.split(' ')
    l2=t2.split(' ')
    x1=l1[4].split(':')
    x2=l2[4].split(':')
    difference=0
    if(l1[-1][0]=='+'): l1[-1]=float(l1[-1][1:3])+  float(l1[-1][3:])/60
    else: l1[-1]=-float(l1[-1][1:3])- float(l1[-1][3:])/60
    if(l2[-1][0]=='+'): l2[-1]=float(l2[-1][1:3])+ float(l2[-1][3:])/60
    else: l2[-1]=-float(l2[-1][1:3])- float(l2[-1][3:])/60
    difference= difference- (l1[-1]-l2[-1])*60*60
    
    difference= difference+(float(l1[1])-float(l2[1]))*24*60*60
    difference=difference+(float(x1[0])-float(x2[0]))*60*60+(float(x1[1])-float(x2[1]))*60+(float(x1[2])-float(x2[2]))
    return str(int(abs(difference)))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()