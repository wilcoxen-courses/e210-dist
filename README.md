# Exercise: Detailed Distributional Analysis

### Summary

This exercise examines the detailed distributional impacts of the tax
policy in the earlier microsimulation calculation.

### Input Data

File **households.csv** is a CSV version of the earlier file giving data 
on 1000 households. Unlike the earlier file, it has a header line giving
the name of the attribute in each column. File **quantities.csv** gives 
the quantities demanded by each household under the base case and tax policy 
simulations. In case you're curious, it was produced by running the earlier 
`ind_demand()` function for each equilibrium price and then writing out the 
output. However, you do not need to do that for this exercise: you can use
*quantities.csv* without recalculating it.

### Deliverables

Please prepare a script called **dist.py** that calculates the effective
tax rate (ETR) for each household and then reports the median ETR for 
the groups indicated below. Then update **results.md** replacing the 
TBD placeholders with your answers to the questions in the file.

### Instructions

1. Include the following import statements to bring in modules that will 
   be needed:
   ```
   import csv 
   import numpy as np 
   from collections import defaultdict
   ```
   The last one is new: it provides an enhanced dictionary that can have 
   a default value for new keys. It avoids the need for checking whether a 
   key is already in a dictionary before trying to use it.

**A. Reading the data files**

1. Define a function called `read_data` that takes two arguments: `filename`
   and `floatlist`. The first will be used for a file name to be read and 
   the second will be used to indicate which fields in each record should 
   be converted to numbers using `float()`. The function will read a CSV 
   file and return a dictionary of the data. The body of the function 
   should do the following:
   
   1. Open `filename` for reading using `fh` as the file handle.
   
   1. Create a `csv.DictReader()` object as shown below. Iterating over 
      this will return a series of dictionaries with field names 
      given by the first row of the file. It does in a single call what 
      you've done by hand before: trimming each line, splitting it into 
      fields, and then building a dictionary from the fields.
      ```
      reader = csv.DictReader(fh)
      ```
   1. Create an empty dictionary called `file_data`.
   
   1. Use a for loop with a running variable called `hh` to iterate
   over `reader`. Each time through the loop `hh` will be a dictionary with 
   information about one particular household. Within the loop do the 
   following:

       1. Use a for loop with a running variable called `field` to loop 
       over `floatlist`. Within the loop, set `hh[field]` to the 
       numeric value of itself returned by `float(hh[field])`.
   
       1. After the `field` loop finishes, create a variable called 
       `key` that is equal to the household's ID, which is in `hh['id']`.
       
       1. Then store `hh` in `file_data` using `key` as the key.
       
    1. After the `hh` loop finishes close `fh` and return `file_data`.
    
1. Create a variable `hh_info` that is the result of calling `read_data` 
   using `households.csv` as the filename and the list `['a','b','inc']` 
   for `floatlist`. Note that `a` and `b` won't be used below but we'll 
   convert them to numeric values in case the script were ever extended.
   
1. Create a variable called `qty_info` that is the result of calling 
   `read_data` on file `quantities.csv` and using `['qd1','qd2']` for 
   `floatlist`. `qd1` won't be used below but as before we'll convert it 
   to its numeric value for future use.

**B. Joining the datasets**
   
1. The next step is to join, or merge, the two datasets using the ID of the 
   household to match up the data. To do so, set up a for loop that uses a 
   running variable called `qty` to loop over the values in the `qty_info` 
   dictionary. Looping over the values rather than the keys is done by 
   using the `values()` call as shown below:
   ```
   for qty in qty_info.values():
   ```
   On each trip through the loop, `qty` will be a different entry from the 
   dictionary (that is, information from a different record in the quantities 
   file) and will have the values of `id`, `qd1` and `qd2` for one 
   household. Within the loop do the following:
   
    1. Create a variable called `id` equal to the ID for the current 
    household, which will be `qty['id']`.
       
    1. Create a variable called `hh` that is the entry in `hh_info`
    for household `id`.
       
    1. Set `hh['qd1']` and `hh['qd2']` to the corresponding values from
    `qty`.
    
    As you might guess, this is known as joining `qty_info` onto `hh_info`.

**C. Computing income quintiles and the ETRs**
       
1. After the `qty` loop completes `hh_info` will contain all the 
information about each household from the two files. We'll now extract the 
list of incomes and compute where the breaks between income quintiles fall. 
To do that, create a list called `incomes` that contains the value of 
`hh['inc']` for every household in `hh_info`. The easiest way to do it is 
to use a list comprehension but you can also do it using a regular for loop 
that iterates through `hh_info` and appends `hh['inc']` to a list.

1. Now use numpy's `percentiles()` call to find the breaks at the 
   quintile boundaries and call the resulting list `inc_cuts`. The call 
   should look like this:
   ```
   inc_cuts = np.percentile(incomes,[0,20,40,60,80])
   ```
   After the call `inc_cuts` will include 5 values: the minimum income for
   each quintile. The first will be the minimum income in the dataset, the 
   second will be the income at the 20th percentile, etc.    
   
1. Now we'll calculate the ETR for each household and also record 
   each household's income quintile while we're at it. Start by creating
   a variable called `pd1` that is equal to 53.35 and one called `pd2`
   equal to `55.27`. Then create a variable called `dp` that is equal to 
   `pd2` - `pd1`.
   
1. Next, set up a for loop using running variable `hh` to loop over
   `hh_info.values()`. Within the loop do the following:
   
   1. Set `hh['rev']` to the revenue burden on the household, which is `dp` 
   times `hh['qd2']`.
   
   1. Set `hh['etr']` to the household's ETR:100 times `hh['rev']` divided 
   by `hh['inc']`. Note that the 100 means the value will be a percentage, 
   so that 1 represents 1%.
   
   1. Set variable `quint` to 0. It will be used with the loop described 
   below to determine the income quintile for the household.
   
   1. Set up a for loop with running variable `min_inc` and looping over 
   `inc_cuts`. Within the loop include an if statement that checks whether
   `hh['inc']` is greater than or equal (`>=`) to `min_inc`. If so, add 1 
   to `quint`. That's all that will be in the for loop.
   
   1. After the `min_inc` loop, `quint` will be the quintile where the 
   household's income falls, where the first quintile is 1. At that point,
   set `hh['quint']` to the string version of `quint` via `str(quint)` to
   retain the information. Converting `quint` to a string will be handy 
   when printing out a sorted version of the data below.
   
**D. Grouping the results by type and quintile**

1. After the `hh` loop completes we'll aggregate the ETR results into three 
   sets of groups: (1) by type and quintile, (2) by quintile over all types,
   and (3) by type over all quintiles. The first step is to create a variable 
   called `grouped` to hold the grouped information. It will be a 
   `defaultdict` that automatically creates an empty list the first time 
   any given key is used. Use the call:
   ```
   grouped = defaultdict(list)
   ```
1. Now set up a for loop with running variable `hh` that loops over the
   values of `hh_info`. Within the loop do the following:
   
   1. Create a variable called `by_group` equal to a tuple consisting of 
   `hh['type']` and `hh['quint']`.
   
   1. Append `hh['etr']` to `grouped[by_group]`, which will a list set up
   automatically because `grouped` is a `defaultdict`.
   
   1. Then create a variable called `by_quint` that is equal to a tuple
   consisting of the string "all" and `hh['quint']` and append `hh['etr']`
   to `grouped[by_quint]`. This will have the effect of building one 
   list for each quintile that has all the ETRs for households in that 
   quintile.
   
   1. Then create a variable called `by_type` that is equal to a tuple
   consisting of `hh['type']` and "all" and use it in a similar way to
   append the household's ETR to the corresponding element of `grouped`.
   This will build a list of the ETRs of all households of each given type.

**E. Computing the median ETR for each group**

1. Now we'll compute the median ETR for each group of households. Start 
   by creating an empty dictionary called `medians`. Then use a for loop 
   with running variable `key` to iterate through `grouped`. Within the 
   loop, use numpy's `median()` call to calculate the group's median ETR
   from the list of individual ETRs in `grouped` as follows:
   ```
   this_median = np.median(grouped[key])
   ```
   Then round `this_median` to 2 decimal places and save it in `medians` 
   using key `key`.

**F. Printing the results and writing them up**

1. Print a header for the results along the lines of "type quint etr".

1. Use a for loop with running variable `key` and iterate over 
`sorted(medians)`. Within the loop use a print statement to write out 
`key[0]`, `key[1]` and `medians[key]`. The value of `key[0]` is the 
type and the value of `key[1]` is the income quintile.

1. Finally, look over the results and then use a text editor to fill 
in answers to the questions in **results.md**. Replace the "TBD" with 
your response. It's OK to be very concise: the goal is insights rather
than a detailed exposition.
   
### Submitting

Once you're happy with everything and have committed all of the changes to
your local repository, please push the changes to GitHub. At that point, 
you're done: you have submitted your answer.

### Tips

+ This exercise goes through one of the fundamental workflows of data 
analytics: joining datasets, calculating detailed results from the joined
data, grouping the results according to various attributes, applying one 
or more functions to the grouped data, and then reporting the results.
