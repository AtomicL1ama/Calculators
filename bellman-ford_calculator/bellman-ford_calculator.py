#A simple tool I was inspired to make while completing Assignment 6 for CS4121 (Networking and Data Communications)
#bellman-ford_calculator.py takes a series of inputs from the terminal and produces a matrix of least-cost paths traversing each node

class BFCalculator:
    
    def __init__(self, numNodes):
        self.numNodes = numNodes
        self.nodeList = self.buildNodeList()
        self.costMatrix = self.buildCostMatrix()
        self.dvMatrix = self.getCostMatrix()
        
    def __str__(self):
        return self.printDV()

    def printDV(self):
        msg = ""
        for x in range(self.numNodes):
            msgTemp = "D{}= ".format(self.nodeList[x])
            for y in range(self.numNodes):
                msgTemp += "| " + str(self.dvMatrix[x][y]) + " | "
            msg += msgTemp + "\n"
        return msg
  
    def getCostMatrix(self):
        return self.costMatrix

    def getDVMatrix(self):
        return self.dvMatrix

    def vectorFactory(self):
        vect = []
        for x in range(self.numNodes):
            vect.append(99)
        return vect

    def matrixFactory(self):
        mtrx = []
        for x in range(self.numNodes):
            mtrx.append(self.vectorFactory())
        return mtrx

    def buildNodeList(self):
        nodes = []
        for x in range(self.numNodes):
            msg = "Name of node{}: "
            name = input(msg.format(x))
            nodes.insert(x,name)
        return nodes

    def buildCostMatrix(self):
        costMatrix = self.matrixFactory()
        for x in range(self.numNodes):
            for y in range(self.numNodes):
                if(x!=y):
                    msg = "What is the c({},{}): "
                    cost = int(input(msg.format(self.nodeList[x], self.nodeList[y])))
                    costMatrix[x][y] = cost
                else:
                    costMatrix[x][y] = 0
        return costMatrix 

    def getDV(self, node1Index, node2Index):
        leastCost = 99
        for x in range(self.numNodes):
            leastCost = min(leastCost, self.costMatrix[node1Index][x] + self.dvMatrix[x][node2Index])
        return leastCost
    
    def updateDVMatrix(self):
        for x in range(self.numNodes):
            for y in range(self.numNodes):
                self.dvMatrix[x][y] = self.getDV(x,y)

def runDV():
    numNodes = input("How many nodes?: ")
    calculator = BFCalculator(int(numNodes))
    calculator.updateDVMatrix()    
    print(calculator)

################   Main  ##################

runDV()
