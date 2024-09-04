grades = []
input_messages = ["Enter the first grade or 'Q' to quit: ", "Enter the second grade: ", "Enter the third grade: ", "Enter the fourth grade: "]
i = 0

print("Enter letter grades such as A, B-, C+, etc...")

while (i < 4):
    # Get user input
    user_input = input(input_messages[i]).upper()

    # Quit if entered Q
    if user_input == "Q":
        break

    grades[i] = user_input
    i += 1

# PRINT AVERAGE/ALL
# average = sum(grades.values()) / len(grades)
# print("The average grade is " + str(average))