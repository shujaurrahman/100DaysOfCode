# Docstring 
# documentation of the function when user hover it for future ref what it does

# function with return 
def format_name(f_name,l_name):
    """formats name first letter to capital rest small"""
    if f_name=="" or l_name=="":
        return "you didn't provide valid input"
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    return formated_f_name+formated_l_name
format_name("ShuJa","rahMaN")
print(format_name("",""))

