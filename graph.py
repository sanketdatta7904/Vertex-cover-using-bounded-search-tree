class Graph:
    def __init__(self):
        self.nodes = {}
        self.sortedNodes = []
        self.vc = []

        
    
    def getNumberOfNodes(self):
        return len(self.nodes)
    def getNumberOfEdges(self):
        num = 0
        for i in range (len(self.nodes)) :
            num += self.nodes[i].neighbor.size
        return num/2
    
    



    