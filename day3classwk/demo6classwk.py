# List
#   - ordered
#   - indexed
#   - immutable
#   - collection of similar or dissimilar type of data   
#   var_name = (v1, v2, v3, ...)
#   tuple()     --> to convert

def function1():
    t1 = (11, 22, 33, 44, 55)

    print(f"type(t1) = {type(t1)}")
    print(f"len(t1) = {len(t1)}")
    print(f"t1 = {t1}")

    print("Tuple t1 using for loop : ")
    for ele in t1:
        print(ele)

#function1()

def function2():
    t1 = (11, 22, 33, 44, 55)

    print("t1 using indices : ")
    index = 0
    while index < len(t1):
        print(f"t1[{index}] = {t1[index]}")
        index += 1

    print(f"index of 22 = {t1.index(22)}")
    print(f"count of 22 = {t1.count(22)}")
    
#function2()

def function3():
    student = ("abc", 12, 9, 95.0)

    print(f"type(student) = {type(student)}")
    print(f"len(student) = {len(student)}")
    print(f"student = {student}")

    print(f"name = {student[0]}")
    print(f"rollno = {student[1]}")
    print(f"std = {student[2]}")
    print(f"marks = {student[3]}")


function3()

    
