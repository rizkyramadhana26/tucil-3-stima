from random import randint
from Node import *

def toString(puzzle):
    return ','.join(str(item) for innerlist in puzzle for item in innerlist)

def readFile(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [line.strip().split() for line in lines]
    for i in range(4):
        for j in range(4):
            lines[i][j] = int(lines[i][j])
    return lines

def randomPuzzle(n):
    if(n==1):
        steps=15
    elif(n==2):
        steps=30
    else:
        steps=60

    root = Node("NO",[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],(3,3),0)

    i=0
    while i<steps :
        y = randint(1,4)
        if y==1 :
            try:
                root=root.UP()
                i+=1
            except:
                pass
        elif y==2 :
            try:
                root=root.DOWN()
                i+=1
            except:
                pass
        elif y==3 :
            try:
                root=root.LEFT()
                i+=1
            except:
                pass
        else :
            try:
                root=root.RIGHT()
                i+=1
            except:
                pass
    Node.numOfNodes = 0
    return root.matrix
