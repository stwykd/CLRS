class Graph:
    def __init__(self):
        self.Adj={}

    def addVertex(self, key):
        self.Adj[key]={}

    def addEdge(self, u, v, w=0):
        if u not in self.Adj:
            self.Adj[u]={v:w}
        if v not in self.Adj:
            self.Adj[v]={}
        else:
            self.Adj[u].update({v:w})

    def bfs(self, s):
        frontier = self.Adj[s]
        level={s:0}
        parent={s:None}
        next=[]
        i=0
        for v in frontier:
            for u in self.Adj[v]:
                if u not in level:
                    next.append(u)
                    parent[v]=u
                    level[u]=i
            i+=1
            frontier=next
            next=[]

    def dfs(self):
        parent={}
        visited=[]
        for u in self.Adj.keys():
            if u not in visited:
                dfs-visit(self, u)

    def dfs-visit(self, u):
        visited.append(u)
        for v in self.Adj[u]:
            if v not in visited:
                parent[v]=u
                dfs-visit(self, u)

    def dijkstra(self, W, s):

        d[s]=0
        S=[]
        Q=self.Adj.keys()
        while Q!=None:
            u=extract_min(Q)
            S=S.append(u)

            for v in Adj[u]:
                Relax(u,v,w)

if __name__=="__main__":
    g=Graph()
    g.addVertex('S')
    g.addEdge('S','A',5)
    g.addEdge('A','B',1)
    print g.Adj['A']

    g=Graph()
    g.addEdge('A','B')
    g.addEdge('A','C')
    g.addEdge('B','D')
    g.addEdge('D','F')
    g.addEdge('C','D')
    g.addEdge('D','G')
    g.addEdge('C','E')
    g.addEdge('C','G')
    g.addEdge('D','H')
    g.addEdge('F','H')

    print g.Adj.viewvalues()

    g.bfs('A')
