# # with open("./day25/weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)

# import csv

# with open("./day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])

#     print(temperatures)

import pandas

data = pandas.read_csv("./day25/weather_data.csv")
print(data["temp"])
