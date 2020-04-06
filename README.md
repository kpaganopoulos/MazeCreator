# MazeCreator

##Maze Creator 

A python script that creates maze, implementing Depth-First Algorithm. The output maze is organized like a graph. The result is saved to a text file with the following format:

(5, 2), (6, 2)
(6, 2), (6, 3)
(6, 3), (7, 3)

Depth-first Search

Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. One starts at the root (selecting some arbitrary node as the root in the case of a graph) and explores as far as possible along each branch before backtracking.

example of DFS

DFS in Pseudocode

procedure DFS(G,v):
1) label v as discovered
2) for all edges from v to w in G.adjacentEdges(v) do
3) if vertex w is not labeled as discovered then
4) recursively call DFS(G,w)
