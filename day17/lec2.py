class User:
    # pass #skip for now content in the class 
    def __init__(self,user_id,username):
        # initializing attributeo of object  with contrutor for all objects 
        self.id=user_id
        self.username=username
        self.followers=0 #default value for all object without passsing to contructor by default 

user_1=User("001","shuja")

print(user_1.id,user_1.username,user_1.followers)