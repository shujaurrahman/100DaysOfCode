# calculator

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

operation={
    "+":add,
    "-":sub,
    "*":mul,
    "/":divide,
    "^":exp,
    }

# works like this
# function=operation["+"] we call the key and key value of key for this add fuction and assign to a fucntion
# print(function(2,3)) call function

num1=int(input("what's the first number? "))
num2=int(input("what's the second number? "))
print("which of this operation do you want to perform ? ")
for key in operation:
    print(key)

op_symbol=input("Pick out a symbol: ")
cal=operation[op_symbol]

print(f"{num1} {op_symbol} {num2} = {cal(num1,num2)}.")