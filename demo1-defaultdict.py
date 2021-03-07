#! /bin/python3
#  Spring 2020 (PJW)
#
#  Illustrate the use of defaultdict and grouping records
#

import csv
from collections import defaultdict

#
#  Build a list of some sample data
#

lines = [ 
    "name,timezone",
    "New York,ET",
    "New Jersey,ET",
    "Texas,CT",
    "Illinois,CT",
    "Colorado,MT", 
    "Utah,MT",
    "California,PT",
    "Washington,PT"
    ]

#
#  Set up a DictReader to parse the data
#

reader = csv.DictReader(lines)

#
#  Read it all into a list and then print the list
#

data_list = [rec for rec in reader]

for rec in data_list:
    print( rec )

#%%
#
#  Now group the states by time zone. Create a dictionary where each key will 
#  be a timezone and each value will be a list of states in that timezone.
#  Use a default dictionary so that empty lists will automatically be created
#  on the fly.
#

by_zone = defaultdict(list)

for rec in data_list:
    tz = rec['timezone']
    by_zone[tz].append( rec['name'] ) 

#%%
#
#  Now print what we found. Use an f-string for nice formatting. Variable
#  names within the string will automatically be replaced by their values.
#

for tz in sorted( by_zone.keys() ):
    states = ', '.join( by_zone[tz] )
    print( f"Time zone {tz}: {states}" )
    