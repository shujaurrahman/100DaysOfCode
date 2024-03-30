class User:
    # pass #skip for now content in the class 
    def __init__(self,user_id,username):
        # initializing attributeo of object  with contrutor for all objects 
        self.id=user_id
        self.username=username

user_1=User("001","shuja")

print(user_1.id,user_1.username)