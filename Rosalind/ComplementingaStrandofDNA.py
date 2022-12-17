# Problem
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string s of length at most 1000 bp.

# Return: The reverse complement sc of s.

#dna = 'AAAACCCGGT'

file = open(r'Data\rosalind_revc.txt') #open from file
dna = file.read()

revComp = dna

# Complement 'A' and 'T'
revComp = revComp.replace('A', 'B')
revComp = revComp.replace('T', 'A')
revComp = revComp.replace('B', 'T')

# Complement 'C' and 'G'
revComp = revComp.replace('C', 'D')
revComp = revComp.replace('G', 'C')
revComp = revComp.replace('D', 'G')

revComp = revComp[::-1] # reverse order of string

print(revComp) # print