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
    print(f"The lowest grade of {numberToGrade(grades[0])} will be dropped")

    # Remove first grade (lowest)
    del grades[0]

    return grades

# Get average of grades
def gradeAverage(grades):
    return sum(grades) / len(grades)

# Convert number grade to letter
def numberToGrade(grade):
    if grade >= 4.0:
        letter = "A+"
    elif grade >= 3.7:
        letter = "A"
    elif grade >= 3.3:
        letter = "A-"
    elif grade >= 3.0:
        letter = "B+"
    elif grade >= 2.7:
        letter = "B"
    elif grade >= 2.3:
        letter = "B-"
    elif grade >= 2.0:
        letter = "C+"
    elif grade >= 1.7:
        letter = "C"
    elif grade >= 1.3:
        letter = "C-"
    elif grade >= 1.0:
        letter = "D"
    else:
        letter = "F"

    return letter