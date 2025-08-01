# Gradebook Program

def calculate_letter_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def add_student(gradebook):
    name = input("Enter student name: ")
    if name in gradebook:
        print("Student already exists.")
    else:
        gradebook[name] = []
        print(f"{name} added to gradebook.")

def add_grade(gradebook):
    name = input("Enter student name: ")
    if name in gradebook:
        try:
            grade = float(input("Enter grade (0-100): "))
            if 0 <= grade <= 100:
                gradebook[name].append(grade)
                print(f"Grade added for {name}.")
            else:
                print("Invalid grade range.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Student not found.")

def view_student_average(gradebook):
    name = input("Enter student name: ")
    if name in gradebook:
        grades = gradebook[name]
        if grades:
            avg = sum(grades) / len(grades)
            letter = calculate_letter_grade(avg)
            print(f"{name}'s average: {avg:.2f} (Grade: {letter})")
            print(f"Grades: {grades}")
        else:
            print(f"{name} has no grades yet.")
    else:
        print("Student not found.")

def display_class_statistics(gradebook):
    if not gradebook:
        print("Gradebook is empty.")
        return

    total = 0
    count = 0
    highest = ("", 0)
    lowest = ("", 100)

    for student, grades in gradebook.items():
        if grades:
            avg = sum(grades) / len(grades)
            total += avg
            count += 1
            if avg > highest[1]:
                highest = (student, avg)
            if avg < lowest[1]:
                lowest = (student, avg)

    if count > 0:
        class_avg = total / count
        print(f"Class average: {class_avg:.2f}")
        print(f"Highest performing student: {highest[0]} ({highest[1]:.2f})")
        print(f"Lowest performing student: {lowest[0]} ({lowest[1]:.2f})")
    else:
        print("No grades available to calculate statistics.")

def show_menu():
    print("\n===== Gradebook Menu =====")
    print("1. Add new student")
    print("2. Add grade to existing student")
    print("3. View student average and letter grade")
    print("4. Display class statistics")
    print("5. Exit")

def main():
    gradebook = {}

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student(gradebook)
        elif choice == '2':
            add_grade(gradebook)
        elif choice == '3':
            view_student_average(gradebook)
        elif choice == '4':
            display_class_statistics(gradebook)
        elif choice == '5':
            print("Exiting gradebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
