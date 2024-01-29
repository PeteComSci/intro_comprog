# Lists

Lists in Python are like your own collection of favorite things. They can be changed, updated, and modified as you like.

### Crafting Your First List

Creating a list is like packing your backpack - you decide what goes in and what stays out.

Example:
```python
favorite_subjects = ['Math', 'Science', 'History', 'Art']
print(favorite_subjects)
```

---

### Accessing Elements in Your List

Grabbing an item (element) from your list is as easy as picking a book from your shelf. Just remember, we start counting from 0.

Example:
```python
print(favorite_subjects[0]) # Outputs 'Math'
message = f"My favorite subject is {favorite_subjects[2]}."
print(message) # Outputs 'My favorite subject is History.'
```

---

### Tweaking Your List (Multiple Means of Action & Expression)

Feel free to rearrange your list, add new interests, or remove what's no longer a favorite.

#### Modifying Elements

Changing an item in your list is like updating your playlist with new songs.

Example:
```python
favorite_subjects[3] = 'Physical Education'
print(favorite_subjects)
```

---

#### Expanding Your List

Discover a new hobby? Add it to your list using `append()` or `insert()`.

Example:
```python
favorite_subjects.append('Computer Science')
favorite_subjects.insert(2, 'English Literature')
print(favorite_subjects)
```

---

#### Streamlining Your List

Sometimes we outgrow our interests. Remove items easily with `del` or `remove()`.

Example:
```python
del favorite_subjects[1] # Bye Science
favorite_subjects.remove('Math') # See ya Math
print(favorite_subjects)
```

---

## Exercises

Apply your skills in a way that works best for you. Choose an exercise, try it out, and feel free to express your solution in a way that showcases your unique understanding.

---

### Exercise 1: Dream Devices

List the tech gadgets you've been eyeing or heard about lately. Write code that prints out why each gadget is on your wish list. Maybe you love the camera on that new phone or the graphics on the latest gaming console.

---

### Exercise 2: Top Movies Invite

Create a list of activities you want to do this weekend. 
Code a simple program that helps you organize these activities by priority or interest level. Here you can find the [sorting algorithms](https://github.com/PeteComSci/intro_comprog/tree/30f2e5f045dc110e6f597d5e6fbc8d5eac240c95/topics/algorithms/sorting_algorithms).

---

### Exercise 3: Global Explorer

Are you a bookworm? Make a list of books you plan to read. 
Use an [algorithm](https://github.com/PeteComSci/intro_comprog/tree/30f2e5f045dc110e6f597d5e6fbc8d5eac240c95/topics/algorithms/sorting_algorithms) to sort them alphabetically, by genre, or by the author's last name.
