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