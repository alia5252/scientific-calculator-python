import math 
history = []
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def power (a,b):
    return a**b 
def modulus(a,b):
    return a % b
def sine(a):
    return math.sin(math.radians(a))
def cosine(a):
    return math.cos(math.radians(a))
def tangent(a):
    return math.tan(math.radians(a))
def logarithm(a):
    return math.log10(a)
def factorial(a):
    return math.factorial(int(a))
def divide(a,b):
    if b == 0:
        return "cant divide by 0"
    return a/b
def square_root(a):
    if a < 0:
        return "Square root undefined for negative numbers"
    return math.sqrt(a)

while True:
    print("\n simple calculator")
    print("Operations: +, -, *, /, %, **, sqrt, sin, cos, tan, log, fact")
    print("type history to see history")
    print("type 'clear history' to clean history")
    print("type 'exit' to stop")
    oprationn = input ("enter the oprationn:")
    if  oprationn == "exit":
        print("calculator closed")
        break
    elif oprationn == "history":
        if len(history) == 0:
            print("no history found")
        
        else:
            print("\ncalculation History:")
            for item in history:
                print(item)
        continue 
    elif oprationn == "clear history":
            history.clear()
            # clear file content also 
            open("history.txt", "w").close()
            print("history cleared")
            continue

    try:
        num1 = float(input ("enter first number:"))
    except ValueError:
        print("Invaild input ! please enter a number.")
        continue
    #single number oprations 
    if oprationn == "sqrt":
            result = square_root(num1)
            record = f"sqrt({num1}) = {result}"
    elif oprationn == "sin":
        result = sine(num1)
        record = f"sin({num1})= {result}"
    elif oprationn == "cos":
        result = cosine(num1)
        record = f"cos({num1})= {result}"
    elif oprationn == "tan":
        result = tangent(num1)
        record = f"tan({num1})= {result}"
    elif oprationn == "log":
        if num1 <= 0:
            result = "log undefined"
        else:
            result = logarithm(num1)
            record = f"log ({num1})= {result}"
    elif oprationn == "fact":
        if num1 < 0:
            result = " factorial undefined"
        else:
            result = factorial(num1)
            record = f"fact({num1})= {result}"
    # two - number oprationn
    else :
        try:
            num2 = int (input ("enter second   number:"))
        except ValueError:
            print("Invaild input ! please enter a number.")
            continue
        if oprationn == "+":
            result = add(num1,num2)
        elif oprationn == "%":
            result = modulus(num1,num2)
        elif oprationn == "-":
            result = subtract(num1,num2)
        elif oprationn == "*":
            result = multiply(num1,num2)
        elif oprationn == "/":
            result = divide(num1,num2)
        elif oprationn == "**":
            result = power (num1,num2)
        elif oprationn == "sqrt":
                result = square_root(num1)
        else:
            result = "invaild opration "
        record = f"{num1}{oprationn}{num2} = {result}"
    print ("Result = ",result)
    history.append(record)
    #save history to file 
    with open ("history.txt","a")as file :
        file.write(record + "\n")

