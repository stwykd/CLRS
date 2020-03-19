import collections, sys

def bfs(s, g):
    level = {s:0}
    parent = {s:None}
    i=1
    frontier=[s]
    while frontier:
        next=[]
        for u in frontier:
            for v in g[u]:
                if v not in level:
                    level[i]=v
                    parent[u]=v
                    next.append(u)
                print next
                frontier=next
                i+=1
    for node in g:
        if node in level:
            sys.stdout.write(str(level[node]*6)+" ")
        else:
            sys.stdout.write(str(-1)+" ")

# Takes the number of test cases
for _ in range(input()):
    # taking N, number of nodes, and M number of edges
    N, M = map(int, raw_input().split())
    graph = collections.defaultdict(list)
    for i in range(M):
        # Nodes between which the edge exists
        u, v = map(int, raw_input().split())
        if u not in graph:
            graph[u]=[v]
        else:
            graph[u].append(v)
        if v not in graph:
            graph[v]=[u]
        else:
            graph[v].append(u)
    s = input()
    bfs(s, graph)
