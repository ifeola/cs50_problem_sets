# Student Result Management System

#### Video Demo: [Link to project video](https://youtu.be/oxrpYGSl4cc)

#### Description

The Student Result Management System is a terminal-based Python application designed to help teachers manage student academic records. It allows users to add students, enter scores, calculate total score and average score for each student, assign grades based on the average score, and store results in a file "db.csv" for later use.

#### Features

- Add new student's name, id and level
- Add new students with unique student IDs
- Enter student scores
- Validate user input and handle errors gracefully
- Automatically calculate total score, average score, and grade
- View formatted student results in the terminal
- Save and load student data using a CSV file

#### How to Run

1. Ensure Python 3.10 or later is installed.
2. Download or clone the repository.
3. Navigate to the project directory.
4. Run the program using:
   python project.py

#### Files

- project.py – All application logics are here
- requirement.txt - pip-installable libraries that my project requires
- test_project.py - tests three of my custom functions in project.py
- db.csv – Persistent storage for student records
- README.md – Project documentation

#### Code Functionality Overview

The program defines a Student class to represent each student and encapsulate all student-related data and behavior. The class stores the student’s name, ID, academic level, and subject scores. It provides methods to add grades, compute the total score, calculate the average score, and determine the final letter grade based on predefined grading thresholds.

Input validation is handled using helper functions. The is_name_valid function ensures that a student’s name consists of exactly two alphabetic words. The is_student_id_valid function checks that a student ID is exactly six alphanumeric characters. To prevent duplicate records, the is_new function checks whether a given student ID already exists in the CSV database.

The get_student_details function collects and validates all required student information before creating and returning a Student object. The get_student_scores function prompts the user to enter scores for each subject, validates that scores are numeric and within the range of 0 to 100, and stores them in the student object.

Persistent storage is handled by the store_student function, which writes the student’s personal details, subject scores, total score, average score, and final grade to db.csv using Python’s CSV module. The result_template function generates a formatted result sheet as a multi-line string for display in the terminal.

The main function controls the overall program flow by collecting student data, processing scores, saving records, and displaying the final result. The program executes through this function when run directly.

#### Design Choices

A Student class was used to encapsulate student data and related behavior, improving code organization. CSV was selected for data storage because it is simple, readable, and suitable for structured records. The program was divided into functions to improve modularity and maintainability.

#### Limitations and Future Improvements

- The program currently supports a limited grading structure.
- Future improvements may include support for multiple subjects and a graphical user interface.

#### Academic Honesty

This project was completed as part of CS50’s Introduction to Programming with Python. All code is original unless otherwise stated.
