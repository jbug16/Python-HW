from grade_compute import *

def main():
    # Get user input
    letter_grades = collectGrades()

    # Convert input to numbers
    number_grades = gradeToNumber(letter_grades)

    # Print letter grades entered
    print(f"You entered the grades {letter_grades[0]}, {letter_grades[1]}, {letter_grades[2]}, {letter_grades[3]}")

    # Remove the lowest grade
    new_grades = removeLowestGrade(number_grades)
    
    # Get the average of the new grades
    average = gradeAverage(new_grades)

    # Convert the average to a letter grade
    letter_average = numberToGrade(average)

    # Print the average grade
    print("The average grade is " + str(letter_average))

# Call main function
main()