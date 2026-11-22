# CSC 225 — Graph Search: BFS and DFS

**Name: Keith McGregor 

This assignment introduces graph representation and two ways to search a graph: depth-first search (DFS) and breadth-first search (BFS).

## How to complete and submit

1. Open the instructor's GitHub repository and click **Fork** to create a copy in your own GitHub account.
2. **Clone your fork** to your computer (or use GitHub Codespaces if your instructor permits it).
3. Open the project in VS Code. Complete the `TODO` sections in `graph.py`. Leave the provided test cases unchanged.
4. Answer the questions **in this README.md file**, replacing each `YOUR ANSWER HERE` with your response. Use your own words.
5. Run `python main.py` and `python test_graphs.py`. Fix any issues and rerun the tests.
6. Commit and push your changes to **your fork** on GitHub. Verify that both your Python code and README answers appear online.
7. Submit **the URL of your forked GitHub repository** to the assignment on **Blackboard**. Do not submit only a link to the original instructor repository.

> The repository you submit must contain your completed `graph.py` and answered `README.md`. No PDF or separate written worksheet is required. You do not need to open a pull request.

## What you will build

We will work with an **undirected, unweighted graph** stored as an **adjacency list**. Each vertex is a dictionary key, and its neighbors are stored in a list. The graph may contain cycles or disconnected components.

Example:

```python
{
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
```

For consistent traversal results, **visit neighbors in the order they appear in each list**. Do not sort them.

### Part 1 — Build the graph

Open `graph.py`. Implement:

- `add_vertex(v)`: Create an empty neighbor list for a new vertex; do nothing if it already exists.
- `add_edge(u, v)`: Add both endpoints if needed, then add the undirected connection (`u` to `v` and `v` to `u`). Avoid duplicate neighbors. You may assume `u != v`.

**Guidance:** First check `if v not in self.adj`. Then store a list with `self.adj[v] = []`. For an undirected edge, each endpoint belongs in the other's list.

**Question 1.** Why does adding an undirected edge require updating two adjacency lists?

Because if I added an undirected edge just from A:B that just says I can go from a to be and not that I can go from B to A, and when using undirected edges they can go both ways no just to one vertex.

**Question 2.** What is one advantage of an adjacency list over an adjacency matrix for a graph with relatively few edges?

When you use a adj list it only stores the edges that are actually used and only takes up V+E while a matrix makes a table which is  V times V even if most of the edges are never used.

### Part 2 — Depth-first search (DFS)

Implement `dfs(start)` in `graph.py` using **recursion**. Return a list of vertices in the order they are first visited. You may assume `start` is already in the graph.

Suggested approach:

1. Create an empty `visited` set and an empty `order` list.
2. Define a stack inside `dfs` that accepts a vertex.
3. Mark the vertex visited and append it to `order`.
4. Loop the steps while the stack is non-empty:for each neighbor of that vertex, call the helper if that neighbor has not been visited.


**Question 3.** What prevents DFS from visiting vertices forever when a graph contains a cycle?

The visited set keeps a track of all the visited vertices, and once you get to a vertex it checks it's unvisited neighbors, and if one of them is in that visisted set then it skips that one.

**Question 4.** Starting at `A` in Graph 1 below, write the DFS visit order. Explain where DFS first needs to backtrack.

Visit order: A,B,D,E,F,C   | It first has to backtrack at F because F has no unvisited neighbors

### Part 3 — Breadth-first search (BFS)

Implement `bfs(start)` in `graph.py` using a **queue** (`collections.deque` is already imported). Return a list of vertices in the order they are removed from the queue. You may assume `start` exists.

Suggested approach:

1. Create `visited`, `order`, and an empty `deque`.
2. Add `start` to the queue and immediately mark it visited.
3. While the queue contains vertices, remove its first vertex with `popleft()` and append it to `order`.
4. Add unvisited neighbors to the back of the queue and mark them visited **when they are added**.
5. Return `order`.

**Question 5.** Why should BFS mark a neighbor visited when it is **enqueued**, rather than waiting until it is removed from the queue?

Because if you waited t mark it as visited then you could accidenlty add the same vertext twice, which woudl make a duplicate

**Question 6.** Starting at `A` in Graph 1, write the BFS visit order and list the queue contents immediately after processing `A` and immediately after processing `B`.

visit order: A,B,C,D,E,F After processing A: queue has [B,C], Processing B: queue has [C,D]

### Part 4 — Test your code

Run these commands in the project folder:

```bash
python main.py
python test_graphs.py
```

On some computers, use `python3` instead of `python`.

`main.py` builds these graphs, and `test_graphs.py` checks the results. The expected orders assume neighbors are stored in the order the edges were added.

**Graph 1** (branching graph with a cycle):

```text
A--B   A--C   B--D   B--E   C--F   E--F
```

**Graph 2** (diamond):

```text
0--1   0--2   1--3   2--3
```

**Graph 3** (disconnected; `Z` is isolated):

```text
A--B   B--C   X--Y   Z
```

| Test | Start | Expected DFS | Expected BFS |
|---|---|---|---|
| Graph 1 | `A` | `A, B, D, E, F, C` | `A, B, C, D, E, F` |
| Graph 2 | `0` | `0, 1, 3, 2` | `0, 1, 2, 3` |
| Graph 3 | `A` | `A, B, C` | `A, B, C` |
| Graph 3 | `Z` | `Z` | `Z` |

Tests also check neighbor lists and duplicate-edge handling. **Do not modify `test_graphs.py` to make the tests pass.**

**Question 7.** Why do searches starting at `A` in Graph 3 not visit `X`, `Y`, or `Z`?

Because graph 3 is disconnected to the A_B_C doesnt have any edges to connect to X, Y or Z

**Question 8.** Suppose every edge has the same cost. Which search is useful for finding a path with the fewest edges from a starting vertex: DFS or BFS? Why?

BFS would be better because it goes through each vertext by level, so the first time it hits a vertext that would be the cheapest or less expensive path there.

**Question 9.** After your program works, describe one difference between the orders produced by DFS and BFS on Graph 1.

DFS goes deep before going wide, and BFS goes wide before going deep

### Part 5 — Optional visualization (not graded)

Run:

```bash
python visualize.py
```

This writes `example_graph.dot` using only standard Python. If you have the separate **Graphviz** application installed, you can render it with:

```bash
dot -Tpng example_graph.dot -o example_graph.png
```

Graphviz is **not required** for grading. Do not spend time installing it until BFS and DFS work.

## Files

| File | Purpose |
|---|---|
| `graph.py` | **Edit this:** implement the graph and searches |
| `README.md` | **Edit this:** answer Questions 1–9 |
| `main.py` | Provided examples; run to see results |
| `test_graphs.py` | Provided checks; do not modify |
| `visualize.py` | Optional DOT export |
| `.gitignore` | Excludes generated files |

## Final submission checklist

- [ ] All `TODO` methods in `graph.py` are complete.
- [ ] `python test_graphs.py` reports `All tests passed!`.
- [ ] Questions 1–9 are answered in this `README.md`.
- [ ] My changes are committed and pushed to **my fork**.
- [ ] I submitted the URL of **my fork** in Blackboard.

---

*Source acknowledgment: Graph search topics adapted from the instructor-provided Chapter 22 lecture slides, © 2022 Pearson Education, Inc. The programming prompts, examples, and code structure are prepared for this assignment.*
