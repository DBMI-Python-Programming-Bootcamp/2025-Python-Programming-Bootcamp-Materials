

# Files & Pandas

## File Handling

Python uses files to quickly analyse lots of data. There are several functions for file handling that allow users to read from, write into, update and delete files.

## Reading from a file
### Reading an entire file
Reading from a file is particularly useful in data analysis applications and data modification. For example, you can read the content of a text file and rewrite the file with formating that allows a browser to display it. To begin, you need a text file to open and then use the built-in function open() to access that file. The text file should be in the same place as your code. The syntax for the function is:

```python
f = open("pats.txt")
print(f.read())
``` 
The open() function returns a file object, which has a read() method for reading the content of the file that is stored where the program that is being executed is stored:

```python
with open("pats.txt") as file_object:
  contents = file_object.read()
print(contents)
```

Or you may tell Python exactly where the file is on your computer, regardless of where your Python code is store:

```python
with open("C:\\Users\\alshukrishaymaa\\PycharmProjects\\pythonProject\\pats.txt") as file_object:
print(file_object.read())
```
By default the read() method returns the whole text, but you can also specify how many characters you want to return

### Reading line by line

You can return one line by using the readline() method:
```python
with open("pats.txt") as file_object:
    print(file_object.readline())
```

Or you may use a for loop on the file object to examine each line from a file, one at a time:

```python
file_object = open("pats.txt")
for line in file_object:
   print(line)
```

Multiple lines can be accessed using readlines() method:
```python
with open('pats.txt', 'r') as file_object:
    lines = file_object.readlines()
print(f"The first line is: {lines[0]}")
print(f"The second line is: {lines[1]}")
```

It is a good practice to always close the file when you are done with it using close()


When you print each line, you will find blank lines between the lines you have in your file. These lines appear becuase an invisible newline character is at the end of each line in the text file and the print function adds its own new line each time you call it. You may use strip() each time the print function is called to eliminate the extra lines
```python
filename = 'pats.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())#rstip()

pat1 = lines[1].strip().split('|')
pat2 = lines[2].split('|')
```

We can lable the data for each line:
```python
at1d = {'mrn' : int(pat1[0]),
         'birthyear' : int(pat1[1]),
         'ssn' : pat1[2],
         'fname' : pat1[3],
         'lname' : pat1[4],
         'zip' : pat1[7]}
```

A function can be used to do that for every patient in the data

```python
def patlist_to_patdict(patlist):
    return {'mrn' : int(patlist[0]),
            'birthyear' : int(patlist[1]),
            'ssn' : patlist[2],
            'fname' : patlist[3],
            'lname' : patlist[4],
            'zip' : patlist[7]}
print(patlist_to_patdict(pat1))
print(patlist_to_patdict(lines[-1].strip().split('|')))
```

What if we wanted to build in the functionality to strip and split the line?

```python
def patline_to_patdict(patline):
    plist = patline.strip().split('|')
    return  plist 
```

It is also possible to read each line and append that line to a list
```python
patd_list = []
for line in lines:
    patd_list.append(patline_to_patdict(line))
print(patd_list)
```





## Writing to a file

One of the simplest ways to save data is to write it to a file, this way you can always examine the output after a program finish running and you can share the data with others

### Writing to an empty file

To write text to a file, you need to call open() with a second argument telling Python that you want to write to the file. You can open the file in write mode 'w', read mode 'r', append mode 'a', or a mode that allows you to read and write to the file 'r+'. If you omit the mode argument, Python opens the file in read-only mode by default. The open() function automatically creates the file to write to, if you do the write mode 'w' and the file exists, Python will erase the contents of that file before running the file object

```python
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write('I love Python')
```
### Writing multiple lines

```python
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write('I love Python\n')
    file_object.write('I love programming\n')
```

## Appending to a file

Append mode can be used to add content to a file instead of writing over existing content. Any lines you write to the file will be added at the end of the file. If the file does nto exists, Python will create an empty file 


```python
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write('I love Python\n')
    file_object.write('I love programming\n')
```

## Pandas

Python library that is used to analyze, clean, and process data in large data sets. It can clean messy data sets and make them readable and useful 


### Pandas DataFrame

DataFrames are 2D structures with corresponding labels and are similar to SQL tables or excel spreadsheets. They are widely used in data science, machine learning, scientific computing, and many other data-intensive fields.

```python
import pandas
mydataset = {
  'name': ["TP53", "TNF", "EGFR","VEGFA"],
  'description': ["tumour-suppressor protein p53","tumour necrosis factor","epidermal growth factor","vascular endothelial growth factor A"]
}
myvar = pandas.DataFrame(mydataset)
print(myvar)
print(myvar.loc[1])
print(myvar.loc[[1, 2]])
```

You can rename the lables of a DataFrame, and call the value of a specific label

```python
df = pandas.DataFrame(mydataset, index = ["g1", "g2", "g3", "g4"])
print(df)
print(df.loc["g2"])
```

### Reading from external file

You can read data sets that are stored in a csv or text file and load them into a DataFrame
```python
import pandas as pd
df = pd.read_csv('pats.txt')
print(df.to_string()) #to print the entire DataFrame
print(df.columns)
print(df) #Pandas will return the first 5 rows, and the last 5 rows for a DataFrame with many rows
print(df.tail(10)) #to print the last 10 rows only
print(df.info())
```

Let's read data from two different files
```python
pats = pd.read_csv('patients.csv')
conds = pd.read_csv('conditions.csv')
print(pats)
print(conds)
print(pats.columns)
print(conds.columns)
```

We can rewrite them to have just a few columns

```python
pats = pats[['Id', 'BIRTHDATE', 'SSN', 'FIRST', 'LAST', 'GENDER', 'ZIP']]
conds = conds[['PATIENT', 'CODE', 'DESCRIPTION']]
```

Let's take a look at just one patient
```python
pat1 = pats.iloc[0]
print(pat1)
print(pat1['BIRTHDATE'])
p1bd = pat1['BIRTHDATE']
print(type(p1bd))
print(len(p1bd))
print(p1bd.split('-'))
```
It is also possible to extract a number from a string
```python
p1by = int(p1bd.split('-')[0])
print(p1by)
```

Below is a function that accepts a string, extract a number from it and return the age
```python
def birthdate_string_to_age(bdstr, year = 2025):
    birthyear = int(bdstr.split('-')[0])
    return year - birthyear

# examples
birthdate_string_to_age('2001-01-01')
birthdate_string_to_age('1970-12-12')
```

We can use that function to find the age and add it to the DataFrame
```python
pats['AGE'] = pats['BIRTHDATE'].apply(birthdate_string_to_age)
print(pats)
```
We can use some statistical functions to analyse the data, or apply some filters to show specific group of data
```python
print(pats['AGE'].mean())
print(pats['AGE'].median())
print(pats['AGE'].min())
print(pats['AGE'].max())
print(pats[pats['AGE'] > 50])
print(pats[pats['GENDER'] == 'F'])
print(pats[(pats['GENDER'] == 'F') & (pats['AGE'] > 20)])
```


Using matplotlib to virtualize the new added column
```python
import matplotlib.pyplot as plt
print(pats['AGE'])
pats['AGE'].plot()
plt.show()
```

Looking at the conditions file

```python
print(conds.to_string())
print(conds['DESCRIPTION'])
print(conds[conds['DESCRIPTION'] == 'Essential hypertension (disorder)'])
```

We can match data from the two files, patients and conditions
```python
hypertensions = conds[conds['DESCRIPTION'] == 'Essential hypertension (disorder)']
print(hypertensions['PATIENT'])
print(pats['Id'].isin(conds['PATIENT']))
print(pats[pats['Id'].isin(hypertensions['PATIENT'])])
hypertension_pats = pats[pats['Id'].isin(hypertensions['PATIENT'])]
```

isin() function can be used to look for specific values in a list, dictionary, or dataframe
 

```python
pat_age = pats[['Id', 'BIRTHDATE', 'AGE']]
print(new_dataframe)
new_dataframe = pd.DataFrame(pat_age)
print(new_dataframe.isin([22, 49,103,'1976-02-11']))
print(new_dataframe.isin({'AGE': [22, 49]}))

```
Can you find the mean age of patients with hypertension?



 

