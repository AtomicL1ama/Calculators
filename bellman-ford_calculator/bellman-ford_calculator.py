#A simple tool I was inspired to make while completing Assignment 6 for CS4121 (Networking and Data Communications)
#bellman-ford_calculator.py takes a series of inputs from the terminal and produces a matrix of least-cost paths traversing each node

class BFCalculator:
    
    def __init__(self, numNodes):
        self.numNodes = numNodes
        self.nodeList = self.buildNodeList()
        self.costMatrix = self.buildCostMatrix()
        self.dvMatrix = self.buildDVMatrix()
        
    def __str__(self):
        return self.printDV()

    def printDV(self):
        msg = "\n######## Bellman-Ford Distance Vector ########\n\n"
        for x in range(self.numNodes):
            msgTemp = "D{}= ".format(self.nodeList[x])
            for y in range(self.numNodes):
                msgTemp += "| " + str(self.dvMatrix[x][y]) + " | "
            msg += msgTemp + "\n"
        msg += "\n##############################################\n"
        return msg
  
    def getCostMatrix(self):
        return self.costMatrix

    def getDVMatrix(self):
        return self.dvMatrix

    def setCostMatrixValue(self,x, y, cost):
        self.getCostMatrix()[x][y] = cost

    def setDVMatrixValue(self,x, y, distance):
        self.getDVMatrix()[x][y] = distance

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
                    cost = self.getCost(x,y)
                    costMatrix[x][y] = cost
                else:
                    costMatrix[x][y] = 0
        return costMatrix

    def buildDVMatrix(self):
        dvMatrix = self.getCostMatrix()
        return dvMatrix

    def getCost(self, x, y):
        msg = "What is the c({},{}): "
        cost = int(input(msg.format(self.nodeList[x], self.nodeList[y])))
        return cost

    def getLeastCost(self, node1Index, node2Index):
        leastCost = 99
        for x in range(self.numNodes):
            leastCost = min(leastCost, self.getCostMatrix()[node1Index][x] + self.getDVMatrix()[x][node2Index])
        return leastCost
    
    def updateDVMatrix(self):
        for x in range(self.numNodes):
            for y in range(self.numNodes):
                self.setDVMatrixValue(x,y,self.getLeastCost(x,y))

    def runBFCalculator(self):
        self.updateDVMatrix()
        print(self)

def runDV():
    numNodes = input("How many nodes?: ")
    calculator = BFCalculator(int(numNodes))
    calculator.runBFCalculator()

################   Main  ##################

runDV()
