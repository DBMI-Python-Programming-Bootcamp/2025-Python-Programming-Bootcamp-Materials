# Dictionaries (dict)

In Python, dictionaries - *dict*s - are a very useful data structure for storing groups of related information. 

So far we have been representing collections of information using sequences -- mostly lists.
For example, we've represented sets of patient characteristics (mrn, birthdate, ssn, first name, etc) using lists like this:

```
pat1 = [7491,	2018, '999-92-3312', 'Dionna', 'Heathcote', 72411]

```

A serious limitation of this approach is that it requires the programmer, or someone else reading the code, to *remember* that the item at index 0 is an MRN, 
the item at index 5 is a last name, etc. It's easy to lose track of what is what, and it's easy to make mistakes.

Here's an example dict that stores the same information in a more explicit way, as a series of *key* and *value* pairs:

```
pat1 = {'mrn' : 7491,
         'birthdate' : 2018,
         'ssn' : '999-92-3312',
         'fname' : 'Dionna',
         'lname' : 'Heathcote',
         'zip' :  72411}

```

The code creates a dictionary and stores it in a variable named pat1. 


```
pat1 = {'mrn' : 7491, 'birthdate' : 2018,'ssn' : '999-92-3312','fname' : 'Dionna','lname' : 'Heathcote','zip' :  72411}

```

This code does the exact same thing, but in a way that is harder to read.
Just as with lists, we are allowed to put dictionary elements on separate lines.

---
# <ins>Key-Value Pairs</ins>: 

Each element of a dictionary is a key-value pair.

Here the dictionary is called *pat1* and the keys are *mrn*, *birthdate*, *ssn*, etc. The values are the patient's mrn, birthday and social security number.

Note the use of the curly braces (this indicates it's a dict). *Don't confuse this use of curly braces with the use in format strings.*

Note also the use of the colon to separate each key from its value.

Each key/value pair is separated from the next one by a comma. 

Keys always go to the left of the colon, values go to the right. This is similar to how variable names always go on the left in an assignment statement.


Each key is connected to its value, and we can use the key, in combination with the name of the variable storing the dict, to access this value:

```python
print(pat1['fname'])
```

**Dicts are mutable**

We can add new key/value pairs to any existing dict. Note that the *values* stored can be just about anything: strings, integers, even lists (or other dicts).

```python
pat1['sex'] = "Female"
pat1['age'] = 7
pat1['conditions'] = ["measles", "fever"]
pat1(an_element)
```

Alternatively, if we already know all the things we want to put into a dict initially, we can add those key and values in a single statement:

```python
pat2 = {'mrn': 7182,
        'birthyear': 1989,
        'fname': 'Edgar',
        'lname': 'Hermann',
        'age' : 35,
        'sex' : 'Male',
        'conditions' : ['type ii diabetes', 'eczema'],
        'zip': 72034}
```


Note that in these examples the keys are all strings. 
It's good to use descriptive strings for dictionary keys because that makes it a little easier to see what the code is doing just by looking at it. 


Python requires dictionary keys to not be *mutable*.

---
# <ins>Keys vs. Positions</ins>

As we've seen above, values in a dictionary are accessed via their keys, *not by their position*. One nice thing about this is that it means the order of elements in a dictionary doesn't matter. We saw this above, where *pat1* and *pat2* have their elements listed in different orders.

```python
print(pat1['fname'])
```
vs.

```python
print(pat1[0])
```


Of course if we have a list within a dict, the items in the list are accessed using their indices, just like any other list:

```python
print(pat1['conditions'])
print(pat1['conditions'][0])
```

It can be confusing, especially for beginners, to deal with nested data structures, like a dict that has a list as one of its values. 
Sometimes it may help to pull information out and store it in another variable.


Compare:
```python
print(f"{pat1['fname']} {pat1['lname']} has {len(pat1['conditions'])} listed conditions. The first is: {pat1['conditions'][0]}")
```

vs



```python
p2_fullname = pat2['fname'] + ' ' + pat2['lname']
p2_conds = pat2['conditions']
p2_age = pat2['age']
print(f"{p2_fullname} has {len(p2_conds)} listed conditions. The first is: {p2_conds[0]}")
```

If a *value* stored in a dict is mutable, we can change it directly:

```python
pat1['conditions'].append('hyperhydrosis')
```

**Question:** what if we modify one of the variables we created above to simplify handling information about patient 2?

Will the following modify our original dict, *pat1*, or not?


```python
p2_age = p2_age + 1     # Happy birthday Egdar!
```


```python
p2_conds.append('fever')
```

Remember: dictionary *keys* can't be mutable!


---
# <ins>Keys must be unique within a dictionary</ins>
Reusing a key will overwrite the old value with a new value

```python
pat1['age'] = pat1['age'] + 1     # Happy birthday Dionna!
```

Obviously, this means you can't have two identical keys in the same dictionary.


---
# <ins>Key Types</ins>
Keys can be of any immutable type (e.g., number, strings, tuples).
*Usually* strings make the most sense to use as dict keys.
Note that you cannot use a list as a key because it is mutable. You could use a tuple though, if you really wanted to.


---
# <ins>Methods for working with dicts</ins>
Python dictionaries have a variety of built-in methods for manipulating them

e.g., .keys(), .values(), .items(), .get(), .pop(), .update(), etc.


### Getting length
>len(dict) | *len* gets the length of a dictionary.

```python
len(pat1)
```

The length of a dictionary is the number of key/value pairs it contains.


### Get all items [tuple(key,value)]
>dict.items() | Returns a new object of the dictionary's items in (key, value) format

```python
p1items = pat1.items()
```

What kind of object is this? We might want to make it into a list:

```python
p1items_list = list(pat1.items())
```


### Get all keys [keys]
>dict.keys() | Returns a new object containing just the dictionary's keys

```python
pat1.keys()
```

### Get all values [values]
>dict.values() | Returns a new object containing just the dictionary's values

```python
pat1.values()
```

### Check if key is in dictionary
>k in dict | Returns True or False if dict has a key k

```python
'name' in pat2
'fname' in pat2
```

### Attempt to retrive using non-existent key
>Returns the value with key k - KeyError

```python
pat2['gender']
```

### Retrieve using get()
>dict.get(key[, default]) | Returns the value for a key if it exists in the dictionary, else it returns a default value

```python
print(pat2.get('gender'))
print(pat2.get('gender', 'We don't have information about this patient's gender'))
```

### Create copy
>dict.copy() | Returns a shallow copy of the dictionary
```python
copy_of_pat1 = pat1.copy()
copy_of_pat1["fname"] = "dionna"
print(pat1)
print(copy_of_pat1)
```



### Pop key
>dict.pop(key[, default]) 

>Removes and returns an element from a dictionary 
having the given key. Returns default if the key is missing and default value is specified

```python
copy_of_pat1 = pat1.copy()
copy_of_pat1.pop('fname')
```

Note that this is a good way to lose information!

### Update key
>dict.update([other]) | Updates one dictionary with key/value pairs from another, overwriting existing keys.

```python
pat2.update({'fname' : 'Elgin', 'age' : 36}) # Happy birthday, Elgin!
```


### Delete key
>del dict[k] | Removes the key:value for key k

```python
del pat2['zip']
```

### Clear the dictionary
>dict.clear() | Removes all elements from the dictionary

```python
pat2.clear()
print(pat2)
```

This is a *really* good way to lose information!



---
# <ins>Nested Dictionaries</ins>
As we have seen, dictionaries can contain complicated structures as their values, including lists. Dictionaries can also contain other dictionaries

This makes them ideal for data science and other fields that involve complex data structures. At this point in your Python journey, we don't necessarily recommend trying this until you have more experience manipulated complicated structures. It can be confusing. See? 



```python
patients_d = {  7491 : {'birthdate': 2018,
                        'ssn': '999-92-3312',
                        'fname': 'Dionna',
                        'lname': 'Heathcote',
                        'zip': 72411,
                        'sex': 'Female',
                        'age': 7,
                        'conditions': ['measles', 'fever']},
                7182 : {'birthyear': 1989,
                        'fname': 'Edgar',
                        'lname': 'Hermann',
                        'age' : 35,
                        'sex' : 'Male',
                        'conditions' : ['type ii diabetes', 'eczema'],
                        'zip': 72034}}
```

Note that this would be another way to create the same kind of structure from already-existing dicts *pat1* and *pat2*:


```python
patients_d2 = {7491 : pat1, 7182 : pat2}
```

What would be a small difference between these two?



# Dictionaries inside lists
Lists can also contain dictionaries:

```python
patlist = [{'mrn': 7052, 'birthyear': 2013, 'ssn': '999-80-4418', 
            'fname': 'Eleni', 'lname': 'Gusikowski', 'zip': 72736},
           {'mrn': 1744, 'birthyear': 1969, 'ssn': '999-72-5953', 
            'fname': 'Michelle', 'lname': 'Breitenberg', 'zip': 72472}]
```




# ------------------------------------------------------
# Class Exercise


Let's add another person to the patient list above, making sure we use the same keys


* MRN : 4851
* Birth Year : 2011
* Social Security Number :  999-51-6410
* First Name : Ricardo
* Last Name : Mills
* Zip Code : 72046


---
# <ins>Using multiple loop variables</ins>

Recall that the *items* method returns something that looks like a sequence of tuples:

```python
print(another_element.items())
```
In a moment we'll look at how to use a list to access these tuples one by one. 
First, a brief diversion into the topic of using multiple loop variables.

Consider the following list of tuples. Each tuple consists of first a number and then its square:

```python
squares = [(1,1), (2,4), (3,9), (4,16), (5,25)]
```

If we wanted to print these out, we could do something like the following:
```python
for s in squares:
    print(f"The square of {s[0]} is {s[1]}")
```

One limitation of this approach is that if we are working with a very complicated loop, 
with many lines of code inside the loop, we might find ourselves typing *s[0]* and *s[1]* repeatedly, and we might even lose track of what they mean.

Python loops can help with this, by allowing the use of multiple loop variables:


```python
squares = [(1,1), (2,4), (3,9), (4,16), (5,25)]
for num, square in squares:
    print(f"The square of {num} is {square}")
```


```python
squares3 = [(1,1,1), (2,4,16), (3,9,81), (4,16,256), (5,25,625)]
for n1, n2, n3 in squares3:
    print(f"The square of {n1} is {n2}, and the square of that is {n3}")
```



---
# <ins>Exercise: Combining Elements: Dicts, Lists, Loops, and Ifs</ins>

**Let's build a list of patient dicts** that contains at least three patients, and includes both *conditions* and *sex* for all patients. We can start with Dionna and Edgar.

```python
patlist = [{'mrn': 7491,
            'birthdate': 2018,
            'ssn': '999-92-3312',
            'fname': 'Dionna',
            'lname': 'Heathcote',
            'zip': 72411,
            'sex': 'Female',
            'age': 7,
            'conditions': ['measles', 'fever']},
            {'mrn': 7182,
            'birthyear': 1989,
            'fname': 'Edgar',
            'lname': 'Hermann',
            'age' : 35,
            'sex' : 'Male',
            'conditions' : ['type ii diabetes', 'eczema'],
            'zip': 72034}]
```
        
We'll start by adding one patient.

Next, let's try **looping over this list and displaying each patient's full name, age, and sex**.

Next, let's modify the loop to also print out how many conditions each patient has.

Finally, let's change this code further to **only output that information for patients with male sex who are above the age of 18**.




