from utils import *

puzzle = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,0,15]]
goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
nodeList = {}
numOfNodes = 0
prioQ = []
prioQLength = 0
visited = []
visitedLength = 0

if puzzle!=goal :
    node = {}
    numOfNodes+=1
    name="n"+numOfNodes
    # node['name']=name
    # node['prev']="NO"
    # node['matrix']=puzzle
    # node['nullPos']=findNull(puzzle)
    # node['cost']=countCost(puzzle)
    node = makeNode(name,"NO",puzzle,findNull(puzzle),countCost(puzzle))
    prioQ, prioQLength, nodeList, numOfNodes, visited, visitedLength = enqueue(prioQ,prioQLength,node,visited)
    

found = False
while(prioQ and not found):
    now = prioQ.pop(0)
    if(now['nullPos'][0]!=0): #BUKAN PALING ATAS
        temp = now['matrix']
        temp[now['nullPos'][0]][now['nullPos'][1]] = temp[now['nullPos'][0]-1][now['nullPos'][1]]
        temp[now['nullPos'][0]-1][now['nullPos'][1]] = 0
        if temp==goal:
            found=True
            ans = temp['name']
        else:
            numOfNodes+=1
            name = 'n'+numOfNodes
            node = makeNode(name,now["name"],temp,(now['nullPos'][0]-1,now['nullPos'][1]),countCost(temp))
            prioQ, prioQLength, nodeList, numOfNodes, visited, visitedLength = enqueue(prioQ, prioQLength, nodeList, numOfNodes, visited, visitedLength,node)

    
    if(now['nullPos'][0]!=3): #BUKAN PALING BAWAH
        temp = now['matrix']
        temp[now['nullPos'][0]][now['nullPos'][1]] = temp[now['nullPos'][0]+1][now['nullPos'][1]]
        temp[now['nullPos'][0]+1][now['nullPos'][1]] = 0
        if temp==goal:
            found=True
            ans = temp['name']
        else:
            numOfNodes+=1
            name = 'n'+numOfNodes
            node = makeNode(name,now["name"],temp,(now['nullPos'][0]+1,now['nullPos'][1]),countCost(temp))
            prioQ, prioQLength, nodeList, numOfNodes, visited, visitedLength = enqueue(prioQ, prioQLength, nodeList, numOfNodes, visited, visitedLength,node)

    if(now['nullPos'][1]!=0): #BUKAN PALING KIRI
        temp = now['matrix']
        temp[now['nullPos'][0]][now['nullPos'][1]] = temp[now['nullPos'][0]][now['nullPos'][1]-1]
        temp[now['nullPos'][0]][now['nullPos'][1]-1] = 0
        if temp==goal:
            found=True
            ans = temp['name']
        else:
            numOfNodes+=1
            name = 'n'+numOfNodes
            node = makeNode(name,now["name"],temp,(now['nullPos'][0],now['nullPos'][1]-1),countCost(temp))
            prioQ, prioQLength, nodeList, numOfNodes, visited, visitedLength = enqueue(prioQ, prioQLength, nodeList, numOfNodes, visited, visitedLength,node)


    if(now['nullPos'][1]!=3): #BUKAN PALING KANAN
        temp = now['matrix']
        temp[now['nullPos'][0]][now['nullPos'][1]] = temp[now['nullPos'][0]][now['nullPos'][1]+1]
        temp[now['nullPos'][0]][now['nullPos'][1]+1] = 0
        if temp==goal:
            found=True
            ans = temp['name']
        else:
            numOfNodes+=1
            name = 'n'+numOfNodes
            node = makeNode(name,now["name"],temp,(now['nullPos'][0],now['nullPos'][1]+1),countCost(temp))
            prioQ, prioQLength, nodeList, numOfNodes, visited, visitedLength = enqueue(prioQ, prioQLength, nodeList, numOfNodes, visited, visitedLength,node)

    visited.append(now['name'])

if found :
    now = ans
    while now!= "NO" :
        print(nodeList[now]['matrix'])
        now = nodeList[now]['prev']

    




