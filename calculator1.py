#calculator
def addition(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y
def powerOf(x,y):
    return x ** y
count = 0
emptyString = ""
while True:
    print("select operation")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.increase first number by power of a second number")
    choice = input("enter choice(1/2/3/4/5): ")

    if count <= 99 and choice in ('1','2','3','4','5'):
        num1 = float(input("enter first number"))
        num2 = float(input("enter second number"))


        if choice == '1':
            print(num1, "+", num2, "=", addition(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "increased by the power of ", num2, "=",powerOf(num1, num2))
        count = count + 1

        print(emptyString)
        print(emptyString)
        print(emptyString)

    else:
        break


