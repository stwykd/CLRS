class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, _id):
        self.vertices[_id] = Vertex(_id)

    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return -1

    def add_edge(self, u, v, w=0):
        if u not in self.vertices:
            self.add_vertex(u)
        if v not in self.vertices:
            self.add_vertex(v)
        self.vertices[u].add_conn(v, w)

    def get_vertices(self):
        return list(self.vertices.keys())

    def bfs(self, s):
        level = {s: 0}
        parent = {s: None}
        i = 1
        frontier = [s]
        while frontier:
            next = []
            for u in frontier:
                for v in self.get_vertex(u).get_conn():
                    if v not in level:
                        level[v] = i
                        parent[v] = u
                        next.append(v)
            print "frontier:"
            print frontier
            frontier = next
            i += 1

    def dfs(self):
        for u in self.get_vertices():
            self.get_vertex(u).set_color('white')
            print '{0} is white'.format(str(self.get_vertex(u).get_id()))
            self.get_vertex(u).set_parent(None)
        for u in self.get_vertices():
            if self.get_vertex(u).get_color() == 'white':
                self.dfs_visit(u)

    def dfs_visit(self, u):
        self.get_vertex(u).set_color('gray')
        print '{0} is gray'.format(str(self.get_vertex(u).get_id()))
        for v in self.get_vertex(u).get_conn():
            if self.get_vertex(v).get_color == 'white':
                self.get_vertex(v).set_parent(u)
                self.dfs_visit(v)
        self.get_vertex(u).set_color('black')
        print '{0} now black!'.format(str(self.get_vertex(u).get_id()))

    def dijkstra(self, s):
        s = []
        from Queue import PriorityQueue
        q = PriorityQueue()
        for v in self.get_vertices():
            q.put(v)
        while q.qsize() > 0:
            u = q.get()
            s.append(u)
            print "s is now {0}".format(str(s))
            for v in self.get_vertex(u).get_conn():
                self.relax(u, v, self.get_vertex(u).get_weight(v))

    def relax(self, u, v, w):
        if self.get_vertex(v).get_dist() > self.get_vertex(u).get_dist()+w:
            self.get_vertex(v).set_dist(self.get_vertex(u).get_dist()+w)
            self.get_vertex(v).set_parent(u)

    def __contains__(self, n):
        return n in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())


class Vertex:
    def __init__(self, _id):
        self._id = _id
        self.connected = {}
        self.parent = None

        # for dfs
        self.color = ''
        # for dijkstra (distance from s)
        self.dist = float('Inf')

    def get_id(self):
        return self._id

    def add_conn(self, v, w=0):
        self.connected[v] = w

    def get_weight(self, v):
        return self.connected[v]

    def get_conn(self):
        return self.connected

    def set_parent(self, p):
        self.parent = p

    def get_parent(self):
        return self.parent

    def set_color(self, w):
        self.color = w

    def get_color(self):
        return self.color

    def set_dist(self, d):
        self.dist = d

    def get_dist(self):
        return self.dist



graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_edge(1, 3, 2)
graph.add_edge(2, 3, 1)
graph.add_edge(1, 2, 3)
print graph.get_vertices()
graph.get_vertex(3).set_parent(1)
print graph.get_vertex(3).get_parent()

graph = Graph()
graph.add_edge(1, 3, 4)
graph.add_edge(3, 7, 2)
graph.add_edge(1, 2, 1)
print graph.get_vertices()
print graph.get_vertex(1).get_weight(2)

graph.add_edge(3, 4, 3)
graph.add_edge(2, 5, 4)
graph.add_edge(2, 3, 1)
print graph.get_vertices()
print graph.get_vertex(1).get_conn()
print graph.get_vertex(2).get_conn()
print graph.get_vertex(7).get_conn()
graph.get_vertex(2).set_parent(1)

print graph.get_vertex(graph.get_vertex(2).get_parent()).get_id() == graph.get_vertex(2).get_parent()

graph.bfs(1)
print ''
graph.dfs()
print ''
graph.dijkstra(1)
