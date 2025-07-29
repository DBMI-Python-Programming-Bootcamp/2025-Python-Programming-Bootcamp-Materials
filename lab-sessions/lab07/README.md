# Installing Libraries
Walk though in-class.
# Variables

We've discussed variables in the past, such as:

```python
student_name = "William"
student_age = 12
print(f"{student_name} is {student_age} years old.")
```

However, variables are much more versatile than that, as we've eluded to in the past lectures.

## Counting Loop Iterations
For example, in my lecture on `for` loops we looked at this bit of code that outputs the number of times a loop runs:

```python
loop_count = 0
for i in range(1,10): # this loop has i go from 1-9
    loop_count = loop_count + 1
print(loop_count)
```

This example is trivial, as we can tell the loop goes 9 times just through logic.

However, something like this is less trivial for us, though still simple for the computer to calculate:

```python
x = 39
y = 42

loop_count = 0
for outer_loop in range(1,x): # this loop has i go from 1 to x
    for inner_loop in range(1,y): # this loop has j go from 1 to y
        loop_count = loop_count + 1
print(loop_count)
```

This tells us how many times this loops overall. 

## Going Further

As an example, let's take the code from above and modify it. 

How would we see the number of times the *outer_loop* and *inner_loop* run?

```python
x = 39
y = 42

inner_loop_count = 0
for outer_loop in range(1,x): # this loop has i go from 1 to x
	for inner_loop in range(1,y): # this loop has j go from 1 to y
		inner_loop_count = inner_loop_count + 1
print(inner_loop_count)
```

For the inner loop, notice that the number of loops is already counted in our **loop_count** variable, so we have renamed it to **inner_loop_count**.

What ways do we have to see the number of times the *outer loop* runs?

## Simulating Randomness
Even in the example above we could use simple math to see how many times the code loops. But what if we didn't know the values of the **x** and **y** variables? We can simulate this using the *randint* function. For this we're going to import a library.

```python
import random #import the random library
x = random.randint(1,100) #assigns x a random integer between 1 and 100
print(x)
```

> *randint* takes two integer values, the first is the lower bound, the second is the upper bound. For example randint(1,10) gives you an integer value between 1 and 10.

Not that once assigned this value is set, it's not random every time you use *x*.

You can check this like so: 
```python
print(x)
print(x)
print(x)
print(x)
print(x)
```

Now adding this to our previous example:

```python
x = random.randint(1,100)
y = random.randint(1,100)

inner_loop_count = 0
for outer_loop in range(1,x): # this loop has i go from 1 to x
	for inner_loop in range(1,y): # this loop has j go from 1 to y
		inner_loop_count = inner_loop_count + 1
print(inner_loop_count)
```

It's no longer trivial for us to calculate the number of times looped as we don't know the value of *x* and *y* until program execution, but we can still calculate it with the *inner_loop_count* variable.

### Roll the Dice
Let's use some other examples, this time using standard six-sided dice.

> Rolling a six-sided dice gives you an equal chance of getting a value of 1,2,3,4,5, or 6.

We might simulate rolling a die in python as follows:
```python
die_value = random.randint(1,6) #gives a random value between 1 and 6
print(f"You rolled a {die_roll}.")
```

#### Monte Carlo Simulation
An easy model to simulate statistics for things such as dice rolls, is a Monte Carlo strategy. In this approach we make a large number of "rolls" and then store them in a way that we can deduce statistics from them.

First, we need a way to generate a large number of "rolls." The obvious tool we have at our disposal is the for loop. Lets start small:

```python
for roll_num in range(0,10): #loop ten times  
   die_value = random.randint(1,6)  
   print(die_value)
```

This "rolls" the die and prints out the value, but we need a way to store it.

For now, we're going to use a list, called *die_value_list*.

```python
die_value_list = []
for roll_num in range(0,10): #loop ten times  
   die_value = random.randint(1,6)  
   die_value_list.append(die_value)
print(die_value_list)
```

Now, we have a random list containing the multiple values of dice rolls. 

We can make this even more powerful, using a `function` as we discussed in the last lecture:
```python
def roll_dice(num_dice):  
    dice_list = []  
    for roll_num in range(0, num_dice):
	    dice_list.append(random.randint(1,6))
	return dice_list

print(roll_dice(5)) # roll five dice
print(roll_dice(10)) # roll ten dice
print(roll_dice(12)) # roll twelve dice
```

### In-class Exercise

Use our `roll_dice` code above as a template.
#### Task 1
Calculate and print the average roll using die_value_list. 

> **Note:** We know the average roll should be (1+2+3+4+5+6) / 6 = 3.5
#### Task 2
Calculate and print the number of times we rolled a 6.

> **Note:** We know the chance of rolling a 6 is 1/6 or 16.7%. In 1,000 rolls we should expect to see about 167 6s rolled.

### Non-trivial examples
Ok, so we see that Monte Carlo works for a simple case, but we could easily calculate these values manually. 
> Chance of rolling a 6 = 1/6 = 16.7%
> Average roll is (1+2+3+4+5+6) / 6 = 3.5

What if we want to do something like, if we roll 2 dice, what is the chance their sum is equal to 7?
```python
number_of_rolls = 100000 # how many times to roll the two dice
die_value_list = []
for roll_num in range(0,number_of_rolls): #loop number_of_rolls times  
   first_die_value = random.randint(1, 6)
   second_die_value = random.randint(1, 6)
   total_value = first_die_value + second_die_value
   die_value_list.append(total_value)
print(f'The chance of rolling a seven with two dice is approximately {die_value_list.count(7) / number_of_rolls}')
```

Alternatively if we want to use our function, we could do:
```python
# previous function to roll dice
def roll_dice(num_dice):  
    dice_list = []  
    for roll_num in range(0, num_dice):
	    dice_list.append(random.randint(1,6))
	return dice_list

# this function rolls n dice and sums the result
def roll_dice_and_sum(num_dice, num_times):
	die_sum_list = []
	for i in range(0, num_times):
		die_sum_list.append(sum(roll_dice(num_dice)))
	return die_sum_list

num_dice = 2
num_times = 100
target_roll = 7
print(f'The chance of rolling a {target_roll} with ten dice is approximately {roll_dice_and_sum(num_dice, num_times).count(target_roll) / num_times}')
```

> We can still calculate this, the valid combinations that make a 7 are:
> (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 combinations
> 6 * 6 = 36 total combinations
> So the answer is 6/36 = 1/6 ~= 16.7%

What's the chance of rolling a 3?

> (1,2), (2, 1) = 2 combinations
> 2 / 36 = 5.6%

Now that we trust and understand the method, you can hopefully see how powerful it can be. For example, what if we want to do something *more* complicated? If we roll 10 dice, what is the chance that their sum is equal to 36?

Here's the old way:
```python
number_of_rolls = 100000 # how many times to roll the two dice  
die_value_list = []  
#loop number_of_rolls times  
for roll_num in range(0,number_of_rolls):  
    sub_list = []  
    for j in range(10):  
        sub_list.append(random.randint(1,6))  
    die_value_list.append(sum(sub_list))  
print(f'The chance of rolling a 36 with ten dice is approximately {die_value_list.count(36) / number_of_rolls}')
```

With the function approach it's simply:
```python
num_dice = 10 # change from 2 to 10 dice  
target_roll = 36 # change our target number from 7 to 36
print(f'The chance of rolling a {target_roll} with ten dice is approximately {roll_dice_and_sum(num_dice, num_times).count(target_roll) / num_times}')
```

## Something Graphic
Thus far we've only looked at output from the console, but it's *frequently* useful to visualize the data as a figure. To do so, we'll be using the `matplotlib` library.
```python
import matplotlib.pyplot as plt  
```

> Unlike the `random` library, you will probably need to install `matplotlib` in Pycharm before you can use this library. To do so you can click "Install package matplotlib" when you mouseover the name in Pycharm. **Note:** this may take a few moments to install.

#### Line Plots

```python
import matplotlib.pyplot as plt  
  
# Sample data  
x = [1, 2, 3, 4]  
y = [10, 20, 25, 30]  
  
# Create plot  
plt.plot(x, y)  
  
# Add labels  
plt.xlabel('X axis')  
plt.ylabel('Y axis')  
plt.title('Simple Line Plot')  
  
# Show the plot  
plt.show()
```

We can change the color like so:
```python
plt.plot(x, y, color="red") # change the color to red
plt.plot(x, y, color="#00FF00") #change the color to green 
```

### Dice Visualization
Let's use this to plot our dice rolls from earlier.

```python
die_value_list = []
for roll_num in range(0,10): #loop ten times  
   die_value = random.randint(1,6)  
   die_value_list.append(die_value)
```

```python
# potential die rolls are 1,2,3,4,5,6
x = [1, 2, 3, 4, 5, 6]
y = [die_value_list.count(1), 
	 die_value_list.count(2),
	 die_value_list.count(3),
	 die_value_list.count(4),
	 die_value_list.count(5),
	 die_value_list.count(6)]

plt.plot(x, y)

# Add labels  
plt.xlabel('Die value')  
plt.ylabel('# of times rolled')  
plt.title('Plot of die values rolled')  
  
# Show the plot  
plt.show()
```
### Bar Plots

Hmm, this isn't very intuitive and doesn't make sense as a line plot, instead maybe a bar plot would be better for this visualization. This is easy in `matplotlib`, you simply change:

```python
plt.plot(x, y) # line plot
```

To:

```python
plt.bar(x, y) # bar plot
```

Keep in mind that `matplotlib` can do both at the same time for example:

```python
plt.plot(x, y) # draw this first
plt.bar(x, y, color="red", alpha=0.5) # draw this second (on top of)
```

### Histograms

```python
plt.hist(roll_dice(1000), bins=6, color='orange', edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
```
