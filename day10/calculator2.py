# calculator
import art
def add(a,b):
    """Add two numbers"""
    return a+b

def sub(a,b):
    """Subtracts two Numbers"""
    return a-b
def mul(a,c):
    """Multiply two numbers"""
    return a*c
def exp(a,b):
    """Exponents b to a """
    return b**a

def divide(a,b):
    """Divides two number"""
    if b!=0:
        return a/b
    else:
        return "Division not possible"

def calculator():
    print(art.logo)
    print("\nCalculator 2.0 \n")
    operation={
        "+":add,
        "-":sub,
        "*":mul,
        "/":divide,
        "^":exp,
    }
    print("which of this operation do you want to perform ? ")



    num1=float(input("what's the first number? "))
    should_continue=True
    for key in operation:
        print(key)
    while should_continue: 
        op_symbol=input("Pick out a symbol: ")
        num2=float(input("what's the next number? "))
        cal=operation[op_symbol]
        answer=cal(num1,num2)
        print(f"{num1} {op_symbol} {num2} = {answer}.")
        if input(f"Type 'Y' to continue calculating with {answer}. or Type 'n' to start a new  calulation. ").lower()=="y":
            num1=answer
        else:
            should_continue=False
            calculator()

calculator()