# Problem
# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

# Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

# Given: A DNA string t having length at most 1000 nt.

# Return: The transcribed RNA string of t.

#dna = 'GATGGAACTTGACTACGTAAATT' # DNA string
file = open(r'Data\rosalind_rna.txt') # open DNA string from file
dna = file.read()

rna = dna.replace('T', 'U') # replace 'T' with 'U'

print(rna) # print string