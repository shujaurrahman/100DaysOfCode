import pandas
# data=pandas.read_csv("day25/weather_data.csv")

# print(type(data['temp']))

# data_dict=data.to_dict()

# temp_list=data['temp'].to_list()

# # average=sum(temp_list)/len(temp_list)

# # print(average)


# print(data['temp'].mean())

# # Get column 
# print(data['condition'])
# print(data.condition)

# get row
# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])

# create a dataframe 
data_dict={
    "students":["Amy","James","Angela"],
    "scores":[76,56,65]
}

data=pandas.DataFrame(data_dict)

print(data)
data.to_csv("day25/new_csv.csv")