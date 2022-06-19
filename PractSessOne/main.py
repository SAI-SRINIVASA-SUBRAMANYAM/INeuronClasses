# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def test1():
    print("This is my first time to code using pycharm")
# Press the green button in the gutter to run the script.
def get_fib(n):
    a,b= 0,1
    for i  in range(n):
        yield a
        a, b = b, a+b

if __name__ == '__main__':
    print(__name__)
    print_hi('PyCharm')
    test1()
    for i in get_fib(10):
        print(i, end=", ")
print(__name__)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
