def fun():
    print("Inside fun function")

def test(func):
    func()

def outer():
    def inner():
        print("inside inner() function")

    return inner

print(f"type(fun) = {type(fun)}")

f1 = fun
f1()

test(fun)

inn = outer()
inn()
