# File handling in python 
# file =open("day24/data.txt")
# content=file.read()
# print(content)
# file.close()


# if we don't want to deal with close in python we use 
# default mode is set to r that is write 
# with open("day24/data.txt") as f:
#     content=f.read()
#     print(content)


# to write on the file 

with open("day24/data.xt",mode='a') as f:
    f.write("Pursuing mca at AMU")


# differne mode for diff thing r for read w for write a for append 