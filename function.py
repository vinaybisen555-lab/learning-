
def square(number):
    return number * number


num = int(input("Enter a number: "))
print("Square:", square(num))

double = lambda x: x * 2
print("Double:", double(num))
