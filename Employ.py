class Employee:
    def __init__(self):
        print('Employee created')
    def __del__(self):
        print("destructer called")
def create_object():
    print("making object")
    obj=Employee()
    print("function end")
    return obj
print("calling function")
obj = create_object()
print("program end")