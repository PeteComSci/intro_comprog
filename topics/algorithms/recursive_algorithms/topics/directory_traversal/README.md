Directory Traversal is a tangible example of recursion that's applicable in real-world scenarios, especially in file management, where directories can have multiple layers of nested subdirectories.

### Directory Traversal
```plaintext
function directoryTraversal(path)
    // Base case: If path is a file, print its name
    if isFile(path)
        print "File:", path
        return

    // If path is a directory, print its name
    if isDirectory(path)
        print "Directory:", path
        
        // Get list of files and directories in current directory
        fileList = getFiles(path)
        dirList = getDirectories(path)

        // Recursive case: Traverse each directory
        for dir in dirList
            directoryTraversal(dir)
        
        // Process each file
        for file in fileList
            print "File:", file
```
**Explanation:**
- **Base Case (`if isFile(path)`)**: If the path is a file, display the file's name. This is the simplest case where no further traversal is necessary.
- **Process Current Directory (`if isDirectory(path)`)**: If the path is a directory, display its name and retrieve the list of files and subdirectories it contains using `getFiles(path)` and `getDirectories(path)`.
- **Recursive Case (Directories)**:
  - **`for dir in dirList`**: Iterate through each subdirectory.
  - **`directoryTraversal(dir)`**: Recursively call `directoryTraversal` for each subdirectory. This will explore each branch of the directory tree fully before returning.
- **Process Files**:
  - **`for file in fileList`**: After all subdirectories have been fully explored, process (e.g., display) the files in the current directory.

