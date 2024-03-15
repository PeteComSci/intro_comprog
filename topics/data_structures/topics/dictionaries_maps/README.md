## Dictionaries or Maps (Key-Value Pairs)

Dictionaries or maps are versatile data structures used to store data in key-value pairs. Each key is unique and maps to a value, allowing for efficient data retrieval and manipulation. Let's explore dictionaries/maps and operations such as adding, retrieving, and removing items with examples in both pseudocode and Python.

---

#### Pseudocode Example: Dictionaries/Maps

```plaintext
// Pseudocode: Working with a dictionary/map of student grades

// Create a dictionary/map of student grades
Set studentGrades to {"Alice": 85, "Bob": 92, "Charlie": 78}

// Adding an item
Set studentGrades["Diana"] to 95  // Adds Diana to the dictionary with a grade of 95

// Retrieving an item
Set aliceGrade to studentGrades["Alice"]
Output "Alice's grade:", aliceGrade  // Outputs: Alice's grade: 85

// Removing an item
Remove studentGrades["Charlie"]  // Removes Charlie from the dictionary

// Iterating through the dictionary/map
For each student, grade in studentGrades Do
    Output student, "'s grade: ", grade
End For
```

In this pseudocode:
- The dictionary/map `studentGrades` stores student names as keys and their grades as values.
- New items are added using `Set`.
- Items are retrieved by specifying their key.
- Items are removed using `Remove`.
- A `For` loop is used to iterate through the dictionary/map and output each key-value pair.

---

#### Python Example: Dictionaries

```python
# Python: Working with a dictionary of student grades

# Create a dictionary of student grades
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Adding an item
student_grades["Diana"] = 95  # Adds Diana to the dictionary with a grade of 95

# Retrieving an item
alice_grade = student_grades["Alice"]
print("Alice's grade:", alice_grade)  # Outputs: Alice's grade: 85

# Removing an item
del student_grades["Charlie"]  # Removes Charlie from the dictionary

# Iterating through the dictionary
for student, grade in student_grades.items():
    print(student, "'s grade: ", grade)
```

In this Python code:
- The dictionary `student_grades` stores student names as keys and their grades as values.
- New items are added using `=`.
- Items are retrieved by specifying their key.
- Items are removed using `del`.
- The `.items()` method and a `for` loop are used to iterate through the dictionary and print each key-value pair.

---

These examples demonstrate the utility of dictionaries/maps in storing and managing data in key-value pairs. They provide an efficient way to access, add, and remove data, making them an excellent choice for various use-cases where quick data retrieval and structured storage are required.

---

# Python Dictionaries with Marvel Movies Example

Below, you will learn how to add, edit, delete, and search for items in dictionaries, along with more advanced operations like sorting and grouping.

## Starting Point: The Marvel Movies Dictionary

Let's begin with our initial dictionary of Marvel movies:

```python
marvel_movies = {
    "Captain America: The First Avenger": {"Release Year": 2011, "Movie Timeline": "1940s"},
    "Captain Marvel": {"Release Year": 2019, "Movie Timeline": "1995"},
    "Iron Man": {"Release Year": 2008, "Movie Timeline": "2010"},
    "Iron Man 2": {"Release Year": 2010, "Movie Timeline": "2011"},
    "The Incredible Hulk": {"Release Year": 2008, "Movie Timeline": "Post-Iron Man events"}
}
```

<details>
<summary><b>Basic Operations on Dictionaries</b></summary>

### Adding a New Movie

Add a new entry to the dictionary:

```python
def add_movie(movies_dict, movie_name, release_year, timeline):
    movies_dict[movie_name] = {"Release Year": release_year, "Movie Timeline": timeline}
```

### Editing an Existing Movie

Modify the details of an existing movie:

```python
def edit_movie(movies_dict, movie_name, release_year=None, timeline=None):
    if movie_name in movies_dict:
        if release_year:
            movies_dict[movie_name]["Release Year"] = release_year
        if timeline:
            movies_dict[movie_name]["Movie Timeline"] = timeline
```

### Deleting a Movie

Remove a movie from the dictionary:

```python
def delete_movie(movies_dict, movie_name):
    if movie_name in movies_dict:
        del movies_dict[movie_name]
        print(f"{movie_name} was successfully deleted.")
```

### Searching for a Movie

Check if a movie is in the dictionary:

```python
def search_movie(movies_dict, movie_name):
    return movie_name in movies_dict
```

</details>

<details>
<summary><b>Advanced Dictionary Operations</b></summary>

### Searching in Inner Dictionaries

Search for movies based on inner dictionary values:

```python
def search_in_details(movies_dict, key, value):
    for movie, details in movies_dict.items():
        if details.get(key) == value:
            print(f"{movie}: {details}")
```

### Printing Movies in a Range of Years

Display movies released within a specific range of years:

```python
def print_movies_in_range(movies_dict, start_year, end_year):
    for movie, details in movies_dict.items():
        if start_year <= details["Release Year"] <= end_year:
            print(f"{movie}: {details}")
```

### Grouping Movies by a Theme

Organize movies based on a common theme:

```python
def group_movies_by_theme(movies_dict, theme_key):
    theme_groups = {}
    for movie, details in movies_dict.items():
        theme = details.get(theme_key)
        if theme:
            if theme not in theme_groups:
                theme_groups[theme] = [movie]
            else:
                theme_groups[theme].append(movie)
    for theme, movies in theme_groups.items():
        print(f"\n{theme}:")
        for movie in movies:
            print(f"- {movie}")
```

</details>

<details>
<summary><b>Explanation of Key Concepts</b></summary>

### The `.get()` Method

Retrieve a value from a dictionary safely, without raising an error if the key doesn't exist:

- **Usage**: `dictionary.get(key, default=None)`

### Conditional Range Check

Efficiently check if a value falls within a specified range:

- **Example**: `if start_year <= details["Release Year"] <= end_year:`

### List Appending Method

Add an item to the end of a list associated with a dictionary key:

- **Usage**: `list.append(item)`

</details>

<details>
<summary><b>Practical Applications and Exercises</b></summary>

- **Add a New Marvel Movie**: Using the `add_movie` function, add "Thor" with a release year of 2011 and a timeline of "2011".
- **Edit a Movie Detail**: Change the movie timeline of "Iron Man" to "2008" using the `edit_movie` function.
- **Delete a Movie**: Remove "The Incredible Hulk" from the dictionary.
- **Search for a Movie by Year**: Utilize `search_in_details` to find all movies released in 2008.
- **Print Movies Released Between 2008 and 2011**: Use `print_movies_in_range` to display all such movies.
- **Group Movies by Timeline**: Organize movies by their "Movie Timeline" using `group_movies_by_theme`.

</details>

This markdown document serves as a comprehensive guide to using Python dictionaries, demonstrated through engaging examples and practical exercises. It's designed to encourage interactive learning and exploration of Python's powerful capabilities for managing and manipulating data.
