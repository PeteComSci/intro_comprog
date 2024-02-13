# Adpated and extended the file called number_checker.py

def chkEvOd(num):
  if num % 2 == 0:
    print("the number is even")
  else:
    print("the number is odd")


def chkPstNgt(number):
  if number > 0:
    print("your number is positive.")
  elif number < 0:
    print("your number is negative.")
  else:
    print("your number is 0.")


def search(search_grade, stu_grades):
  found = False
  i = 0
  while not found and i < len(stu_grades): # not false=>true, therefore the condition is met
    if search_grade == stu_grades[i]:
      found = True
      print("the search grade is in ", i, " position")
    else:
      i = i + 1

  if found == False:
    print("grade is not found")


def menu(grades):
  print("hello, welcome to my program")
  quit = False
  while not quit:
    user_choice = input("enter 1 to search, \n 2 to check" )
    if user_choice == "1":
      search_grade = int(input("enter a grade to search"))
      search(search_grade, grades)
    elif user_choice == "999":
      quit = True
    else:
      print("invalid")


def main():
  grades=[5,7,6,7,5,7]
  menu(grades)
  # search_grade = int(input("enter a grade to search"))
  # search(search_grade, grades)
  print(grades)
  highest_grade(grades)
  lowest_grades(grades)
  grades.insert(2, 5)
  print(grades)
  grades[3]=0
  print(grades)
  grades.append(7)
  print(grades)
  grades.remove(5)
  print(grades)
  grades_length=len(grades)
  print(grades_length)
  for grade in grades:
    if grade<3:
      print("contact mr.birchnall")
    else:
      print(grade)
  # TODO: Prompt the user to enter an integer and store it in the variable 'number'. number = int(input("enter an integer"))
  
  # TODO: Determine if the number is positive, negative, or zero and print the appropriate message. # Hint: Use comparison operators (>, <, ==) to check if the number is positive, negative, or zero.
  chkPstNgt(number)
  '''if number >0:
  print("your number is positive.")
  elif number<0:
  print("your number is negative.")
  else:
  print("your number is 0.")'''
  # TODO: Check if the number is even or odd and print the message. # Hint: Use the modulo operator (%) to determine if a number is even or odd.
  chkEvOd(number)
  ''' if number %2==0: #== is comparing, while = is giving number%2 the value of 0
  print("the number is even")
  else:
  print("the number is odd")'''
  
  # TODO: Check if the number is divisible by 5 and print the message. # Hint: To check if a number is divisible by 5, the remainder when divided by 5 should be 0.
  if number % 5 == 0:
    print("the number is divisible by 5")
  else:
    print("the humber isn't divisible by 5")
  
  # Advanced Task: If the number is positive and even, check if it is also a multiple of 10.
  # Hint: Combine conditions using 'and'. A number is a multiple of 10 if the remainder when divided by 10 is 0.
  divisor = int(input("enter a second ineger"))
  if number % divisor == 0:
    print(number, "is divisible by", divisor)
  else:
    print(number, "is not divisible by", divisor)
  # if number >0 and number %2==0:
  # number %10==0

def highest_grade(student_grades):
  top_grade=student_grades[0]
  for grade in range(1, len(student_grades)):
    if grade > top_grade:
      top_grade = grade
      print("the highest grade is ",top_grade,".")


def lowest_grades(students_grades):
  least_grade=students_grades[0]
  for grades in range( 1, len(students_grades)):
    if students_grades[grades] < least_grade:
      least_grade = students_grades[grades]
      print("the lowest grade is",least_grade,".")
      '''for index in range(1,len(student_grades)):
      if student_grades[index] >top_grade:
      top_grade=student_grades[index]'''


if __name__ == "__main__":
  main()
