#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s.endswith('AM'):
        if s[:2] == '12':
            return '00' + s[2:-2]
        else: 
            return s[:-2]
    elif s.endswith('PM'):
        if s[:2] == '12':
            return s[:-2]
        else:
            hour = int(s[:2]) + 12
            hour = str(hour)
            return hour + s[2:8]
    else:
        return s

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)

