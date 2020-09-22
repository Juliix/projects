#Script to design primers for RT stem-loop
#Made by Julie Mallet September 17th 2020

import re

# Principal function that get the microRNA sequence from the user
# and check the validity of the microRNA sequence
def core():
    seqmiRNA = input("Enter the sequence of your microRNA:\n")
    seqmiRNA = seqmiRNA.upper()


    # regex for detect another letter than ATGC & number
    regex = r"[^ATGC]"
    if re.finditer(regex, seqmiRNA):
        print("\033[91mdOnly ATGC sequence is autorized \033[0m")
        core()
core()

def printseq():
    print("This is the sequence of the microRNA:")
    print(seqmiRNA)
printseq()

last6var = seqmiRNA[-6:] #Select the last 6 nucleotides of the microRNA
leftovers = seqmiRNA[:-6] #Select the rest of the microRNA


#Conversion of each nucleotide in its complement
# for each i
if v1 == "A":
    v1 = "T"
else :
    if v1 == "T":
        v1 = "A"
    else :
        if v1 == "G":
            v1 = "C"
        else :
            if v1 == "C":
                v1 = "G"

if v2 == "A":
    v2 = "T"
else :
    if v2 == "T":
        v2 = "A"
    else :
        if v2 == "G":
            v2 = "C"
        else :
            if v2 == "C":
                v2 = "G"

if v3 == "A":
    v3 = "T"
else :
    if v3 == "T":
        v3 = "A"
    else :
        if v3 == "G":
            v3 = "C"
        else :
            if v3 == "C":
                v3 = "G"

if v4 == "A":
    v4 = "T"
else :
    if v4 == "T":
        v4 = "A"
    else :
        if v4 == "G":
            v4 = "C"
        else :
            if v4 == "C":
                v4 = "G"

if v5 == "A":
    v5 = "T"
else :
    if v5 == "T":
        v5 = "A"
    else :
        if v5 == "G":
            v5 = "C"
        else :
            if v5 == "C":
                v5 = "G"
if v6 == "A":
    v6 = "T"
else :
    if v6 == "T":
        v6 = "A"
    else :
        if v6 == "G":
            v6 = "C"
        else :
            if v6 == "C":
                v6 = "G"

universalloop = "GTCGTATCCAGTGCAGGGTCCGAGGTATTCGCACTGGATACGAC"
primerRT = universalloop+v6+v5+v4+v3+v2+v1 #will give you the primer necessary for RT specific of the last 6 nucleotides of the microRNA
primerFwdqPCR = "GCGGCG"+leftovers #will give you the primer for the qPCR

print("Your primer for the RT is :")
print(primerRT)
print("Your primer Forward for qPCR:")
print(primerFwdqPCR)
