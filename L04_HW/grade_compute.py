# Collect the grades of student
def collectGrades():
    grades = []

    # Different message for each input
    input_messages = [
        "Enter the first grade or 'Q' to quit: ", 
        "Enter the second grade: ", 
        "Enter the third grade: ", 
        "Enter the fourth grade: "]

    print("Enter letter grades such as A, B-, C+, etc...")

    # Get 4 inputs
    i = 0
    while (i < 4):
        # Get user input
        user_input = input(input_messages[i]).upper()

        # Quit if entered Q
        if user_input == "Q":
            break

        # Add grade to array (grades)
        grades.append(user_input)
        i += 1

    return grades

# Convert grade input to number value
def gradeToNumber(grades):
    number_grade = []
    for grade in grades:
        match grade:
            # A
            case "A+":
                number_grade.append(4.0)
            case "A":
                number_grade.append(3.9)
            case "A-":
                number_grade.append(3.7)

            # B
            case "B+":
                number_grade.append(3.3)
            case "B":
                number_grade.append(3.0)
            case "B-":
                number_grade.append(2.7)

            # C
            case "C+":
                number_grade.append(2.3)
            case "C":
                number_grade.append(2.0)
            case "C-":
                number_grade.append(1.7)

            # D
            case "D+":
                number_grade.append(1.3)
            case "D":
                number_grade.append(1.0)
            case "D-":
                number_grade.append(0.7)

            # F
            case "F":
                number_grade.append(0.0)

    return number_grade

# Remove lowest grade
def removeLowestGrade(grades):
    # Sort grades least to greatest
    grades.sort()

    # Print lowest grade
    print(f"The lowest grade of {grades[0]} will be dropped")

    # Remove first grade (lowest)
    del grades[0]

    return grades

# Get average of grades
def gradeAverage(grades):
    return sum(grades) / len(grades)

# Convert number grade to letter
def numberToGrade(average):
    if (average == 4.0):
        letter_average = "A+"

    return letter_average

letter_grades = collectGrades()
number_grades = gradeToNumber(letter_grades)

print(f"You entered the grades {letter_grades[0]}, {letter_grades[1]}, {letter_grades[2]}, {letter_grades[3]}")

new_grades = removeLowestGrade(number_grades)
average = gradeAverage(new_grades)

print("The average grade is " + str(average))