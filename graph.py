# Couple Ideas:
# I could have an subclass unweighted or weighted graph 
# Or I could just have a weighted graph with 1 as a weight

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = set()
        self.adjency_list = dict() # I actualy want a dict instead of list, edges could be chars

    def __str__(self):
        vertex_string = "Vertices: " + str(self.vertices)
        edge_string = "Edges: " + str(self.edges)
        return f"{vertex_string}\n{edge_string}"

    def set_vertices(self, set_of_vertices):
        self.vertices = set_of_vertices

    def set_edges(self, set_of_edges):
        self.edges = set_of_edges

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def add_edge(self, edge):
        self.edges.add(edge)

    def are_neighboors(self, vertex1, vertex2):
        return (vertex1, vertex2) in self.edges or (vertex2, vertex1) in self.edges

class GraphTraversal:
    def __init__(self, graph):
        self.graph = graph

# The problem with the recursive approach is where does the marked 
# From reducible dfs
# marked = [False] * G.size()
# def dfs(G, v):
#     visit(v)
#     marked[v] = True
#     for w in G.neighbors(v):
#         if not marked[w]:
#             dfs(G, w)
# marked = [False] * G.size()
# def dfs_iter(G, v):
#     stack = [v]
#     while len(stack) > 0:
#         v = stack.pop()
#         if not marked[v]:
#         visit(v)
#         marked[v] = True
#         for w in G.neighbors(v):
#             if not marked[w]:
#                 stack.append(w)

# From MIT F6.006 Introduction to Algorithms, Fall 2011 13. Breadth-First Search (BFS)
# BFS(s, Adj):
#     level = {s : 0}
#     parent = {s: None}
#     i = 1
#     frontier = [s]
#     while frontier:
#         next = []
#         for u in frontier:
#             for v in Adj[u]:
#                 if v not in level:
#                     level[v] = i
#                     parent[v] = u
#                     next.append(v)
#         frontier = next
#         i+= 1 

