# Data types in python
# strings

# printing character in strings
print("hell0"[2])

# double quotes outside interges will be treated as strings and this will lead to concatination
print("123"+"456")

# float 
print(3.145)

# int
print(123)

# Boolean
x=True
print(x)

# num_char=len(input("What is your name?  "))
# print("Your name conatins "+ str(num_char) +" characters.")

# Mathematical operation in pythons 
# add sub multiply divide
print(2-3)
4+5
4*5
6/3
2**3

# PEMDASLR 

print(int(8/3))  
# this converts into integers instead of round number

# for this we have round number function 
print(round(8/3,2))

# round(operation,places till to be rounded)

print("floor division return division in intergers \n")
print(8//2)

# short hand for mathematical operation 
a=0
a=a+1
# can be written as 
a+=1
# similarly
a-=1
a*=2
a/=3

# f-string 
# converting various data type variable into string in one go example
number=3
floatingno=3.444
booleanv=True

# now to print each one of the datatype needs to be converted into string datatype
# but we have f-string and with its use we can convert all other datatype into string

print(f"the string with all datatype is {number} and {floatingno} and {booleanv}")

