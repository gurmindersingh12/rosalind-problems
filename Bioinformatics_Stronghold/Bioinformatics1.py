
#########################################################################################
########################    Bioinformatics Stronghold    ################################
#########################################################################################

### problem

s = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

print (s)

len(s)

count_A = s.count('A')
count_T = s.count('T')
count_G = s.count('G')
count_C = s.count('C')

print (count_A, count_C, count_G, count_T)


## dataset

dataset = 'CGCTATAGAACGAGTAGTAATGGGTGTATAGCATATTAACTATGCTGGGTATTCGATTCTCTCCTAGCCATTATAAGTGTCTTTCGATTCAGGCGTGCGCCCGTAGCGAGTCCGACGAATAAGGAGTAGCGACTGAGTTCAACTGCCCGAGGCCGCAATCTGCAGCCTCACCCTTAAGTGCTGCTGTACCGCACAGAACGCAGGTGTTCTCCAGGCTCGAATACAGTTCCGGGTGATCTCGGACTTCTGCCACAACGTGAGCTGTTCATTTTTGCGCAACCTACTGAGAGCTGAGAGGCCCACCTTTATAACTGGGGCCTTCGTCCAAAGGCCTTAACGGAGCAGCACTAAACAGTTTAAAAACCCTGTGTCCCGTCTCCATAGATTAAACTTGGATGTCATAAGCACTTGTTTTTTGGGACTATGGGTTGAATTCACCCGGGTTCAGAAGAATCGCGTACTAAGCATCCTAAGAGGACATTGTAGCCGATATCACTGAGGCTGAGACCGATCTTGCTTTGAGCACGTCAAAAAAGGAAAAGAGGGGGATGGCCATTGGGGAGACAGGTCATAGGTGAAACTAGACATCATCTATTATTCATAAAAACCTTTTGGCTGTAACGCATGGGTCCAATTTCGGAGCGCACAAATCCGTGGGTTTTTCTGCTCTTCCCGTTTGGAGAAGAGGAGGCTCCAACCTCCAGTGCCACTGCCACACGTAATTACAATTCTGTCTTAACTACCGTGGAAAGCACCGCGCGCAGACGCGCCGTTCTAATTGCGAATACAGCCAGACACTAAGCAGGGTCAGTATTTTCTAACCGAAAGCTGGCTAGGTTGTAATGTCGCCGGTGATTACCGATTGAGTGGTGTTTGCAATGCCTCCA'

print (dataset)

len(dataset)

count_A = dataset.count('A')
count_T = dataset.count('T')
count_G = dataset.count('G')
count_C = dataset.count('C')

print (count_A, count_C, count_G, count_T)

#########################################################################################################################


t = "GATGGAACTTGACTACGTAAATT"
print (t)

u = t.replace ('T', 'U')
print(u)


t2 = "ACTTTGTTGTATCTAAGGTCCCCCCGCTACGAACGAAAGGGTTTGGTTTGCTCTATACCTGTGTCACTAATGAAGTGACCTGGCCGCAAACCACGGGGGTGTTAGACTACAATTTATAAGACGGTGATTAGGGCCAGCGCACTGTAGGATACGTCAGGACCTCGTTCGAGTAGCCATCTCAGTTCCTCACGCTTCGACATGTGCGATGAGGAACTTTTTTCTCCATGCTAAGTGTGCATGCATCACGAGCCAACATTAGTCAGGATTCAGTTGACTCCGATGCGGAGAATTCTCAACTGCCCTTTGCTAGGCCACTATACTACAGCGCGTGCCAACTTGATGTTGAATATAGCGACCAGCGTTTGCTGCATATCCGGTAGCTGATATCACTCATGCCCATTGTATATCTGCCCTGGTGGTACGTCGTACGAGCAATGCTGCGATAATTAAATGGTGCGCCGGACGAGGCAAGTGGGCCGTCTCGCCAAACGCACCACGTCTCAGCTATATCCATTAGCAGAATGAAAGCCACATAGAAGAATGCGTGGGTGATGTTTGATGAAGAATTCAATGCATACACGCTTACCGGGTGGTGTGCTAACAAGGGGATCGTCCGGAAAGAGTGGCTGGAACTACTCAGCACAATCATGGGCTGGCGCAGACCACCTGTCTATCACACTCAGCTGCTACATCACACGGCTTGGGTAGTTCCCGGTGAGATTATCTCTATAGAACTAACTCATCGTATATAGAAACGGCCGCGGGTCGGTTACTCCCCCTTGGCAAGGCCCCCACTCCAGCCACAATGTTATCACTGTTTCGCTAAGCCGCATTTCTGGAGCAGGCTGCAATTAGAGGTAGTGGATGGAACGCGCATCAGGCACAATGACCGAAATTTCTTATGCGCGGCTTCCTCATCCGGATAA"

print(t2)

u2 = t2.replace ('T', 'U')
print(u2)


############################################################################################################

s = 'AAAACCCGGT'
print (s)

### complement mapping

complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

### Find the complement of each nucleotide and reverse the string

reverse_complement_s = "".join(complement[base] for base in reversed(s))

## "".join(): Joins the complemented characters into a single string.

## reversed(s): Reverses the input DNA string. 

## 'complement[base] for base in reversed(s)': Replaces each nucleotide in the reversed string with its complement using the complement dictionary.


print (reverse_complement_s)


### problem dataset

s = 'TAGTCACCTCCATAGCCAGGTGTGATTGTGGATGACCGCGTGTAAGGCCGTCGATATGCTATGTCGGTAAGTTACGTATTAATTACAAATGACGGGCGTAGGTGTTACTGCCGTAGCTTAGTCTCGTAACACGTATCTCTGCCACTCGCGTCCGGTGCCACTAAGCAACATAAAATGCAGCTCGAAGGATACGTCAATCACACTTTTGCACAAACAGTCCGTAATGTTTAGCAATATATAGAAGAATGTCCCGGAGGCATCCCTCATCGTGAACTGTGATGAGACGAAACAAATGCAGCAACCCTTACCGCATCGCTCATTGTTGTCAGTCGTCCCGCTCATAGTGATGGATCTGAGATCATGTCCTACATCCCTACGCTTCGTGCTATTCGTACTAAACTTCTACAATGCTCTGAAAAGAAAACTGGAGGCATATTTGGAGTGAATCCAAAAGGGGGGTTCCCTTGTGCTGTGAGGGTAGAGCAATGGAAGGCAAAGTTGTGCGGTTGTGACATCTCTGGTAGCTATCCTAGAAATAGGTTACGATTCTGTGAATGGCTTTATTCCTCAACGACGAATCGCATACTCTCATCTAATGTCCGACGGCAGTTACGGCCCCACACACGGGGACCAATGCTTAAAGGTGCTGTCTGTCTGAATCACCTAGGTCGACAACCCCAGGTAATGACAGAACTGGGCATGTACACGCTCTAATACATCGCGGTACTCTTATGTGGCTGAGTTCGACGATGACCTGGGGATGAATTGGATCAAGAGAACCTTAGTACCAAAAGGGTACTCTACTCTCTATACTAGCAATTGCGCGATCACTTATTCGTATATGTCGATCGTGACACGGTCGCCGCCCGCCCACACTTACTGACGAGTCCAACAGGCAAATCTAACATCGCGGCGTAAAAGAAATGGCTGTTGT'


print (s)

### complement mapping

complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

### Find the complement of each nucleotide and reverse the string

reverse_complement_s = "".join(complement[base] for base in reversed(s))


print (reverse_complement_s)

######################################################################################################################


#######################################################################################################
######################    Rabbits and Recurrence Relations  ###########################################
#######################################################################################################

## Recurrence relation and Fibonacci sequence

##  In case of Fibonacci's rabbits, any given month will contain the rabbits that were alive the previous month, plus any new
## offspring. A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive
## two months prior. As a result, if F(n) respresents the number of rabbit pairs after n-th month, then we obtain the Fibonacci
## sequence having terms Fn that are defined by the recurrence relation; F(n) = F(n-1) + F(n-2) (with F1=F2=1 to initiate the sequence). 


## Problem

## The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, 
## every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

n = 5
k = 3

## Problem understanding ##

## we can start with 1 rabbit in the first month month.
## rabbits mature after 1 month i.e., they start reproducing in their second month.
## each mature pair produce `k` new pairs of rabbits per month.
## the task is to calculate total number of rabbit pairs after `n` months.


## Formula:
## this problem can be modeled using a modified Fibanacci recurrence.

# F(n) = F(n-1) + k.F(n-2)

## F(n-1) is the rabbit pair alive from previous month
## k.F(n-2) is the rabbit pairs produced by mature rabbits.

### Manual way

## n=5, k=3; assumption F1=F2=1
## Month 1: F(1) = 1
## Month 2: F(2) = 1
## Month 3: F(3) = F(2) + 3.F(1) = 1+3 = 4
## Month 4: F(4) = F(3) + 3.F(2) = 4+3 = 7
## Month 5: F(5) = F(4) + 3.F(3) = 7+12 = 19

## output answer = 19

n = 5
k = 3

def rabbit_pairs(n, k):
    ## intialize the first 2 months
    if n == 1 or n == 2:
        return 1
    
    ## variables to store F(n-1), F(n-2)

    prev, curr = 1, 1
    ## prev represents F(n−2): the number of rabbit pairs from two months ago.
    ## curr represents F(n−1): the number of rabbit pairs from the previous month.

    ## calculate rabbit pairs from month 3 to n
    for _ in range(3, n+1):
       next_val = curr + k*prev
       prev, curr = curr, next_val

       ## next_val = curr + k * prev
       ### Uses the formula: F(n)=F(n−1)+k⋅F(n−2)

       ## prev, curr = curr, next_val
       ## Updates the variables for the next iteration:
       ## prev (F(n-2)) becomes the current value of curr.
       ## curr (F(n-1)) becomes the newly calculated value, next_val.

    return curr

## After the loop ends, curr will hold F(n)F(n), the total number of rabbit pairs in month n.

## input values
n, k = 5, 3
print(rabbit_pairs(5, 3))


## Downloaded Dataset


def rabbit_pairs(n, k):
    ## intialize the first 2 months
    if n == 1 or n == 2:
        return 1
    
    ## variables to store F(n-1), F(n-2)

    prev, curr = 1, 1
    
    ## calculate rabbit pairs from month 3 to n
    for _ in range(3, n+1):
       next_val = curr + k*prev
       prev, curr = curr, next_val

    return curr

## input values
n, k = 31, 2
print(rabbit_pairs(31, 2))
### output: 715827883


#################################################################################################################
#################################################################################################################


