#! /bin/python3
#  Spring 2021 (PJW)
#
#  Illustrate grouping and aggregation
#

import csv
import numpy as np
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

#
#  Now print what we found. Use an f-string for nice formatting. Variable
#  names within the string will automatically be replaced by their values.
#

for tz in sorted( by_zone.keys() ):
    states = ', '.join( sorted(by_zone[tz])  )
    print( f"Time zone {tz}: {states}" )

#%%
#
#  More elaborate example: computing the median population density of 
#  counties by state and sorting the results.
#

#
#  Read the county data into a list, computing the density along the way
#

rec_list = []

fh = open('example_data.csv')
reader = csv.DictReader(fh)

for rec in reader:  
    this_state = rec['state']
    this_km2 = float(rec['ALAND'])/1e6
    this_pop = float(rec['pop'])
    rec['density'] = this_pop/this_km2
    rec_list.append( rec )

#%%
#
#  Now walk through the list and collect the densities into groups 
#  by state
#

by_state = defaultdict(list)

for rec in rec_list:
    this_state = rec['state']
    this_density = rec['density']
    by_state[ this_state ].append( this_density )

#%%
#
#  Now walk through the state groups we just built and compute the median 
#  density. Combine the density and the state name into a tuple and store 
#  it in a list.
#

by_density = []

for state in by_state.keys():
    
    #  Get the state's list 
    
    this_list = by_state[state]
    
    #  Compute the median and round it 
    
    med_density = round( np.median(this_list), 2 )
    
    #  Build a tuple with the result and the name. This will allow 
    #  the results to be sorted very easily.
    
    this_tuple = (med_density,state)
    
    #  Add the tuple to the list.
    
    by_density.append( this_tuple )
    
#%%
#
#  Now sort the list of tuples and print them. Will sort first by density
#  then by state name since that's the order of items in the tuple. Print 
#  the out with the name first since that's easier to read.
#

print( "\nMedian county population density by state")
print( "Individuals per square km\n" )

for (den,state) in sorted(by_density):
    print( f"{state}: {den}" )