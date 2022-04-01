class Node:
    numOfNodes = 0
    def __init__(self,prev,matrix,nullPos,level):
        Node.numOfNodes+=1
        self.name="n"+str(Node.numOfNodes)
        self.prev=prev
        self.matrix=matrix.copy()
        self.nullPos=nullPos
        self.level=level
        self.cost=self.countCost(matrix)
        

    def UP(self):
        if self.nullPos[0]==0:
            raise Exception("Cannot move it up !")
        else:
            temp = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            for k in range(4):
                for l in range(4):
                    temp[k][l]=self.matrix[k][l]
            i=self.nullPos[0]
            j=self.nullPos[1]
            temp[i][j] = temp[i-1][j]
            temp[i-1][j] = 0
            cost = self.countCost(temp)
            return Node(self.name,temp,(i-1,j),self.level+1)

    def DOWN(self):
        if self.nullPos[0]==3:
            raise Exception("Cannot move it down !")
        else:
            temp = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            for k in range(4):
                for l in range(4):
                    temp[k][l]=self.matrix[k][l]
            i=self.nullPos[0]
            j=self.nullPos[1]
            temp[i][j] = temp[i+1][j]
            temp[i+1][j] = 0
            cost = self.countCost(temp)
            return Node(self.name,temp,(i+1,j),self.level+1)
    def LEFT(self):
        if self.nullPos[1]==0:
            raise Exception("Cannot move it left !")
        else:
            temp = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            for k in range(4):
                for l in range(4):
                    temp[k][l]=self.matrix[k][l]
            i=self.nullPos[0]
            j=self.nullPos[1]
            temp[i][j] = temp[i][j-1]
            temp[i][j-1] = 0
            cost = self.countCost(temp)
            return Node(self.name,temp,(i,j-1),self.level+1)

    def RIGHT(self):
        if self.nullPos[1]==3:
            raise Exception("Cannot move it down !")
        else:
            temp = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            for k in range(4):
                for l in range(4):
                    temp[k][l]=self.matrix[k][l]
            i=self.nullPos[0]
            j=self.nullPos[1]
            temp[i][j] = temp[i][j+1]
            temp[i][j+1] = 0
            cost = self.countCost(temp)
            return Node(self.name,temp,(i,j+1),self.level+1)

    def __lt__(self,other):
        return self.cost < other.cost

    #UBAH DI SINI
    def countCost(self,puzzle):
        cost=0
        for i in range(4):
            for j in range(4):
                if puzzle[i][j]!=4*i+j+1 and puzzle[i][j]!=0:
                    cost+=1

        if puzzle[3][3]!=0:
            cost+=1
        return cost+self.level

    def isGoal(self):
        goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
        return self.matrix == goal

    def print(self):
        print("=====================")
        for i in range(3):
            print("* ",end="")
            for j in range(3):
                if self.matrix[i][j]!=0 :
                    print(str(self.matrix[i][j]).ljust(2),end="")
                else:
                    print("  ",end="")
                print(" | ",end="")
            if self.matrix[i][3]!=0 :
                print(str(self.matrix[i][3]).ljust(2),end="")
            else:
                 print("  ",end="")
            print(" *")
            print("*-------------------*")
        print("* ",end="")
        for j in range(3):
            if self.matrix[i][j]!=0 :
                print(str(self.matrix[3][j]).ljust(2),end="")
            else:
                print("  ",end="")
            print(" | ",end="")
        print(str(self.matrix[3][3]).ljust(2),end="")
        print(" *")
        print("*-------------------*")
        print("=====================")