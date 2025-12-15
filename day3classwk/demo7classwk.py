# set
#   - set is collection of unique similar or dissimilar type of data
#   - unordered
#   - not indexed
#   - mutable
#   s = {v1, v2, v3, ....}
#   s = set()   -- empty set

def function1():
    s1 = {11, 22, 33, 44, 55}

    print(f"type(s1) = {type(s1)}")
    print(f"len(s1) = {len(s1)}")
    print(f"s1 = {s1}")

    for ele in s1:
        print(ele)

#function1()

def function2():
    s1 = {11, 22, 33, 44}
    s2 = {33, 44, 55}

    print(f"union = {s1.union(s2)}")
    print(f"intersection = {s1.intersection(s2)}")

#function2()


def function3():
    s1 = {11, 22, 33, 44, 55}

    print(f"before : s1 = {s1}")

    #s1.add(66)
    #s1.add(44)

    #s1.pop()
    s1.remove(44)

    print(f"after : s1 = {s1}")

function3()

# frozenset
#   - set is collection of unique similar or dissimilar type of data
#   - unordered
#   - immutable
#   frozenset()   - conversion function 
