from Node import *
from BranchNBound import *

puzzle = [[1,3,4,15],[2,0,12,5],[7,6,11,14],[8,9,10,13]]

# n1 = Node("NO",puzzle,(3,2))
# n2 = n1.UP()
# n4 = n1.LEFT()

bnb = BranchNBound(puzzle)
# bnb.prioQ.put((n2.cost,n2))
# bnb.prioQ.put((n4.cost,n4))
# print(bnb.prioQ.get()[1].matrix)
# print(bnb.prioQ.get()[1].matrix)
# print(bnb.prioQ.get()[1].matrix)
bnb.searchSolution()
print(Node.numOfNodes)