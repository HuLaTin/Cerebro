# Problem

# Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.
# Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

# Return: The Hamming distance dH(s,t).

from scipy.spatial.distance import hamming

file = open(r'Data\rosalind_hamm.txt')
text = file.readlines()

#string1 = 'GAGCCTACTAACGGGAT'
#string2 = 'CATCGTAATGACGGCCT'

string1 = text[0].strip()
string2 = text[1].strip()

string1 = list(string1) # typecase to list
string2 = list(string2)
hamming(string1, string2) * len(string1)