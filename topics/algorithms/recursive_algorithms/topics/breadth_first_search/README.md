BFS is particularly useful for finding the shortest path on unweighted graphs, level order traversal of trees, or traversing graphs level by level.

### Breadth-First Search (BFS)
```plaintext
function BFS(startNode)
    // Create a queue for BFS and enqueue the start node
    queue = empty queue
    enqueue(queue, startNode)
    visited[startNode] = true

    // Loop to visit each node in the queue
    while not isEmpty(queue)
        // Dequeue a vertex from the queue and print it
        node = dequeue(queue)
        print node

        // Get all adjacent vertices of the dequeued node
        // If an adjacent vertex has not been visited, mark it visited and enqueue it
        for each vertex in adjacent(node)
            if not visited[vertex]
                visited[vertex] = true
                enqueue(queue, vertex)
```
**Explanation:**
- **Queue Initialization (`queue = empty queue`)**: BFS uses a queue to keep track of the nodes to visit next.
- **Enqueue Start Node**: The starting node is added to the queue and marked as visited.
- **Processing Nodes (`while not isEmpty(queue)`)**: Nodes are dequeued one by one, and their adjacent nodes are explored.
- **Exploring Adjacent Nodes (`for each vertex in adjacent(node)`)**: For each dequeued node, all unvisited adjacent nodes are enqueued and marked as visited.
