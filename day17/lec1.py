# Creating classes in python
class User:
    # pass #skip for now content in the class 
    def __init__(self):
        print("New user created")

user_1=User()

# creating the object of User class which is just empty
 
# pascal case evry first letter capital -> PascalCase for classes 
# camelcase first letter lowecase then word starts with capital ->camelCase 
# snakecase where all letter of word is in lowercase but separated by _ ->snake_case

# adding atttribut to the class User

user_1.id="001"
user_1.username="shuja"

print(user_1.username)

user_2=User()

# now for user 2 we will need to specify everytime id and username therefore we specify it attribute in class using constructor
# contructor tell that for everytime an object is created what should happen i.e on initializing object 
# in python for constructor a special function is used called __init__(self): function 