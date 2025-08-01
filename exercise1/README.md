# 📘 Gradebook Management System

A simple command-line Python application to manage student grades, compute averages, assign letter grades, and display class statistics.

---

## ✅ Features

* Store student data in a dictionary: `{ "Student Name": [grades] }`
* Menu-driven interface with 5 options:

  1. Add new student
  2. Add grade to existing student
  3. View student average and letter grade
  4. Display class statistics
  5. Exit
* Calculates **letter grades**:

  * A: 90–100
  * B: 80–89
  * C: 70–79
  * D: 60–69
  * F: Below 60
* Class statistics include:

  * Class average
  * Highest performing student
  * Lowest performing student

---

## 🛠️ Key Concepts Demonstrated

* **Dictionaries** and **Lists**
* **Functions** and **Loops**
* **Conditional logic**
* **Menu-based navigation**
* **Basic statistical calculations**

---

## 🚀 Getting Started

### Prerequisites

* Python 3 installed on your system.

### Running the Program

1. Clone or download this repository.
2. Open a terminal and navigate to the project folder.
3. Run the script:

```bash
python gradebook.py
```

---

## 🧪 Example Use Case

```text
===== Gradebook Menu =====
1. Add new student
2. Add grade to existing student
3. View student average and letter grade
4. Display class statistics
5. Exit
Enter your choice (1-5): 1
Enter student name: John
John added to gradebook.

Enter your choice (1-5): 2
Enter student name: John
Enter grade (0-100): 85
Grade added for John.

Enter your choice (1-5): 3
Enter student name: John
John's average: 85.00 (Grade:B)
Grades: [85]
```

---

## 🧠 Suggestions for Enhancement

* Add file saving and loading functionality (e.g., using JSON or CSV)
* Input validation for duplicate students
* Support deleting or editing students/grades
* GUI version using Tkinter or a web framework

---

## 📄 License

This project is free to use under the **MIT License**.
