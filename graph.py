class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, _id):
        self.vertices[_id] = Vertex(_id)

    def getVertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertices

    def addEdge(self, u, v, w=0):
        if u not in self.vertices:
            self.addVertex(u)
        if v not in self.vertices:
            self.addVertex(v)
        self.vertices[u].addNeighbor(v, w)

    def getVertices(self):
        return list(self.vertices.keys())

    def __iter__(self):
        return iter(self.vertices.values())

class Vertex:
    def __init__(self, _id):
        self._id = _id
        self.connected = {}
        self.pred = None

    def getId(self):
        return self._id

    def addNeighbor(self, v, w=0):
        self.connected[v]=w

    def getWeight(self,v):
        return self.connected[v]

    def getConnected(self):
        return self.connected

    def setPred(self, p):
        self.pred=p

    def getPred(self):
        return self.pred

def main():
    print "Main"
    graph = Graph()
    graph.addVertex(1)
    graph.addVertex(2)
    graph.addVertex(3)
    graph.addEdge(1,3,2)
    graph.addEdge(2,3,1)
    graph.addEdge(1,2,3)
    print graph.getVertices()
    graph.getVertex(3).setPred(1)
    print graph.getVertex(3).getPred()

    graph = Graph()
    graph.addEdge(1,3,4)
    graph.addEdge(3,7,2)
    graph.addEdge(1,2,3)
    print graph.getVertices()
    print graph.getVertex(1).getWeight(2)
    

if __name__ == '__main__':
    main()
