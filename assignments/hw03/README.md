2025 Summer Python Programming Bootcamp - Assignment 03
========
DUE Tuesday, July 22 @ 3:00PM Central
----------------------------



Introduction
============
In PyCharm, create a new Python script called "assignment03.py"


Write all of your Python code for the below steps in the *assignment03.py* file.
You will add Python code to this file and then submit it using BOX, as described below.
Make sure to try running your code as you work your way through these steps.




Sequences and selections
====

For this assignment we will work with a small set of example data pulled from the Arkansas Department of Health COVID-19 site on county-level vaccination rates in 2021 (early in the COVID-19 pandemic).
The following code creates a variable that stores a list of tuples. Each tuple has a county name (_str_) and the percentage of persons over age 12 in that county who are fully vaccinated against COVID-19.

```python
vacc_counties = [('Pulaski', 42.7), 
                 ('Benton', 41.4), 
                 ('Fulton', 22.1), 
                 ('Miller', 9.6), 
                 ('Mississippi', 29.4)]
```

You may copy this code into your Python file. Though you may not have experience working with lists of tuples, you do have experience from our in-class exercises working with lists of lists. There is no real difference for the purpose of this exercise.


# Part 1
Add Python code to do the following:

* Using _append_, add one more tuple to _vacc\_counties_ that represents an additional county and its vaccination rate. You may use Scott County, which at this point in time had a rate of 28.1%, or you may make up another example if you prefer.



# Part 2
Add Python code to do the following:

* Using a _for_ loop and an _if_ statement, go through _vacc\_counties_ and print out a message for those counties that have a higher than 30% vaccination rate. Example output:

```python
Pulaski is doing ok, with a rate of 42.7%
Benton is doing ok, with a rate of 41.4%
```

# Part 3
Add Python code to do the following:
* Add another loop that prints out a message for every county, but prints different messages if the rate is above or below 30. Example:

```python
Pulaski County is doing ok, with a rate of 42.7%
Benton County is doing ok, with a rate of 41.4%
Fulton County is doing less ok, with a rate of 22.1%
Miller County is doing less ok, with a rate of 9.6%
Mississippi County is doing less ok, with a rate of 29.4%
Scott County is doing less ok, with a rate of 28.1%
```


# Bonus Round
Can you write code that uses a loop and calculates the mean vaccination rate across this list?




Submission
======
To submit this file, simply drag it into your Bootcamp BOX folder.