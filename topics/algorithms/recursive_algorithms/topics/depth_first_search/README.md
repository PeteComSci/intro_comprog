DFS is particularly useful for scenarios where we want to explore all possibilities, find connected components, check for connectivity, or traverse trees and graphs in a way that exhaustively explores one branch before moving to another.

### Depth-First Search (DFS)
```plaintext
function DFS(node, visited)
    // Mark the current node as visited and print it
    visited[node] = true
    print node

    // Recur for all the vertices adjacent to this vertex
    for each vertex in adjacent(node)
        if not visited[vertex]
            DFS(vertex, visited)
```
**Explanation:**
- **Marking as Visited (`visited[node] = true`)**: When a node is visited, it's marked to avoid revisiting and to prevent cycles.
- **Printing the Node (`print node`)**: This is often a placeholder for other operations you might want to perform on the node.
- **Recursion (`for each vertex in adjacent(node)`)**: DFS explores as far as possible along each branch before backtracking. It uses a recursive approach to visit all nodes reachable from the given node by exploring each branch to its fullest before backtracking.

