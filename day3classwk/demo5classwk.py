# List
#   - ordered
#   - indexed
#   - mutable
#   - collection of similar or dissimilar type of data   
#   var_name = [v1, v2, v3, ...]
#   var_name = [] or list()     --> empty list

def function1():
    l1 = [11, 22, 33, 44, 55]

    print(f"type(l1) = {type(l1)}")
    print(f"len(l1) = {len(l1)}")
    print(f"l1 = {l1}")

    print("l1 using for :", end=" ")
    for element in l1:
        print(element, end=" ")
    print("")

#function1()

def function2():
    l1 = [11, 22, 33, 44, 55]

    print("List l1 using indices :")
    index=0
    while index < len(l1):
        print(f"l1[{index}] = {l1[index]}")
        index += 1

    print(f"index of 33 = {l1.index(33)}")
    
#function2()

def function3():
    l1 = [11, 22, 33, 44, 55]

    print(f"Before : len = {len(l1)} : l1 = {l1}")

    #l1.append(100)      # value is added at the last
    #l1.insert(3, 100)    # value is added at given index
    #l1.insert(10, 100)      # value is added at the last due to invalid index

    #l1.pop()            # last value will be deleted
    l1.remove(44)         # given value will be deleted

    print(f"After : len = {len(l1)} : l1 = {l1}")

#function3()

def function4():
    l1 = [33, 22, 55, 11, 44, 22]

    print(f"count of 22  = {l1.count(22)}")

    print(f"before reverse : {l1}")
    l1.reverse()
    print(f"after reverse : {l1}")
    print(f"before sort : {l1}")
    l1.sort()
    print(f"after sort : {l1}")

#function4()


def function5():
    l1 = [11, 22, 33, 44, 55]

    print(f"l1[0] = {l1[0]}")   #   11
    print(f"l1[1] = {l1[1]}")   #   22
    print(f"l1[2] = {l1[2]}")   #   33
    print(f"l1[-1] = {l1[-1]}") #   55
    print(f"l1[-2] = {l1[-2]}") #   44

    # 0 to n-1      forward indices
    # -1 to -n      backward indices

#function5()

def function6():
    l1 = list(range(11, 21))

    print(l1)

#function6()

def function7():
    student = ["abc", 12, 9, 95.0]

    print(f"type(student) = {type(student)}")
    print(f"len(student) = {len(student)}")
    print(f"student = {student}")

    print(f"name = {student[0]}")
    print(f"rollno = {student[1]}")
    print(f"std = {student[2]}")
    print(f"marks = {student[3]}")


function7()
