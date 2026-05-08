print('\nHi! Welcome to the student grading system.')
print("Please read each instructions carefully before moving to next step.")
print("Invalid iput can end the program and you need to start again from the beginning.")

student_grade_dict = {}

while True:
    student = input('\nPlease enter student name: ')
    grade = input("Please enter student's grade: ")
    student_grade_dict[student] = grade
    print("Thank you for entering the details. Current data in the dictionary is:")
    print(student_grade_dict)
    
    print("\nDo you want to add another student in the dictionary?")
    another_student = input("Please enter  [y/n] : ").lower()

    if another_student not in ('y','yes'):
        break

print("\nCurrent data in the dictionary:")
print(student_grade_dict)
print("\nDo you want to update any existing student's grade in the dictonary?")
update_grade = input("Please enter  [y/n] : ").lower()

while update_grade in ('y','yes'):
    student = input("\nPlease enter existing student's name: ")
    if (student in student_grade_dict):
        grade = input("Please enter new grade for the student: ")
        student_grade_dict[student] = grade

        print("\nUpdated data in the dictionary : ")
        print(student_grade_dict)

    else:
        print("\nSorry! Student does not exist. Please enter valid name next time!")
        print("Current data in the dictionary:")
        print(student_grade_dict)

    print("\nDo you want to update any another student's grade in the dictonary?")
    update_grade = input("Please enter  [y/n] : ").lower()

print("\nThank you for entering the details. Final data in the dictionary is:")
print(student_grade_dict)