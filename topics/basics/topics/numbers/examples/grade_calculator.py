# Grade Calculator

def main():
    greeting()
    # TODO: Prompt the user for the average assignment score and convert it to a float
    # assignments_score = 0  # Placeholder, replace with actual input and conversion
    assignments_score = float(input("Enter the average assignment score from 0-100: "))

    # TODO: Prompt the user for the average tests score and convert it to a float
    # tests_score = 0  # Placeholder, replace with actual input and conversion
    tests_score = float(input("Enter the average tests score from 0-100: "))

    # TODO: Prompt the user for the class participation score and convert it to a float
    # participation_score = 0  # Placeholder, replace with actual input and conversion
    participation_score = float(input("Enter the class participation score from 0-100: "))

    # TODO: Calculate the final grade based on the weights: Assignments (40%), Tests (40%), Participation (20%)
    # final_grade = 0  # Placeholder, replace with the calculation logic
    final_grade = assignments_score * 0.4 + tests_score * 0.4 + participation_score * 0.2

    # Display the final grade
    print(f"Your final grade is: {final_grade}")


def greeting():
    message = input("Enter your name: ")
    print(f"Hello {message}")


if __name__ == "__main__":
    main()