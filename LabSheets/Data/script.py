#!/usr/bin/env python
import csv
import random

#f = open("W08_D02.txt", "w")
#csvfile = csv.writer(f)
#
#for i in range(50):
#    csvfile.writerow([random.randint(2, 50) for  i in range(50)])
#
#f.close()

import urllib
from scipy import misc
file='http://www.itbhuglobal.org/chronicle/732-Hubble2.png'
urllib.urlretrieve(file, 'image.png')
image = misc.imread('image.png',flatten=True)
image = list([list(r) for r in image])

f = open("W08_D02.txt", "w")
csvfile = csv.writer(f)

for row in image[:501]:
    csvfile.writerow(row)

f.close()
