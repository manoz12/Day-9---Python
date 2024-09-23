# Initialize the dictionary to store student information
students_grades = {}

# Function to add a student with their grades
def add_student(name, grades):
    if name in students_grades:
        print(f"Student '{name}' already exists. Use update option to update the grades.")
    else:
        students_grades[name] = grades
        print(f"Student '{name}' added successfully.")

# Function to update grades for a particular student
def update_grades(name, subject, new_grade):
    if name in students_grades:
        students_grades[name][subject] = new_grade
        print(f"Updated {subject} grade for {name} to {new_grade}.")
    else:
        print(f"Student '{name}' does not exist.")

# Function to remove a student's grade in a subject
def remove_grade(name, subject):
    if name in students_grades:
        if subject in students_grades[name]:
            del students_grades[name][subject]
            print(f"Removed {subject} grade for {name}.")
        else:
            print(f"{subject} does not exist for {name}.")
    else:
        print(f"Student '{name}' does not exist.")

# Function to display all students and their grades
def display_students():
    if students_grades:
        for name, grades in students_grades.items():
            print(f"Student: {name}, Grades: {grades}")
    else:
        print("No student records available.")

# Adding some students and their grades
add_student("Alice", {"Math": 85, "English": 78, "Science": 90})
add_student("Bob", {"Math": 75, "English": 65, "Science": 80})

# Display students and their grades
display_students()

# Updating grades for a student
update_grades("Alice", "Math", 95)

# Removing a subject grade for a student
remove_grade("Bob", "Science")

# Displaying the final list of students and their grades
display_students()

# Trying to update and remove for a non-existent student
update_grades("Charlie", "Math", 88)
remove_grade("Charlie", "English")

