# import pandas

# data=pandas.read_csv("day25/weather_data.csv")

# print(data["temp"])

# data_dict=data.to_dict()
# print(data_dict)

# data_temp_list=data["temp"].to_list()
# print(data_temp_list)

# # n=len(data_temp_list)
# # s=0
# # for i in data_temp_list:
# #     s+=i

# # a=s/n
# # print(a)

# av=sum(data_temp_list)/len(data_temp_list)
# print(av)

# print(data["temp"].mean())

# print(data["temp"].max())

# print(data.day)

# print(data[data.day=="Monday"])

# print(data[data.temp==data.temp.max()])


import pandas as pd
data=pd.read_csv("day25/Squirrel_Data.csv")

grey_sq=len(data[data["Primary Fur Color"]=="Gray"])
red_sq=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_sq=len(data[data["Primary Fur Color"]=="Black"])
print(grey_sq,red_sq,black_sq)

data_Dict={
    "fur color":["Gray","Cinnamon","Black"],
    "count":[grey_sq,red_sq,black_sq]

}

print(data_Dict)

df=pd.DataFrame(data_Dict)
df.to_csv("day25/sq-count.csv")
