The Tower of Hanoi problem showcases the elegance of recursive solutions in breaking down a problem into smaller, more manageable sub-problems.

### Tower of Hanoi
```plaintext
function moveDisk(disk, source, destination, auxiliary)
    // Base case: only one disk to move
    if disk == 1
        print "Move disk 1 from pole", source, "to pole", destination
        return

    // Move top n-1 disks from source to auxiliary, using destination as a temporary pole
    moveDisk(disk - 1, source, auxiliary, destination)

    // Move the remaining disk from source to destination
    print "Move disk", disk, "from pole", source, "to pole", destination

    // Move the n-1 disks from auxiliary to destination, using source as a temporary pole
    moveDisk(disk - 1, auxiliary, destination, source)
```
**Explanation:**
- **Base Case (`if disk == 1`)**: If there's only one disk, it can be moved directly from the source pole to the destination pole. This is the simplest case and provides a stopping point for the recursion.
- **Recursive Case**:
  - **First Recursive Call (`moveDisk(disk - 1, source, auxiliary, destination)`)**: Move the top `n-1` disks from the source pole to the auxiliary pole, using the destination pole as a temporary holding area. This step clears the way for moving the largest disk.
  - **Move the largest disk (`print "Move disk", disk, ...`)**: After moving the smaller disks out of the way, move the largest disk from the source pole to the destination pole.
  - **Second Recursive Call (`moveDisk(disk - 1, auxiliary, destination, source)`)**: Move the `n-1` disks from the auxiliary pole to the destination pole, completing the puzzle.

