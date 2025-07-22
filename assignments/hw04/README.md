2025 Summer Python Programming Bootcamp - Assignment 04
========
DUE Friday, July 25 @ 3:00PM Central
----------------------------

Part 0: Setup
======
In PyCharm, create a new Python script names "assignment04.py".
Write all of your Python code for the below steps in the *assignment04.py* file.
You will add Python code to this file and then submit it using Box, as described below. Make sure to try running your code as you work your way through these.



Part 1 : Dictionary basics
======
* Create a variable called _info_ and assign it a _dict_ that stores your first and last name.
Remember that dict keys don't mean anything for Python -- like variable names, they are just there to help us know what information is being stored.

For example:

```python
info = {'fname': 'Jonathan', 'lname': 'Bona'}
```


* Add a _print_ statement that gets the parts of your name out of this dictionary and prints out your full name. Example output:

```
My full name is Jonathan Bona

```

Part 2 : Adding to a dictionary
======

* Using an assignment statment, add a new key/value pair to your dictionary that stores some of your favorite foods. The key should be the string "foods", and the value should be a list of strings that name three or more foods.

* After adding the list of foods, print out your _info_ dict to look at its contents. Here's an example of what the print statement might produce as output:

```
{'fname': 'Jonathan', 'lname': 'Bona', 'foods': ['durian', '臭豆腐', 'hákarl']}
```

* Add a _print_ statement that prints out a message with your full name, a count of the number of foods, and the list of foods. For example:


```
My full name is Jonathan Bona and I like 3 foods: ['durian', '臭豆腐', 'hákarl'] 
```



Part 3 : Dictionaries, lists, loops, and if
=====

You should use the following list of dictionaries for your code in this part.

```python
patlist = [{'mrn': 7182, 'birthyear': 1989, 'ssn': '999-76-5071', 'fname': 'Edgar', 'lname': 'Hermann', 'zip': 72034},
           {'mrn': 7491, 'birthyear': 2018, 'ssn': '999-92-3312', 'fname': 'Dionna', 'lname': 'Heathcote', 'zip': 72411},
           {'mrn': 7052, 'birthyear': 2013, 'ssn': '999-80-4418', 'fname': 'Eleni', 'lname': 'Gusikowski', 'zip': 72736},
           {'mrn': 4851, 'birthyear': 2011, 'ssn': '999-51-6410', 'fname': 'Ricardo', 'lname': 'Mills', 'zip': 72046},
           {'mrn': 1744, 'birthyear': 1969, 'ssn': '999-72-5953', 'fname': 'Michelle', 'lname': 'Breitenberg', 'zip': 72472}]
```

* Add a _print_ statement that prints out just the first element in the list (this is the dict for Hermann Edgar). Example output:

```
{'mrn': 7182, 'birthyear': 1989, 'ssn': '999-76-5071', 'fname': 'Edgar', 'lname': 'Hermann', 'zip': 72034}
```

* Add a _print_ statement that gets the first element in the list and prints out the 'ssn' field. Example output:

```
999-76-5071
```

* Add a _for_ loop that prints out the _ssn_ value for every dict in this list. Example output:

```
999-76-5071
999-92-3312
999-80-4418
999-51-6410
999-72-5953

```

* Add a _for_ loop that uses this list of dicts to print out a message for every person under the age of 18. Example output:

```
Dionna Heathcote is a minor.
Eleni Gusikowski is a minor.
Ricardo Mills is a minor.
```



Submission
======
To submit this file, drag it into your bootcamp submissions Box folder.