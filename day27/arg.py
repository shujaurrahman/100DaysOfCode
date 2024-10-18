# advance arguments

# argument with default Value 
# myfunc(a=1,b=2,c=3)

# for specifying or changing only one value it ex b is changed just change that value 
# myfunc(b=5)

# *args

# myfunc(any no of input )

# myfunc(*number)

# it pass inputs as tuple 

# ex 

# def add(*args):
#     print(type(args))


# def add(*args):
#     r=0
#     for i in args:
#         r+=i
#     print(r)

# def add(*args):
#     print(args[0])
#     r=0
#     for i in args:
#         r+=i
#     print(r)


# add(1,2,3,4)

# unlimited no of arguments can be passed to the function as tuple and coded as per need 


# keywords arguments

# **kwargs , many keyworded arguments

# def cal(n,**kwargs):
    # print(kwargs)
    # for key,value in kwargs.items():
    #     print(key,value)

    # print(kwargs["add"])
    # gets the value by keyword of the argument 

    # add multiple operation by keyword 
    # n+=kwargs["add"]
    # n*=kwargs["mul"]

    # print(n)


# cal(2,add=3,mul=5)


# instead of tuple argument are passed as dictionary more efficient way to get hold of argument by name 
# and apply acton on it 


# class car:
#     def __init__(self,**kargs):
#         self.make=kargs["make"]
#         self.model=kargs["model"]

class car:
    def __init__(self,**kargs):
        self.make=kargs.get("make")
        self.make=kargs.get("model") #benefit: return none if keyword not found in dict

# mycar=car(make="nissan",model="2019")
mycar=car(make="nissan")
print(mycar.make)
