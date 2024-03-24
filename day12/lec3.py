# Modify global variable in local variable 

enimies=1 #global variable
def enimy():
    # by global keyword
    global enimies
    enimies+=1
    print(f"No of enimies are : {enimies}")

enimy()
print(enimies)

# this will print 1 as enimies inside function is out of scope
# islye we try to avaid making variable global invites bugs and coder hates bugs 