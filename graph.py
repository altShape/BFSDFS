"""CSC 225 - Graph search starter code. Finish the TODO sections."""
from collections import deque


class Graph:
    def __init__(self):
        # A dictionary: vertex -> list of neighbors
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        self.add_vertex(v)
        self.add_vertex(u)
        if v not in self.adj[u]:
            self.adj[u].append(v)

        if u not in self.adj[v]:
            self.adj[v].append(u)
        # Assume u != v. The graph is undirected.
        


    def dfs(self, start):
        """Return a DFS visitation list starting at start."""
        visited = set()
        order = []
        def visit(v):
            visited.add(v)
            order.append(v)
            for neighbor in self.adj[v]:
                if neighbor not in visited:
                    visit(neighbor)
        visit(start)
        return order
        # Assume start exists in self.adj.
        

    def bfs(self, start):
        """Return a BFS visitation list starting at start."""
        visited = set()
        order = []
        queue = deque()
        queue.append(start)
        visited.add(start)
        while queue:
            v = queue.popleft()
            order.append(v)
            for neighbor in self.adj[v]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order
        # Assume start exists in self.adj.
        

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('A', 'B')
print(g.adj)