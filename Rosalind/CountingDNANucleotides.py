# Problem
# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string s of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

#dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC' # DNA string
file = open(r'Data\rosalind_dna.txt') # open DNA string from file
dna = file.read()

'''
# Or a little bit prettier
A = dna.count('A')
C = dna.count('C')
G = dna.count('G')
T = dna.count('T')

print(int(A), ' ', int(C), ' ', int(G), ' ', int(T))
'''

print(int(dna.count('A')), ' ', int(dna.count('C')), ' ', int(dna.count('G')), ' ', int(dna.count('T'))) # print counts
