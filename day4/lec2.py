# list in python
# fruits=[item1,item2] syntax 
states_of_india = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jammu and Kashmir",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]
import random
ran=random.randint(1,28)
print(states_of_india[ran]) #Array return string with ran pos of array by random module
# len function return the lenth i.e no of item in list
# state_of_india[-1] print item at pos last in array 
# with ref of specific pos data in array can be altered
# Example
print(len(states_of_india))
# print(states_of_india[29]) 

#index out of range error as 
#there are 29 states but pos start  from 0 till 28 i.e last pos is n-1 of an array len return value-1

states_of_india[0]="shuja"
print(states_of_india[0])

states_of_india.append("something") #adds data at last pos of array 
states_of_india.extend(["item2","item3","item-4"]) #appends more than one data i.e an array can be inserted like this we have more function check out python doc lists 
print(states_of_india)

# list within a list 
# we can have this and this is called nested list 

# example

#we add district also in states example
districts_in_goa = ["North Goa", "South Goa"]
# now we have two list staes and distric 
# we can have single list states and district in list 
states_and_dist_of_india=[
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    ["North Goa", "South Goa"],
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jammu and Kashmir",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]
#we addes districts of goa list inside state list 
# now print 
print(states_and_dist_of_india)
print(states_of_india.index("Goa")) #returns index of that particular element in large list it is difficult to know thats why we use it 
# now printing list that is inside list of states_and_dist_of_india as we know index of that pos 
print(states_and_dist_of_india[6])
# Now printing element of distrinct i.e list in list's element

print(states_and_dist_of_india[6][1])

#thus it is like two dimentional list we can go on like this 

# we can have more than one lists as element inside an list 