
PI = 3.142

def sum(n1, n2):
    return n1 + n2

def diff(n1, n2):
    return n1 - n2

sqr = lambda n : n ** 2
cube = lambda n : n ** 3
pow = lambda b, i : b ** i


if __name__ == '__main__':
    print(f"pi = {PI}")

    print(f"sum(10, 20) = {sum(10, 20)}")
    print(f"diff(20, 10) = {diff(20, 10)}")

    print(f"sqr(4) = {sqr(4)}")
    print(f"cube(3) = {cube(3)}")
    print(f"2 ^ 3 = {pow(2, 3)}")

    print(f"__name__  = {__name__}")

# __name__ is also called as dunder name
# this is set to '__main__' in a program which you are executing
