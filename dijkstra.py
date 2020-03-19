def dijkstra(self, W, s):
    d[s]=0
    S=[]
    Q=self.Adj.keys()
    while Q!=None:
        u=extract_min(Q)
        S=S.append(u)
        for v in Adj[u]:
            relax(u,v,w)

def relax(u,v,w):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        parent[v] = u
