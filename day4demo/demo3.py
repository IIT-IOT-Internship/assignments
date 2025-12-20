# List of dict

def function1():
    students = [
        {'rollno':12, 'name':"nikhil", 'marks':98.5},
        {'rollno':10, 'name':"siddhi", 'marks':87.6},
        {'rollno':13, 'name':"sejal", 'marks':90.0}
    ]

    #print(students)
    
    #for student in students:
    #    print(student)

    for student in students:
        print(f"rollno = {student['rollno']}, name = {student['name']}, marks = {student['marks']}")

function1()
