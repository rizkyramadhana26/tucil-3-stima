from Node import *
from BranchNBound import *

source = input("Ketik 1 untuk menggunakan puzzle random, ketik 2 untuk menggunakan puzzle dari file : ")
if source=='1':
    level = input("Ketik level puzzle yang diinginkan (1, 2, atau 3) : ")
    puzzle = randomPuzzle(level)
else:
    filename = input("Masukkan nama file (harus berada dalam folder test) : ")
    puzzle = readFile("test/"+filename)

bnb = BranchNBound(puzzle)

if bnb.check()==1:
    bnb.searchSolution()
    