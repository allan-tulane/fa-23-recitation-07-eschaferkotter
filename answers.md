# CMPS 2200 Recitation 10## Answers

**Name:**Ethan Schaferkotter


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
The work of reachable is O(n+m), assuming n nodes and m edges that may connect to two nodes.

- **4)**
The worst case for calling reachable would be 1 time because if the connection is not present from the start node, then it is not reachable

- **5)**
The work of connected is related to the work of reachable so it's O(n+m)

- **7)**
With an adjacency matrix, the work would be O(n^2) because every potential edge needs to be checked, therefore O(n*n) = O(n^2)