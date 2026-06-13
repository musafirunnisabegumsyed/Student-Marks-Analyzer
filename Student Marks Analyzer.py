# ---------------- FUNCTIONS ----------------

def view(students):
    # Display all students with their marks
    for name, marks in students:
        print("Name:", name, "Marks:", marks)


def search(students):
    # Search student by name
    name = input("Enter student name: ")

    for n, m in students:
        if n.lower() == name.lower():
            print("Found:", n, m)
            return

    print("Student not found")


def studentavg(students):
    # Calculate average marks of a specific student
    name = input("Enter student name: ")

    for n, m in students:
        if n.lower() == name.lower():
            print("Average:", sum(m) / len(m))
            return

    print("Student not found")


def highest(students):
    # Find highest mark of each student
    for n, m in students:
        print("Highest marks of", n, ":", max(m))


def lowest(students):
    # Find lowest mark of each student
    for n, m in students:
        print("Lowest marks of", n, ":", min(m))


def percentage(students):
    # Calculate percentage (average based calculation)
    for n, m in students:
        print("Percentage of", n, ":", sum(m) / len(m), "%")


def topper(students):
    # Find topper using manual sorting based on average marks

    array = []

    for n, m in students:
        array.append([n, sum(m) / len(m)])

    # Sorting in descending order (manual sorting)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i][1] < array[j][1]:
                array[i], array[j] = array[j], array[i]

    print("\n================ LEADERBOARD ================")

    for n, p in array:
        print(n, "->", p, "%")

    print("\nTopper:", array[0][0], "with", array[0][1], "%")


# ---------------- INPUT SECTION ----------------

students = []

# Number of students input
n = int(input("Enter number of students: "))

for i in range(n):

    # Student name input
    name = input("Enter student name: ")

    # Marks input with validation
    while True:
        marks_input = input("Enter marks separated by space: ")

        if marks_input.strip() == "":
            print("Marks cannot be empty")
            continue

        try:
            marks = list(map(int, marks_input.split()))
            break
        except:
            print("Enter valid numbers only")

    students.append((name, marks))


# ---------------- MAIN MENU ----------------

def studentMarksAnalyzer(students):

    # Menu options list
    tobeused = [
        "View All Students",
        "Search Student",
        "Student Average",
        "Highest Mark",
        "Lowest Mark",
        "Find Topper",
        "Percentage",
        "Exit"
    ]

    while True:

        print("\n===================================")

        # Display menu
        for i, item in enumerate(tobeused, start=1):
            print(i, "->", item)

        print("===================================")

        # Safe input handling for menu choice
        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid input")
            continue

        # Menu operations
        if choice == 1:
            view(students)

        elif choice == 2:
            search(students)

        elif choice == 3:
            studentavg(students)

        elif choice == 4:
            highest(students)

        elif choice == 5:
            lowest(students)

        elif choice == 6:
            topper(students)

        elif choice == 7:
            percentage(students)

        elif choice == 8:
            print("Exiting program...")
            break

        else:
            print("Invalid choice")


# ---------------- PROGRAM START ----------------

studentMarksAnalyzer(students)