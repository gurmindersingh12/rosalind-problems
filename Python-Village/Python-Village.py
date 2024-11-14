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
