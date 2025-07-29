# 2025 Summer Python Programming Bootcamp - Assignment 06

## DUE Thursday, July 31 @ 3:00PM Central

### Part 0: Setup
In PyCharm, create a Python script named "assignment06.py". 

Write all of your Python code for the below tasks in the *assignment02.py* file.

### Part 1: Converting Code to Functions

Here is code that generates the first ten digits of the Fibonacci sequence.

```python
my_list = [0, 1, 1]  
while len(my_list) < 10:  
    my_list.append(my_list[-2] + my_list[-1])
```

This will generate the first ten digits of the Fibonacci sequence.

In Lecture 06 and 07, we discussed functions. Create a function called **fib_list**. This function will take one parameter *n* and should return a list of length *n* that contains the digits of the Fibonacci sequence.

Here are some examples using it:
```bash
fib_list(5)
[0, 1, 1, 2, 3]
fib_list(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
fib_list(15)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
fib_list(20)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
```

### Part 2: Functions in Functions 

In Lecture 07, we implemented a Monte Carlo method to calculate statistics on rolling dice. As a reminder and way to get started, here's the code to make one random roll.

```python
import random
x = random.randint(1,6)
```

We also made a function to do this called `roll_dice` that returned a list of dice rolls.

```python
def roll_dice(num_dice):  
    dice_list = []  
    for roll_num in range(0, num_dice):
	    dice_list.append(random.randint(1,6))
	return dice_list
```

The output should look something like this:

```bash
print(roll_dice(1))
[4]
print(roll_dice(2))
[2, 4]
print(roll_dice(3))
[2, 3, 1]
print(roll_dice(3))
[3, 5, 4]
print(roll_dice(10))
[2, 6, 1, 6, 5, 3, 4, 1, 6, 2]
```

Now, let's repeat part of our in-class exercise, where we calculated and printed the average roll. This time we'll create a function to do it, called `calc_average_roll`. This function will have one parameter called `num_dice` and it should return the average roll. 

> **Note:** You may (but don't have to) use the `roll_dice` function provided inside `calc_average_roll`.

You should then be able to use it like so:

```python
num_dice = 1000
print(f"The average roll of the dice after rolling {num_dice} dice is {calc_average_roll(num_dice)}")
```

You can change the *num_dice* parameter. Your output should look something like:
```bash
The average roll of the dice after rolling 100 dice is 3.93
The average roll of the dice after rolling 1000 dice is 3.506
The average roll of the dice after rolling 10000 dice is 3.4688
The average roll of the dice after rolling 100000 dice is 3.50699
```

> **Note:** as we discussed in class don't set **num_dice** too high, or it may exceed your computer's resources. 

### Part 3 (Optional):
This task may be a bit more challenging, so don't feel like you have to do it.

Make a new function called `format_list`. This function should take a list as a parameter and format it in a way that it can be used in a sentence.

For example:
```python
print(f"I like animals. Especially {format_list(['cats','dogs','birds'])}.")
```

Should output:
```bash
I like animals. Especially cats, dogs, and birds.
```

> **Note:** You need to make sure this works irrespective of the length of the list!

For example:
```bash
print(f"I like animals. Especially {format_list(['cats','dogs','birds'])}.")
I like animals. Especially cats, dogs, and birds.

print(f"I like animals. Especially {format_list(['cats','dogs','birds','hamsters'])}.")
I like animals. Especially cats, dogs, birds, and hamsters.

print(f"I like animals. Especially {format_list(['cats','dogs'])}.")
I like animals. Especially cats and dogs.

print(f"I like animals. Especially {format_list(['cats'])}.")
I like animals. Especially cats.
```

### Part 4: Submission
Please submit this file on Box. 
