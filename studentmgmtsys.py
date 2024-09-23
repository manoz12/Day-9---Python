student_info = {}
def add_student(name,grades):
    if name in student_info:
        print("Student,{name} already exist. Use update function to update the information")
    else:
        student_info[name]= grades
        print(f"Student {name} has been added successfully.")


def update_student(name,subject,new_grade):
    if name in student_info:
        if subject in student_info[name]:
            student_info[name][subject] = new_grade
            print(f"Updated grade for {subject} for student '{name}' to {new_grade}")
        else:
            print(f"Subject '{subject}' not found for student '{name}'.")
    else:
        print(f"Student {name} does not exist.")
    
    
def remove_student(name):
    if name in student_info:
        del student_info[name]
        print(f"Student: {name} has been removed from the record.")
        
    else:
        print(f"Student '{name} does not exist.")
        
            
def display_student():
    if student_info:
        print("\n----Student Grades-----")
        for name, grades in student_info.items():
            print(f"Student :{name}")
            for subject, grades in student_info.items():
                print(f"{subject}, {grades}")
    else:
        print("No Student Record Found.") 

add_student("Alice", {"Math": 85, "Science": 90})
add_student("Bob", {"Math": 75, "English": 80})
display_student()

update_student("Alice", "Math", 95)
update_student("Bob", "History", 88)  # Subject not found case
remove_student("Bob")
display_student()

remove_student("Charlie")