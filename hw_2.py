# Manage student grades.

grades = {}

while True:
    user_input = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ").upper()
    
    # ADD
    if user_input == "A":
        name = input("Student Name: ")
      
        if name in grades:
            print("Sorry, that student is already present.")
        else:
            grade = int(input("Enter the student's grade: "))
            grades[name] = grade

    # REMOVE
    elif user_input == "R":
        name = input("What student do you want to remove? ")
        
        if name in grades:
            grades.pop(name)
        else:
            print("Sorry, that student doesn't exist and couldn't be removed.")

    # MODIFY
    elif user_input == "M":
        name = input("Enter the name of the student to modify: ")
        
        if name in grades:
            print("The old grade is " + str(grades[name]))
            grade = int(input("Enter the student's new grade: "))
            grades[name] = grade
        else:
            print("Sorry, that student doesn't exist and couldn't be modified.")

    # PRINT AVERAGE/ALL
    elif user_input == "P":
        if grades:
            average = sum(grades.values()) / len(grades)
            print("The average grade is " + str(average))
            for name, grade in grades.items():
                print(name + ": " + str(grade))
        else:
            print("No grades to display.")

    # QUIT
    elif user_input == "Q":
        print("Goodbye!")
        break
 
    else:
        print("Sorry, that wasn't a valid choice.")