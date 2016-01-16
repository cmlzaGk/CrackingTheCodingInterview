class Node:
    def __init__(self, data, adjacencyList=[]):
        self.data = data
        self.adjacencyList = adjacencyList
    def AddAjacencyNode(self, adj):
        self.adjacencyList.append(adj)
    def AddAjacencyList(self, adjacencyList):
        self.adjacencyList = adjacencyList
