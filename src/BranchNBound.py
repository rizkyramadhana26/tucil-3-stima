from Node import *
from queue import PriorityQueue
from utils import *
from time import sleep,time

class BranchNBound :
    def __init__(self,puzzle):
        self.visited={}

        found = False
        i=0
        while(not found and i<4):
            j=0
            while(not found and j<4):
                if puzzle[i][j]==16:
                    found=True
                else:
                    j+=1
            if not found :
                i+=1

        root = Node("NO",puzzle,(i,j),0)
        self.start = root
        self.nodeList={root.name : root}
        self.prioQ = PriorityQueue()
        self.prioQ.put((root.cost,root))

    def check(self):
        kurangs = [0 for i in range(16)]
        flat = self.start.matrix[0]+self.start.matrix[1]+self.start.matrix[2]+self.start.matrix[3]
        print(flat)

        for i in range(16):
            kurang=0
            for j in range(i+1,16):
                if flat[j]<flat[i]:
                    kurang+=1
            kurangs[self.start.matrix[i//4][i%4]-1]=kurang

        print("PUZZLE AWAL")
        self.start.print()
        sum=0
        for i,kurang in enumerate(kurangs):
            print(f"Nilai KURANG({i+1})={kurang}")
            sum=sum+kurang
        if (self.start.nullPos[0]+self.start.nullPos[1])%2==1:
            sum+=1
        print(f"Jumlah dari KURANG(i) ditambah X : {sum}")
        if sum%2==0:
            print("Puzzle dapat diselesaikan !")
            return 1
        else :
            print("Puzzle tidak dapat diselesaikan !")
            return 0

    def searchSolution(self):
        print("Mencari solusi...")
        start = time()
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

        end = time()
        current = ans.name
        steps=[]
        while current!="NO":
            steps.insert(0,self.nodeList[current])
            current=self.nodeList[current].prev
        input("Tekan ENTER untuk memulai animasi")
        n = len(steps)
        for i in range(n-1):
            steps[i].print()
            print ("\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A")
            sleep(1)
        steps[n-1].print()
        sleep(1)
        choice = input("Ingin mencetak semua langkah (y/n) ? ")
        if choice=='y':
            for i in range(n):
                steps[i].print()

        print("Jumlah node yang dibangkitkan : ",Node.numOfNodes)
        print("Waktu yang dibutuhkan : ", end-start, " detik")