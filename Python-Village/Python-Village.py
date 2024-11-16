##############################################################################################################

## ID: INI1 (Installing Python)


print ("Hello, World!")

import this

#############################################################################################################

## ID: INI2 (Variables and Some Arithmetic)

a = 324
b = 24
c = a - b
print(c)

print ("a - b is", c)

addition = 2 + 3 == 5
print('addition is', addition)

subtraction = 5 - 2 == 3
print('subtraction is', subtraction)
 

multiplication = 3 * 4 == 12
print('multiplication is', multiplication)


divison = 15 / 3 == 5
print('divison is', divison)

divison1 = 18 / 5 == 3
print('divison1 is', divison1)

#or
# use 18.0/5 or float(18)/5 for precise results

division_remainder = 18 % 5 == 3
print('divison_remainder is', division_remainder)


exponentiation = 2 ** 3 == 8
print('exponentiation is', exponentiation)

a = "Hello"
b ="World"

print (a, b)

a = 'Rosalind'
b = 'Franklin'

c = '!'

print (a, b, c*3)
print (a + ' ' + b + c*3) 

## Problem

a = 3
b = 5
c = (a**2) + (b**2)

print (c)

a = 924
b =  877

c = (a**2) + (b**2)

print (c)


############################################################################################################


## ID: INI3 (String and Lists)

cricket_party = ['March Hare', 'Hatter', 'Darmouse', 'Alice']
print (cricket_party[2])

cricket_party[1] = 'Kohli'

print (cricket_party)

cricket_party.append('Rohit')

print (cricket_party)

## to obtain only some from the list

cricket_party[0:2]  ## it will only show entries from 0 up to but not including 2.
## this process is called 'list slicing'


## if first index of the slice is unspecified, then Python assumes that the slice begins with the beginning of the list (i.e., index 0)
## but still it will give up to but not including that number ( in this case index 2)
cricket_party[:2]

## if second index of the slice is unspeciifed, then we will obtain items till the end of the list.
## it will give items with that index (in this case index 2) up untill the last index.
cricket_party[2:]

## we can also use negative indices to count items backtracking from the end of the list.

cricket_party[-2:] # will give same output as cricket_party[3:]

## python also give us the ability to slice the strings the same way we slice our lists.
## a string can be considered as a list of characters, each of which having its own index starting from 0.

a = 'flimsy'
b = 'miserable'

c = b[0:2] + a[3:]
d = b[0:1] + a[2:]

print (c)
print (d)

s = 'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.'
a = 22
b = 27
c = 97
d = 102

print (s[a:(b+1)] + ' ' + s[c:(d+1)])

## Problem

s = 'uDXNNKvzzIwfVT9zyx66BEChenOClYHB7jsunSC1FJPugSC0k5ewVX6bLSeyGwIFn9JiURT6pHjCMpKfAIliI4gultturturmK94SpIP3c1kmPgEv71kNndH6sDgg6Ttw45rEQw6debUwXqnhfgBSuIWXAIbcm3mZq.'
a = 22
b = 25
c = 90
d = 95

print (s[a:(b+1)] + ' ' + s[c:(d+1)])


#################################################################################################################


## ID: INI4 (Conditions and Loops)

# if we need to choose between two actions, then we can use an 'if' or 'else' statements.

a = 42
if a<10:
    print ('the number is than 10')
else:
    print ('the number is greater or equal to 10')


a = 5
b = -1
if a + b == 4:
    print ('printed when a + b equals four')
print ('always printed')

## if we want to repeat an action several times, we can use while loop.

g = 1
while g <=3:
    print ('Hello! ' *g) # multiply the string 'Hello! ' with g.
    g =  g + 1 #this line will increment the value of g by 1 in each line untill 3.

    ## dont type g = g + 0; beacsue it will create infinite loop.


## if we want to carry out some actions on every element of a list, the 'for' loop will be handy.

names = ['Alice', 'Bob', 'Charley']
for name in names:
    print ('Hello, ' + name)

## and if we want to repeat an action exactly n times, we can use the following template;

n = 10
for i in range(n):
    print (i)

## in the above code, 'range' is a function that creates a list of integers betweeen 0 and n, where n is not included.

print (range(5, 12))
## in Python2, above code will print [5, 6, 7, 8, 9, 10, 11]

## for Python 3

print (list(range(5,12)))

## print numbers from 5 to 11, not including the 12.

## Problem

a = 100
b = 200

# Initialize the sum
total = 0

# Iterate through the range from a to b (inclusive)
for num in range(a, b + 1):
    if num % 2 == 1:  # Check if the number is odd
        total += num

print(total)


## dataset

a = 4323 
b = 8718

# Initialize the sum
total = 0
## this code will initaite a variable 'total' to zero.
## 'total' will be used to accumulate the sum of all odd numbers within the range.
## at the start, we set it to zero because no numbers have been added yet.

# Iterate through the range from a to b (inclusive)
for num in range(a, b + 1): ## this is a for loop that will iterates over all integers from "a" to "b"
                            ## "range(a, b+1)" will generate a sequence of number starting at "a" and end at "b" (since b+1 is excluded)
                            ## the variable "num" takes on each value in this sequence at a time.
    if num % 2 == 1:    ## this conditional statement Check if the number is odd
                        ## if the remainder is 1, that menas it is a odd number
        total += num    ## "total += num" is a shorthand for total = total + num
                        ## if the condition "num % 2 == 1" is true (i.e., number is odd), this line adds the current value to "num" to "total"
                        ## over the course of the loop, this accumulates the sum of all odd numbers in the range.

print(total)

#################################################################################################################################

## ID: INI5 (Working with files)

## Reading and Writing

## we will work with lot of files from rosalind.info, to analyze our datasets

## usually we need to open the file first. to do that we canuse open() function
## open() function usually takes two parameters: the name of the target file and the mode.
## three modes are available:

# r = read mode (file is opened for reading)
# w = write mode (the file is opened for writing, and if the file having the same name exits, it will be erased)
# a = append mode (the file is opened for appending, which means that data is only to be added to the existing data in the file)

f = open("input.txt", 'r')
## the above code line told python to open the file 'input.txt' in 'r' mode and store the result of this operation in a file object called 'f'

## to obtain data from the file object we created, we can apply following methods:

## the command f.read(n) return n bytes of the data from the file as a string. when the size parameter is omitted, the entire contents of the file will be read and returned.

## the command f.readline() takes a single line from the file. Every line (except the last line of the file) terminates in a 
## newline character (\n). To remove this character fromt he end of a line you have read, use the .strip()  method.
## Note that every time you call .readline() it takes the next line in the file.


## the command f.readlines() returns a list containing every line in the file. If we need to obtain a particular line, we can use a 
## list item index, e.g., f.readlines()[2] returns the third line of the file object f.

## an alternative way to read lines is to loop over the file object.

for line in f:
    print (line)

## using this above loop, we can do anything we need with every line in the file.

## if the data in the file is not separated by new lines but rathe rby whitespace, commas, or any other delimeter, 
## then all three commands above will return the data only in the form of lines. As a workaround, we can use the command line.split().
## it uses whitespace in addition \n as delimeters by default, and runs of the same delimeter are regarded as a single
## separting space.

## For example,

'Beautiful is better than ugly.\n'.split()

'Beautiful is better than ugly.'.split()

## we can also specify the delimeter as a parameter of line.split():

'Explicit, is better, than implicit.'.split(",")

'Explicit, is better, than implicit.'.split() ## this uses whitespace to split

## another convenient command for file parsing is .splitlines(). it returns a list of the lines in the 
## string, breaking at the line boundaries. Line breaks are not included.

'Simple is\nbetter than\ncomplex.\n'.splitlines()

## after finishing all the calculation we need to save it.
## to save a file, output the desired file in write mode (if there is no such file, it will be created automatically)

f = open('output.txt', 'w')

## we can also write the data using .write() method

f.write('Any data that we want to write into the file')
f.close()
## when we are finished writing file, we must close it using command f.close()

## the command f.write(string) write the contents of string to file f.
## if we want to write something other than a string (an integer say), we must first
## convert it to string by using the function str().


f = open('output.txt', 'w')

f.write('Any data that we want to write into the file')

inscription = ['Rosalind Elsie Franklin', 1920, 1958]
s = str(inscription)
f.write(s)
f.close()

f = open('output.txt', 'w')

f.write('Any data that we want to write into the file\n')

inscription = ['Rosalind Elsie Franklin', 1920, 1958]
s = str(inscription)

## we can write items into the file one at a time by using a "for" loop

for i in inscription:
    f.write(str(i) + '\n')

## adding '\n'to str(i) means that every item will start with a new line.
f.close()


## Problem

f = open("input.txt", 'w')

f.write('Bravely bold Sir Robin rode forth from Camelot\nYes, brave Sir Robin turned about\nHe was not afraid to die, O brave Sir Robin\nAnd gallantly he chickened out\nHe was not at all afraid to be killed in nasty ways\nBravely talking to his feet\nBrave, brave, brave, brave Sir Robin\nHe beat a very brave retreat\n')

f.close()

f = open("input.txt", 'r')


with open("input.txt", 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if (i + 1) % 2 == 0:
            print(lines[i])


f.close()

### dataset problem

f = open('input1.txt', 'w')
f.close()

with open("input.txt", 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if (i + 1) % 2 == 0:
            print(lines[i])


###########################################
####### Explanation of above code #########
###########################################

## The 'with' statement ensures that the file is automatically closed when the block is exited, 
## even if an error occurs. You don’t need to call 'f.close()' manually. 

## Opens the file named 'input.txt' in read mode ('r').
## The file object is stored in the variable 'f'.

## 'lines = f.readlines()' Reads all the lines from the file and stores them as a list of strings in the variable lines.
## Each element in the list represents one line from the file, including the newline character \n at the end of each line.
## for example, If input.txt contains:
# Line1
# Line2
# Line3
# Line4
### then 'lines' will be:
# ['Line1\n', 'Line2\n', 'Line3\n', 'Line4\n']


## 'for i in range(len(lines)):' The range(len(lines)) generates a sequence of numbers from 0 to len(lines) - 1 (the indices of the list lines).
## i is the index of the current line in the lines list during each iteration.
## Example: For the above 'lines' (Line 1 to Line 4), 'range(len(lines))' will give:
# [0, 1, 2, 3]


## if (i + 1) % 2 == 0: (i + 1) adjusts the index i (0-based) to 1-based numbering because line numbers typically start at 1.
## % 2 == 0 checks if the 1-based line number is even.

## Example: When i = 0, i + 1 = 1 (odd, skipped). And When i = 1, i + 1 = 2 (even, included).

## print(lines[i]): Prints the content of the line at index i from the lines list if its line number is even.





############################################################################################################################
############################################################################################################################



### ID: INI6 (Dictionaries)

##### Intro to Python Dictionary

## We have already discussed and used lists and strings to store and process data.
## Python also has a variable type called a "dictionary" that is similar to a list, but instead
## of having integer indices, we provide our own index, which we called a "key".
## we can assign data to dictionary as follows:
## phones = {'Zoe':'232-43-58', 'Alice':'165-88-56'}
## we can therefore think of a dictionary as a "function" that maps a collection of keys to the values. As with lists, the values of the 
## list can of any type: strings, integers, floating point numbers, even lists or dictionaries themselves.
## for keys we can use only strings, numbers, floats, and other immutable types (an immutable data type is a type whose value cannot be 
## changed after it's created. If you try to modify an immutable object, a new object is created with the modified value).
## Accessing values of a dictionary is also similar to accessing values of a list:

phones = {'Zoe':'232-43-58', 'Alice':'165-88-56'}
print(phones['Zoe'])

## the output after above code was 232-43-58


## we can also add new values to a dictionary or assign a new value to an existing key can also be done as follows:

phones['Zoe'] = '655-99-55'

phones['Bill'] = '342-18-25'

print(phones)

phones['myself'] = '123-45-67'

print(phones)

### Dictionaries are usually case-sensitive if we are using strings as keys. For example, 'key' and 'Key' are viewed as different keys:

d = {}
d['KeY'] = 0
d['key'] = 1
d['Key'] = 2
d['KEY'] = 3
print(d)


### Note how we created an empty dictionary with 'd = {}'.
## this could be useful in case we need to add values to dictionary dynamically (for example, when reading a file).
## if we nned to check whether there a key in dictionary, we can use 'key in d' syntax:

print('key' in d)

## output is True becoz key is present in d.

if 'Peter' in phones:
    print ("We know Peter's phone")
else:
    print ("We don't know Peter's phone")

## output is : "We don't know Peter's phone"


if 'Zoe' in phones:
    print ("We know Zoe's phone")
else:
    print ("We don't know Zoe's phone")

## in case we need to delete a value from a dictionary, use the 'del' command:

print (phones)

## output is: {'Zoe': '655-99-55', 'Alice': '165-88-56', 'Bill': '342-18-25', 'myself': '123-45-67'}

del (phones['Zoe'])

print (phones)

## output is: {'Alice': '165-88-56', 'Bill': '342-18-25', 'myself': '123-45-67'}


# input string
s = 'We tried list and we tried dicts also we tried Zen'

## create an empty dictionary to store word counts

word_count = {}

## split the string into words

words = s.split()

## The 'split()' method splits the string s into a list of words.
## By default, 'split()' separates the string at spaces.

print (words)


## count occurences of each word

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


## output the word counts

for key, value in word_count.items():
    print (key, value)

## word_count.items() gives each key-value pair (word and its count) in the dictionary.
## The for loop iterates through these pairs.
## The print(key, value) statement displays each word and its count.



s = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'

## create an empty dictionary to store word counts

word_count = {}

## split the string into words

words = s.split()

## The 'split()' method splits the string s into a list of words.
## By default, 'split()' separates the string at spaces.

print (words)


## count occurences of each word

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


## output the word counts

for key, value in word_count.items():
    print (key, value)

