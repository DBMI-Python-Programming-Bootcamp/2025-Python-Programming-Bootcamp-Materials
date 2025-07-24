# 2025 Summer Python Programming Bootcamp - Assignment 05

## DUE Tuesday, July 29 @ 3:00PM Central


Part 0: Setup
======
In PyCharm, create a new Python script names "assignment05.py".
Write all of your Python code for the below steps in the *assignment05.py* file.
You will add Python code to this file and then submit it using Box, as described below. Make sure to try running your code as you work your way through these.


### Example data
This assignment asks you to create functions that calculate blood pressure categories based on systolic and diastolic blood pressure readings. In real-world patient records, there are usually several such readings for each patient over time. For this assignment, use the below dict of example patient data, which has one systolic and one diastolic blood pressure readings for each patient.

```python 
patlist = [{'mrn': 7182, 'birthyear': 1989,
            'fname': 'Edgar', 'lname': 'Hermann',
            'zip': 72034,
            'systolic_bp': 166.6, 'diastolic_bp': 110.6},
           {'mrn': 7491, 'birthyear': 2018,
            'fname': 'Dionna', 'lname': 'Heathcote',
            'zip': 72411,
            'systolic_bp': 91.8, 'diastolic_bp': 70.9},
           {'mrn': 7052, 'birthyear': 2013,
            'fname': 'Eleni', 'lname': 'Gusikowski',
            'zip': 72736,
            'systolic_bp': 132.0, 'diastolic_bp': 72.4},
           {'mrn': 4851, 'birthyear': 2011,
            'fname': 'Ricardo', 'lname': 'Mills',
            'zip': 72046,
            'systolic_bp': 190.7, 'diastolic_bp': 102.3},
           {'mrn': 1744, 'birthyear': 1969,
            'fname': 'Michelle', 'lname': 'Breitenberg',
            'zip': 72472,
            'systolic_bp': 164.0, 'diastolic_bp': 68.7}]
```


### Example function
```python
def normal_bp_range(systolic, diastolic):
    """Takes as input a systolic and diastolic blood pressure reading, 
    and returns True if the values are in Normal range, False otherwise.
    See https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings
    """
    if (systolic < 120) and (diastolic < 80):
        return True
    elif:
        return False
```


# Part 1: Applying to patients
Using a loop, the *normal\_bp\_range* function, and the *patlist* structure above, 
print out a message for each of the patients in *patlist* stating whether their blood pressure is in the normal range or not. Example output:

```python 
Edgar Hermann does NOT have blood pressure in the normal range
Dionna Heathcote has blood pressure in the normal range
Eleni Gusikowski does NOT have blood pressure in the normal range
Ricardo Mills does NOT have blood pressure in the normal range
Michelle Breitenberg does NOT have blood pressure in the normal range

```


# Part 2: Printing blood pressure categories
Define a new function named *print\_bp\_range* that takes as input a systolic and diastolic blood pressure reading and, using if/elif/../else, will print out the matching blood pressure category (one of NORMAL, ELEVATED, STAGE 1 HYPERTENSION, STAGE 2 HYPERTENSION, HYPERTENSIVE CRISIS) based on the ranges defined in [https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings](https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings).

**Hint:** there's something interesting about the way these blood pressure categories are listed in that table. Thinking about how Python *if/elif/else* statements work, a direct translation of the below might not work perfectly for readings that would indicate hypertensive crisis *because a value like 181 is both higher than 180 and higher than 140*. 

| Category | Systolic | Diastolic |
| ---------|----------|-----------|
| HIGH BLOOD PRESSURE (HYPERTENSION) STAGE 2 | 140 or higher | 90 or higher |
| HYPERTENSIVE CRISIS | Higher than 180 | Higher than 120 |


Make sure to test your function to check its output with several different values, e.g.:

```python 
>>> print_bp_range(110, 70)
Normal
>>> print_bp_range(125, 70)
Elevated
>>> print_bp_range(145, 93)
Stage 2 hypertension
>>> print_bp_range(175, 125)
Crisis
```

Once you're confident the function is behaving as intended, use a loop to output a message about each example patient's blood pressure category. Note that because the function is printing its own message, it might not be possible to output each patient's info on a single line. That's okay at this step. Example output:


```python
Edgar Hermann's BP category is:
Stage 2 hypertension
Dionna Heathcote's BP category is:
Normal
Eleni Gusikowski's BP category is:
Stage 1 hypertension
Ricardo Mills's BP category is:
Crisis
Michelle Breitenberg's BP category is:
Stage 2 hypertension
```


# Part 3: Returning blood pressure categories
Define a new function named *get\_bp\_range* that takes as input a systolic and diastolic blood pressure reading and, using if/elif/../else, will *return* the matching blood pressure category as a *string* value.

When a function successfully returns a value, you can store that value and use it later. Here is an example:


```python
>>> x = get_bp_range(145,95)
>>> print(x)
Stage 2 hypertension
```

Once this function is working, use a loop to output a message about each example patient's blood pressure category with one line of output per patient. Example output:

```python
Edgar Hermann's BP category is: Stage 2 hypertension
Dionna Heathcote's BP category is: Normal
Eleni Gusikowski's BP category is: Stage 1 hypertension
Ricardo Mills's BP category is: Crisis
Michelle Breitenberg's BP category is: Stage 2 hypertension
```


# Submission

To submit *assignment05.py*, drag it into your Bootcamp submissions Box folder.