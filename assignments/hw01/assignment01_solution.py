
# PART 1
# Create variables named givenName and familyName and assign them values so that they store your given name and # family name respectively
givenName = "Jonathan"
familyName = "Bona"

# Create a variable named startYear and assign it a value so that it stores the year you first became affiliated with UAMS
startYear = 2016
currentYear = 2025
# Add a print statement that prints out a message reporting your full name, the year you started at UAMS, and how many years ago that was.
print(f"{givenName} {familyName} started at UAMS in {startYear}, which was {currentYear - startYear} years ago")

# Add a print statement that prints out the total length of your name.
namelen = len(givenName) + len(familyName)
print(f"The total length of 'Jonathan Bona' is {namelen}, {namelen + 1} if you count the space.")

# PART 2
# Create a variable named courses and assign it a list of strings that represent the names of the courses you are taking this fall.
courses = ['Underwater Basketweaving',
           'Informatics Approaches to TV Sitcom Analysis',
           'Computational Methods']


# Add a print statement that outputs a message with this full list of courses.
print(f"My list of courses is: {courses}")

# Add a print statement that outputs a message with the name of just the first course in the list.
print(f"The first course is: {courses[0]}")

# Add a print statement that outputs a message with the name just the last course in the list.
print(f"The last course is: {courses[-1]}")

# Add a print statement that outputs a message saying how many courses are in the list.
print(f"There are {len(courses)} courses in the list")

# Add a print statement that uses the Python function sorted on your list and outputs the result.
print(f"Here's what happens when I used the sorted function: {sorted(courses)}")

print(f"Here's what is in the variable after I've used the sorted function: {courses}")
# Add a comment that explains what you think the sorted function is doing to your list (hint: try running the above line before reporting what it does)

# I think this function is producing a sorted version of the list, but it is not changing what's stored in the variable.