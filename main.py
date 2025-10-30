'''
import csv
from operator import index

with open("weather_data (2).csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int((row[1])))
    print(temperature)





temp_list = data["temp"].to_list()

max_value = data["temp"].max()


#et Data in ro of our Data Frame
max_temp = data[data.temp == data.temp.max()]
print(max_temp)
monday = data[data.day == 'Monday']
fahrenheit_temps =( monday['temp'] * 9/5) + 32
print(f"Fahrenheit temps: {fahrenheit_temps}")
data = pandas.read_csv("weather_data (2).csv")


# Creating a DATAFRAME from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)


'''


import pandas
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels)
#print(red_squirrels)
#print(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels],
}

#df = pandas.DataFrame(data_dict)
#df.to_csv("squirrel_count.csv")