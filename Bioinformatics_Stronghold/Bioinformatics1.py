
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


#####################################################################################
###########################  Computing GC Content  ##################################
#####################################################################################


fasta_sequence = """>seq1
AGCTATAG
"""

print(fasta_sequence)

s = "AGCTATAG"
print (s)

count_G = s.count('G')
count_C = s.count('C')

print(len(s))

GC_content = (count_G + count_C)/(len(s))

print (GC_content)

#########
### Problem

rosalind_seq = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""

print(rosalind_seq)

### initialize a dictionary to store sequences by their headers

fasta_dict = {}

## now split the input into lines and process them

current_header =  None ## to keep track of the current header

for line in rosalind_seq.strip().split("\n"):
    if line.startswith(">"): ## it is a header
        current_header = line[1:] # remove the ">" to get the header name
        fasta_dict[current_header] = ""  ## start a new entry in the dictionary
    else:
        ## otherwise it a part of sequence, append it to current header.
        fasta_dict[current_header] += line.strip()

## at this point fasta_dict{} contains headers as key and full sequences as values

print(fasta_dict)

## function to calculate GC content

def calculate_gc_content(sequence):
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    return ((g_count + c_count)/len(sequence))*100 if sequence else 0

## calculate and print GC content for GC content
for header, sequence in fasta_dict.items():
    gc_content = calculate_gc_content(sequence)
    print(f"{header}: {gc_content:.2f}%")



#### explanation of the above code

## Initializing Variables

## fasta_dict{}: An empty dictionary that will store the FASTA data.
## we will add headers as keys (e.g., "Rosalind_6404"), and the corresponding sequences as the values.

## current_header: A variable to keep track of the most recent header while processing the file.
## Initially set to `None`` because no header has been encountered yet.

## rosalind_seq.strip(): Removes any extra blank lines or whitespace at the start/end of the input string.

## .split("\n"): Splits the input string into individual lines based on newlines (\n).

## for line in ...: Iterates through each line of the input FASTA data.

## line.startswith(">"): Identifies header lines, which always start with > in FASTA format.

## line[1:]: Removes the > symbol to extract the header name (e.g., "Rosalind_6404").

## fasta_dict[current_header] = "": Adds the header as a key in the dictionary and initializes an empty string for its sequence.


## else:
#   fasta_dict[current_header] += line.strip()

## the above code sequence lines (i.e., lines that don’t start with >).

## line.strip(): Removes any whitespace or newline characters from the sequence line.
## fasta_dict[current_header] += ...: Concatenates the sequence line to the current header's sequence in the dictionary.

## fasta_dict.items(): Retrieves all header-sequence pairs from the dictionary.

## calculate_gc_content(sequence): Calculates the GC content for the current sequence.

## print(f"..."): Prints the header and the GC content (formatted to 2 decimal places).


