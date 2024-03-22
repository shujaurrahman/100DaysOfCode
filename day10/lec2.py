# function with return 
def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "you didn't provide valid input"
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    return formated_f_name+formated_l_name
format_name("ShuJa","rahMaN")
print(format_name("",""))