class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vert(self, _id):
        self.vertices[_id] = Vertex(_id)

    def get_vert(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def add_edge(self, u, v, w=0):
        if u not in self.vertices:
            self.add_vert(u)
        if v not in self.vertices:
            self.add_vert(v)
        self.vertices[u].add_conn(v, w)

    def get_vertices(self):
        return list(self.vertices.keys())

    def __contains__(self, n):
        return n in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())


class Vertex:
    def __init__(self, _id):
        self._id = _id
        self.connected = {}
        self.pred = None

    def get_id(self):
        return self._id

    def add_conn(self, v, w=0):
        self.connected[v] = w

    def get_weight(self, v):
        return self.connected[v]

    def get_conn(self):
        return self.connected

    def set_pred(self, p):
        self.pred = p

    def get_pred(self):
        return self.pred


def main():
    print "Main"
    graph = Graph()
    graph.add_vert(1)
    graph.add_vert(2)
    graph.add_vert(3)
    graph.add_edge(1, 3, 2)
    graph.add_edge(2, 3, 1)
    graph.add_edge(1, 2, 3)
    print graph.get_vertices()
    graph.get_vert(3).set_pred(1)
    print graph.get_vert(3).get_pred()

    graph = Graph()
    graph.add_edge(1, 3, 4)
    graph.add_edge(3, 7, 2)
    graph.add_edge(1, 2, 1)
    print graph.get_vertices()
    print graph.get_vert(1).get_weight(2)

    graph.add_edge(3, 4, 3)
    graph.add_edge(2, 5, 4)
    graph.add_edge(2, 3, 1)
    print graph.get_vertices()
    print graph.get_vert(1).get_conn()
    print graph.get_vert(2).get_conn()
    print graph.get_vert(7).get_conn()
    graph.get_vert(2).set_pred(1)

    print graph.get_vert(graph.get_vert(2).get_pred()).get_id() == graph.get_vert(2).get_pred()


if __name__ == '__main__':
    main()
