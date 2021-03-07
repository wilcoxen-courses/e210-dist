#! /bin/python3
#  Spring 2020 (PJW)
#
#  Illustrate the use of tuples
#

#
#  A list of example data: months of the year
#

months = ['January','February','March', 'April','May','June',
          'July','August','September', 'October','November','December']

#
#  Set up a dictionary that will let us sort the months 
#  by the length of the name and then the name itself.
#

by_len_name = {}

#
#  Step through the months. Enumerate returns a sequence
#  of tuples, one for each item in the list, where the 
#  first element is the index of the item and the second
#  is the item itself.
#

for (n,name) in enumerate(months):
    
    #  Create a tuple with the name's length and the name
    
    this_key = ( len(name), name )
    
    #  Store a short message as the value. Not very interesting
    #  but shows that expressions can be used in f-strings
    
    by_len_name[this_key] = f"{name} is month {n+1}"

#%%
#
#  Print it without sorting
#

print( "\nUnsorted (in order created):\n")
print( "tuple key : value")
for key in by_len_name.keys():
    print( key, ':', by_len_name[key] )

#%%
#
#  Print it sorted by key. Sorts first by length and then 
#  alphabetically by name.
#

print( "\nSorted (by length and name):\n")
print( "tuple key : value")
for key in sorted( by_len_name.keys() ):
    print( key, ':', by_len_name[key] )
