# Implementing the graph class
import numpy as np


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def add_neighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return f"{self.id} is connected to: {str([x.id for x in self.connected])}"

    def get_nodes(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo.get(nbr)

    def remove_neighbor(self, nbr):
        if nbr in self.connectedTo:
            del self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.Hash = {}

    def add_vertex(self, key) -> None:
        newVertex = Vertex(key)
        self.vertList[newVertex.id] = newVertex
        self.Hash[self.numVertices] = newVertex.id
        self.numVertices += 1

    def getVertex(self, key):
        return self.vertList.get(key)

    def __contains__(self, key):
        return key in self.vertList

    def addEdge(self, f, t, weight=0):

        if f not in self:
            self.add_vertex(f)
        if t not in self:
            self.add_vertex(t)
        self.vertList[f].add_neighbor(t, weight)

    def getVertices(self):
        return self.vertList.keys()

    def getCount(self):
        return self.numVertices

    def getAdjMatrix(self):
        adj_matrix = np.zeros((self.getCount(), self.getCount()))
        for v1 in range(self.getCount()):
            for v2 in range(self.getCount()):
                if self.getVertex(self.Hash[v1]).getWeight(self.Hash[v2]):
                    adj_matrix[v1, v2] = self.getVertex(self.Hash[v1]).getWeight(
                        self.Hash[v2]
                    )
        return adj_matrix

    def removeVertex(self, key):

        # In the graph:
        del self.vertList[key]
        self.numVertices -= 1

        # Connections with other vertices:
        for v in self.vertList:
            self.vertList[v].remove_neighbor(key)
