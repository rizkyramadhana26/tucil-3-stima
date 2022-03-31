def findNull(puzzle):
    found = False
    i=0
    j=0
    while(not found and i<4):
        while(not found and j<4):
            if puzzle[i][j]==0:
                found=True
            else:
                j+=1
        i+=1
    return (i,j)

def countCost(puzzle):
    cost=0
    for i in range(4):
        for j in range(4):
            if puzzle[i][j]!=4*i+j+1 :
                cost+=1
    return cost
#prioQ, prioQLength, nodeList, numOfNodes, visited, visitedLength
def enqueue(prioQ, prioQLength, nodeList, numOfNodes, visited, visitedLength,elmt): #cek udah pernah dikunjungi belum
    found = False
    i=0
    while (not found and i<visitedLength):
        if elmt['matrix']==visited[i]['matrix']:
            found=True
            numOfNodes-=1
        else:
            i+=1
    if not found:
        found = False
        i=prioQLength-1
        while (not found and i>=0):
            if prioQ[i]["cost"]>=elmt["cost"]:
                i-=1
            else:
                found=True
        prioQ.insert(i+1,elmt)
        prioQLength+=1
        nodeList[elmt['name']]=elmt
    return prioQ, prioQLength, nodeList, numOfNodes, visited, visitedLength

def makeNode(name,prev,matrix,nullPos,cost):
    node={}
    node['name']=name
    node['prev']=prev
    node['matrix']=matrix
    node['nullPos']=nullPos
    node['cost']=cost
    return node