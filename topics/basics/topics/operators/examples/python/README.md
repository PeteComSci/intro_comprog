# Examples in Pseudocode and Python

### Objectives ###

- To introduce the concept of dynamic input
- To reinforce basic arithmetic operations in programming
- To be able to apply arithmetic operators to solve real-world problems
- To introduce the concept of exponentiation in programming

---

<details>

<summary>Basic Arithmetic Operations</summary>

Write a program to calculate and print the result of various arithmetic operations between two numbers input by the user.

``` 
Input:
  - Prompt the user to enter the first number (`num1`).
  - Prompt the user to enter the second number (`num2`).
    
Processing and Output:
  - Perform the following arithmetic operations:
  - Addition:
    - Calculate `num1 + num2`.
    - Display the result of the addition.
  - Subtraction:
    - Calculate `num1 - num2`.
    - Display the result of the subtraction.
  - Multiplication:
    - Calculate `num1 * num2`.
    - Display the result of the multiplication.
  - Division:
    - Check if `num2` is not zero.
    - If true, calculate `num1 / num2` and display the result.
    - If false, display an error message for division by zero.
  ```

  <details>
    
  <summary>Python Code</summary>
        
  ```python
  # Basic Arithmetic Operations
       
  # Input: Request two numbers from the user
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))

  # Task: Perform arithmetic operations using the input numbers
  # Addition
  addition = num1 + num2
  print(f"Addition of {num1} and {num2} is {addition}")
        
  # Subtraction
  subtraction = num1 - num2
  print(f"Subtraction of {num2} from {num1} is {subtraction}")
        
  # Multiplication
  multiplication = num1 * num2
  print(f"Multiplication of {num1} and {num2} is {multiplication}")
        
  # Division
  # Note: Include error handling for division by zero
  if num2 != 0:
    division = num1 / num2
    print(f"Division of {num1} by {num2} is {division}")
  else:
    print("Error: Division by zero is not allowed.")
            
  ```
  
  </details>

</details>

---

<details>
  
  <summary>Simple Interest Calculator</summary>
  
  Create a program that calculates simple interest given principal, rate of interest, and time.
  
  ```
  # Pseudocode to calculate simple interest

  # Request the principal, rate of interest, and time from the user
  output "Enter the principal amount: "
  input PRINCIPAL
  output "Enter the rate of interest (as a decimal): "
  input RATE
  output "Enter the time in years: "
  input TIME
  
  # Calculate the simple interest using the formula: Interest = Principal * Rate * Time
  INTEREST = PRINCIPAL * RATE * TIME
  
  # Display the calculated interest
  output "The simple interest is: ", INTEREST

  ```
  
  <details>
    <summary>Python Code</summary>
    
  ```python
  # Simple Interest Calculator
  
  # Step 1: Get input values
  principal = float(input("Enter the principal amount: "))
  rate = float(input("Enter the rate of interest (as a percentage, for example, enter 7 for 7%): ")) / 100
  time = float(input("Enter the time in years: "))
  
  # Step 2: Calculate simple interest
  interest = principal * rate * time
  
  # Print the simple interest formatted to two decimal places
  print(f"The simple interest is: {interest:.2f}")

  ```
  </details>

</details>

---

<details>

<summary>Calculating Area and Perimeter</summary>

  Create a program to calculate the area and perimeter of a rectangle. The length and width of the rectangle should be provided by the user.
  
  ```
  Input:
    - Prompt the user to enter the length of the rectangle (`length`).
    - Prompt the user to enter the width of the rectangle (`width`).
  
  Processing and Output:** 
    - Calculate the area (`length * width`) and display it.
    - Calculate the perimeter (`2 * (length + width)`) and display it.
  ```

  <details>
    
   <summary>Python Code</summary>
   
   ```python
    # Calculating Area and Perimeter of a Rectangle
    
    # Input: Request the length and width of the rectangle from the user
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    # Task: Calculate the area and perimeter
    # Area calculation
    area = length * width
    print(f"The area of the rectangle is {area}")
    
    # Perimeter calculation
    perimeter = 2 * (length + width)
    print(f"The perimeter of the rectangle is {perimeter}")
  ```

  </details>

</details>

---

<details>

<summary>Grocery Shopping Calculator:</summary>

Imagine you're at the grocery store with a shopping list for making your favorite dish. You need to buy two essential ingredients: tomatoes and onions. To manage your budget efficiently, you decide to calculate the total cost for these items before heading to the cashier.

```plaintext
  # Initialize variables
  PRICE_TOMATOES = 0.0
  PRICE_ONIONS = 0.0
  NUMBER_OF_FRIENDS = 0
    
  # Input
  output "Enter the price of tomatoes: "
  input PRICE_TOMATOES
  output "Enter the price of onions: "
  input PRICE_ONIONS
  output "Enter the number of friends sharing the onions: "
  input NUMBER_OF_FRIENDS
    
  # Processing and Output
  # Total Cost Calculation
  TOTAL_COST = PRICE_TOMATOES + PRICE_ONIONS
  output "Total cost for tomatoes and onions is " & TOTAL_COST
    
  # Difference in Cost
  COST_DIFFERENCE = PRICE_TOMATOES - PRICE_ONIONS
  output "Difference in cost between tomatoes and onions is " & COST_DIFFERENCE
    
  # Cost of Buying Multiple Packs
  MULTIPLE_PACKS_COST = PRICE_TOMATOES * 3  # Assuming buying 3 packs of tomatoes
  output "Cost for 3 packs of tomatoes is " & MULTIPLE_PACKS_COST
    
  # Price per Onion if a pack is shared among friends
  IF NUMBER_OF_FRIENDS ≠ 0 THEN
    PRICE_PER_ONION = PRICE_ONIONS / NUMBER_OF_FRIENDS
    output "Price per onion when shared among friends is " & PRICE_PER_ONION
  ELSE
    output "Error: Number of friends cannot be zero for division."
  ENDIF
```

  <details>
  
  <summary>Python Code</summary>
    
  ```python
  # Input:
  price_tomatoes = float(input("Enter the price of tomatoes: "))
  price_onions = float(input("Enter the price of onions: "))
    
  # Processing and Output:
  # Total Cost Calculation:
  total_cost = price_tomatoes + price_onions
  print(f"The total cost for tomatoes and onions is {total_cost}")
    
  # Difference in Cost:
  cost_difference = price_tomatoes - price_onions
  print(f"The difference in cost between tomatoes and onions is {cost_difference}")
    
  # Cost of Buying Multiple Packs:
  multiple_packs_cost = price_tomatoes * 3
  print(f"The cost for 3 packs of tomatoes is {multiple_packs_cost}")
    
  # Price per Onion if a pack is shared among friends:
  number_of_friends = int(input("Enter the number of friends sharing the onions: "))
  if number_of_friends != 0:
    price_per_onion = price_onions / number_of_friends
    print(f"The price per onion when shared among friends is {price_per_onion}")
  else:
    print("Error: Number of friends cannot be zero for division.")
  ```

  </details>
  
</details>

---

<details>

<summary>Experimenting with Exponents</summary>

  Write a program where the user enters a base number and an exponent, and the program calculates the power.
  
  ```
  Input:
    - Prompt the user to enter the base number (`base`).
    - Prompt the user to enter the exponent (`exponent`).
  
  Processing and Output:** 
    - Calculate the power (`base` raised to the `exponent`).
    - Display the result.
  ```

  <details>
   <summary>Python Code</summary>
    
   ```python
   # Calculating Powers
    
   # Input: Request a base number and an exponent from the user
   base = float(input("Enter the base number: "))
   exponent = int(input("Enter the exponent: "))
    
   # Task: Calculate the power
   power = base ** exponent
   print(f"{base} to the power of {exponent} is {power}")
   ```
  </details>
  
</details>

---

<details>
  <summary>Volume Adjustment Program</summary>

  Imagine you're a sound engineer working on a new music track. You need to adjust the volume levels during different segments of the track. You decide to use the concept of exponents to increase or decrease the volume exponentially during certain parts.
  
  ```plaintext
    # Initialize variables
    BASE_VOLUME = 0.0
    VOLUME_EXPONENT = 0
    # Input
    output "Enter the base volume level: "
    input BASE_VOLUME
    output "Enter the exponent to adjust the volume: "
    input VOLUME_EXPONENT
    
    # Processing and Output
    # Volume Adjustment
    ADJUSTED_VOLUME = BASE_VOLUME ^ VOLUME_EXPONENT
    output "The new volume level is " & ADJUSTED_VOLUME
  ```
  
  **In this pseudocode**:
  - We initialize `BASE_VOLUME` and `VOLUME_EXPONENT` to their default values.
  - We prompt the user for input and store the responses in the corresponding variables.
  - We calculate the `ADJUSTED_VOLUME` by raising `BASE_VOLUME` to the power of `VOLUME_EXPONENT` using the '^' symbol for exponentiation.
  - We display the `ADJUSTED_VOLUME` as the new volume level.

  <details>
    <summary>Python Code</summary>
    
  ```python
    # Input:
    base_volume = float(input("Enter the base volume level: "))
    volume_exponent = int(input("Enter the exponent to adjust the volume: "))
    
    # Processing and Output:
    # Volume Adjustment:
    adjusted_volume = base_volume ** volume_exponent
    print(adjusted_volume)

  ```

  </details>

</details>

---

> [!TIP]
> Play with different values, including negative numbers and decimals, to see how Python handles different arithmetic operations.

---

Discuss the importance of each operation in real-world scenarios, such as budget calculations, scientific computations, and statistical analysis.

