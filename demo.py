#! /bin/python3
#  Spring 2020 (PJW)
#
#  Illustrate the use of csv.DictReader and defaultdict
#

import csv
import json
from collections import defaultdict

#
#  Some sample data
#

lines = [ 
    "name,timezone\n",
    "New York,ET\n",
    "New Jersey,ET\n",
    "Texas,CT\n",
    "Illinois,CT\n",
    "Colorado,MT\n", 
    "Utah,MT\n",
    "California,PT\n",
    "Washington,PT\n"
    ]

#
#  Create a dictionary that will be lists of locations
#  in each timezone

by_zone = defaultdict(list)

#
#  Create a DictReader object
#
reader = csv.DictReader(lines)

#
#  Read the file
#

for rec in reader:
    print( json.dumps(rec,indent=4) )
    key = rec['timezone']
    by_zone[key].append( rec['name'] ) 

#%%

print( json.dumps(by_zone,indent=4) )



    