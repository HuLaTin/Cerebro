# A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

# Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).

# A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

# import numpy as np
# file = open(r'Data\rosalind_cons.txt') # open DNA string from file
# text = file.read()

# text = text.split('>') # split text on '\n'
# text = text.split('\n', 1)

# DNA = [x for x in text if not '>' in x] #removing '>Rosalind' strings from list

from Bio import SeqIO
import numpy as np


file = r"Data\rosalind_cons.txt"
sequences = []

with open(file, "r") as file_handle:
    for record in SeqIO.parse(file_handle, "fasta"):
        sequences.append(record.seq)



matrix = []
for i in sequences:
    matrix.append([j for j in i])
M = np.array(matrix)#.reshape(len(matrix),len(matrix[0]))

#convert string matrix into profile matrix
A = []
C = []
G = []
T = []
for i in range(len(matrix[0])):
    A_count = 0
    C_count = 0
    G_count = 0
    T_count = 0
    for j in M[:,i]:
        if j == "A":
            A_count += 1
        elif j == "C":
            C_count += 1
        elif j == "G":
            G_count += 1
        elif j == "T":
            T_count += 1
    A.append(A_count)
    C.append(C_count)
    G.append(G_count)
    T.append(T_count)

profile_matrix = {"A": A, "C": C, "G": G, "T": T}
# for k, v in profile_matrix.items():
#     print(k + ": " + " ".join(str(x) for x in v))

#get consensus string
P = []
P.append(A)
P.append(C)
P.append(G)
P.append(T)
profile = np.array(P).reshape(4, len(A))
consensus = []
for i in range(len(A)):
    if max(profile[:,i]) == profile[0,i]:
        consensus.append("A")
    elif max(profile[:,i]) == profile[1,i]:
        consensus.append("C")
    elif max(profile[:,i]) == profile[2,i]:
        consensus.append("G")
    elif max(profile[:,i]) == profile[3,i]:
        consensus.append("T")
print("".join(consensus))
for k, v in profile_matrix.items():
    print(k + ": " + " ".join(str(x) for x in v))