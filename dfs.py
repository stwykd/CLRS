parent={s: None}
def dfsvisit(s, g):
    for v in g[s]:
        if v not in parent:
            parent[v]=s
            dfsvisit(v, g)
def dfs(V, g):
    for s in V:
        if s not in parent:
            parent[s] = None
            dfsvisit(s, g)
