#pakage
# whole bunch of code written by other which can contain many modules

from prettytable import PrettyTable

table=PrettyTable()

# here we used method of the class prettyTable and perfomed methods on our instance or object 
table.add_column("City",['aligarh','delhi','pilibhit'])
table.add_column("State",['UP','delhi','UP'])

table.align="l"
# we accessed the attribute of the class and change the object attribute
print(table)
