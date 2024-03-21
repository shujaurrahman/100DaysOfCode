# Dictionary in python i.e a list with key and its value key->value syntax {key:value}
# {"bug":"An error"}

dictionary={
    "Name":"Shuja",
    "class":"MCA",
    "Roll no":"CAMS104",
}

# dictionary have element which are identified by thier key 
print(dictionary["Name"])

# adding new item to dict
dictionary["location"]="Aligarh"

print(dictionary)

# like empty list can be created so does empty dictionary 
# example
empty_dictionary={}

# wipe an existion dictionary by diclaring it empty 
# dictionary={}

# looping in dictionary
for things in dictionary:
    print(things)

# this only prints the keyof the dictionary not the value of the dictionary 
# for the value we retrive the value of the key
for key in dictionary:
    print(key)
    print(dictionary[key])

