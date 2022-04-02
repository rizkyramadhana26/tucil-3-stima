from Node import *
from BranchNBound import *

filename = input("Masukkan nama file (harus berada dalam folder test) : ")

puzzle = readFile("test/"+filename)
bnb = BranchNBound(puzzle)

if bnb.check()==1:
    bnb.searchSolution()
    