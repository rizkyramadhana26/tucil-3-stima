from Node import *
from queue import PriorityQueue
from utils import *

class BranchNBound :
    def __init__(self,puzzle):
        self.visited={}

        found = False
        i=0
        while(not found and i<4):
            j=0
            while(not found and j<4):
                if puzzle[i][j]==0:
                    found=True
                else:
                    j+=1
            if not found :
                i+=1

        root = Node("NO",puzzle,(i,j),0)
        self.nodeList={root.name : root}
        self.prioQ = PriorityQueue()
        self.prioQ.put((root.cost,root))

    def searchSolution(self):
        found = False
        while(self.prioQ and not found):
            now = self.prioQ.get()[1]
            try:
                newNode = now.UP()
                self.nodeList[newNode.name]=newNode
                newString = toString(newNode.matrix)
                if not self.visited.get(newString,False) :
                    if newNode.isGoal():
                        found=True
                        ans=newNode
                    else:
                        self.prioQ.put((newNode.cost,newNode))
            except :
                pass


            try:
                newNode = now.DOWN()
                self.nodeList[newNode.name]=newNode
                newString = toString(newNode.matrix)
                if not self.visited.get(newString,False) :
                    if newNode.isGoal():
                        found=True
                        ans=newNode
                    else:
                        self.prioQ.put((newNode.cost,newNode))
            except :
                pass


            try:
                newNode = now.RIGHT()
                self.nodeList[newNode.name]=newNode
                newString = toString(newNode.matrix)
                if not self.visited.get(newString,False) :
                    if newNode.isGoal():
                        found=True
                        ans=newNode
                    else:
                        self.prioQ.put((newNode.cost,newNode))
            except :
                pass

            try:
                newNode = now.LEFT()
                self.nodeList[newNode.name]=newNode
                newString = toString(newNode.matrix)
                if not self.visited.get(newString,False) :
                    if newNode.isGoal():
                        found=True
                        ans=newNode
                    else:
                        self.prioQ.put((newNode.cost,newNode))
            except :
                pass

            self.visited[toString(now.matrix)] = True

        current = ans.name
        while current!="NO":
            #print(self.nodeList[current].matrix)
            self.nodeList[current].print()
            current=self.nodeList[current].prev