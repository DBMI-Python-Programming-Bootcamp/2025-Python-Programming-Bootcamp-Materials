
## Conditional Tests

Python uses the values **True** and **False** to check on conditions. 

```python
mynum = 5
mysentence = "this is a sentence."

print(mynum > 4)
print(mysentence[0].islower())
```

```python
>>>mynum==5
True
```

```python
>>>mynum==10
False
```

Testing for equality is case sensitive in Python, so using lower() or upper() to help ignore the case of the value before doing the comparison:


### Checking for Inequality

We may use the exclamation point and an equal sign (!=) to determine if two values are not equal. Here is an example:


```python
>>>age=10
>>>age==10
True
>>>age==20
False
>>>age !=20
True
```

## Selection statements (If)

The last basic ingredient we haven't learned yet that is completely essential to expressing an algorithm in a programming language is selection:
the ability to have the program choose what to do next based on some condition. You will recall that when we started out last week talking about algorithms, we were saying things like "If the first number is greater than the second, then... answer NO". Today we will look at how to make choices like this in Python using **if** statements.


### Introducing if
Here's an extremely simple example that uses an if statement:

```python
if mynum > 4:
    print("Yes")
else:
    print("No")
```


This example is so simple it's almost useless! We know what the value of **mynum** is because we just assigned it. Here's another example:

```python
if mysentence[0].islower():
    mysentence = mysentence[0].upper() + mysentence[1:]
```

What does this code do? It capitalizes a sentence if it's not already capitalized. There's no **else** part -- if the sentence is already in the right format we leave it alone.


### Parts of an if/else

You will notice that, just as with **for** loops, there is an indented structure to our **if** statements.

The condition is the part of an if statement that comes right after the keyword **if**. This will always need to be the sort of thing that could be either True or False:

If the condition is true, then the indented part below the if is executed. We will call this indented part under the if the "body" of the if statement.
If the condition is not true (false), then body of the if statement is skipped. If the code includes an *else* part, then the else body is executed.

Python does not require an **else** block at the end of an **if** statement, it is only a useful option


### If/else with lists

If/else statement is often used in for loops that handle most items in a list in one way but handle certain items with specific values in a different way. The following code
loops through a list of programming languages and looks for the value 'sql'. Whenever the value is 'sql', it is printed in uppercase instead of title case:

```python
programming_languages = ['java','c++','c#','sql','pascal']

for pl in programming_languages:
    if pl == 'sql':
        print(pl.upper())
    else:
        print(pl.title())
```
 
To make these more useful, let's combine them with a loop that operates on a patient list. 

```python
# a list of lists representing patients.
# we will use something better than lists for data like this eventually
# the fields here are: MRN, Birthyear, SSN, Given name, Family name, Zip code
patlist = [[7182, 1989, '999-76-5071', 'Edgar', 'Hermann', 72034],
           [7491, 2018, '999-92-3312', 'Dionna', 'Heathcote', 72411],
           [7052, 2013, '999-80-4418', 'Eleni', 'Gusikowski', 72736],
           [4851, 2011, '999-51-6410', 'Ricardo','Mills', 72046],
           [1744, 1969, '999-72-5953', 'Michelle','Breitenberg', 72472]]
```

What if we wanted to know which patients were over 30 and which were under 30 years of age?


```python
for p in patlist:
    age = 2025 - p[1]
    if age > 30:
        print(f"{p[3]} {p[4]} is over 30")

```

That version only prints a message if the patient is over 30. We can use else to print an appropriate message either way:

```python
for p in patlist:
    age = 2025 - p[1]
    if age > 30:
        print(f"{p[3]} {p[4]} is over 30")
    else:
        print(f"{p[3]} {p[4]} is under 30")

```

Note also that we don't strictly need to store the age in a variable. We could get the same result with this code:

```python
for p in patlist:
    if (2025 - p[1]) > 30:
        print(f"{p[3]} {p[4]} is over 30!")
    else:
        print(f"{p[3]} {p[4]} is under 30!")
```

Of course we don't **need** an if statement to calculate someone's age or compare their age to another number. We only need the if (if/else) when we want to do something different based on the result of the comparison:

```python
for p in patlist:
    print(p[3])
    print(f'\tage calculation: {2025 - p[1]}')
    print(f'\tage greater than 30?: {(2025 - p[1]) > 30}')

```

### Quick In-class Exercise 

Using the patient list example, create a new list that will have only those who are above 18 years old

Define a list of integers and use a combination of **for** and **if** statements to find if each number in the list is even or odd!



### Elif - checking more than one condition


Sometimes we'll want our code to pick among more than two actions depending on conditions. For example, maybe it's more useful to detect when people are in different decades of their lives than to just detect whether they are over or under a specific age.

```python
for p in patlist:
    age = 2025 - p[1]
    if age < 18:
        print(f"{p[3]} {p[4]} is a minor")
    elif age < 30:
        print(f"{p[3]} {p[4]} is in their twenties")
    elif age < 40:
        print(f"{p[3]} {p[4]} is in their thirties")
    else:
        print(f"{p[3]} {p[4]} is forty or over")
```


### And, or, not

We can use the logical operators **and**, **or**, and **not** in Python to create even more complex conditional expressions.

For example, let's say we just want to find people who are in their thirties but we are not interested in listing out all the other possibilities.
That is, we want people that are both  older than 29 and younger than 40:


```python
for p in patlist:
    age = 2025 - p[1]
    if (age > 29) and (age < 40):
        print(f"{p[3]} {p[4]} is in their thirties")
```

Here's an example that uses **or** to get people in two age categories:

```python
for p in patlist:
    age = 2025 - p[1]
    if (age < 18) or (age > 50):
        print(f"{p[3]} {p[4]} is NOT in the middle age {age}")
```

And here we use **not** just to exclude minors:

```python
for p in patlist:
    age = 2025 - p[1]
    if not(age < 18):
        print(f"{p[3]} {p[4]} is an adult")
```

Note that checking **not(age < 18)** is really the same as checking **age >= 18**.


### Break
The Python keyword *break* can be used to stop a loop before it would otherwise end naturally.
For example, let's say we wanted to find the first person in our list whose first name starts with 'R', and then stop looking:


```python
# for every patient in the list
for p in patlist:
    # get the first and last name and store them for easy reference in the rest of the loop
    fname = p[3]
    lname = p[4]
    
    if not fname.startswith('R'):
        print(f"{fname} {lname} does not have a first name that starts with 'R'!")
    else:
        print(f"{fname} {lname} DOES have a first name that starts with 'R'!")
        break # stop the loop once we do find someone whose name starts with 'R'
```




### Here's one more way to loop through a list:

```python
alist = [1, 2, 3, 5, 9, 1005]
for i in range(len(alist)):
    print(f"the value at index {i} is {alist[i]}")
```

This produces the same output as the following, which will look more familar:


```python
for i, n in enumerate(alist):
    print(f"the value at index {i} is {n}")
```

Let's take a moment to explore how the version with range works.

Note that it is often more convenient to just let enumerate assign each list index and list item to two separate variables.
In a case where we want the loop to examine more than one value from the list at a time, the *range(len(..))* version may be more appropriate.


Let's say we want the loop body to print out every number and the number that comes after it, like this:


```python
for i in range(len(alist)):
    print(f"the value at index {i} is {alist[i]}")
    print(f"the next number, which is at index {i + 1} is {alist[i + 1]}")
```

That code actually doesn't work. Why not? Let's figure it out and fix it together before the exercise.



2025 Summer Python Programming Bootcamp - In-class Exercise 3
========

## Introduction
For this in-class exercise, we will divide up into breakout groups of 2-4 students. One student in each group will volunteer to "drive" PyCharm, and the group will
work together on the exercise outlined below. There is no submission step for this exercise, but we will bring the groups together to discuss the exercise at the end. One student from each group should be prepared to share the group's work with the rest of the class.


## Exercise
Let's say we want to be able to tell whether a list of numbers is sorted. We've discussed this example before, but now that we know about *if*, we can start working on it.
For this in-class exercise, we will bring together what we have learned recently about lists, loops, and selection statements to create code that can tell us whether a list of numbers is sorted or not.

### Part 1
Write a loop that will go through a list, print out every pair of numbers, and print a message with each pair saying whether they are in the correct order.

For example, if your loop sees this list:

```python
alist = [1, 2, 3, 1005, 9, 5]
```

It should print messages like the following:

```python
Comparing 1 and 2
1 is not greater than 2, so they're ok
Comparing 2 and 3
2 is not greater than 3, so they're ok
Comparing 3 and 1005
3 is not greater than 1005, so they're ok
Comparing 1005 and 9
1005 is greater than 9, so they're not in order
Comparing 9 and 5
9 is greater than 5, so they're not in order
```

You'll probably want to test your loop with a list that is in order as well.
That's a little tricky because your loop uses the name of the variable that holds the list.
You can address that either by making another copy of your loop and changing the variable name, or by just changing what list is in the variable.
Here's an in-order list for you:

```python
alist = [1, 2, 3, 5, 9, 1005]
```

### Part 2
Write a new version of your loop that just lets us know if a list is out of order, and why.
If your loop figures out that the list is out of order, it should say so and stop looking, e.g.

```python
1005 is greater than 9, so the list is out of order. I'm done!
```


### Part 3 (time allowing)
Can you figure out how to make a loop that will output an appropriate message informing us when the list IS in order?


