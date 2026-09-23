import pandas

primary_data = pandas.read_csv("100-dni-z-pythonem/dzien 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color_data = primary_data["Primary Fur Color"]
categorized_fur_color_data = fur_color_data.value_counts()
categorized_fur_color_data.to_csv("100-dni-z-pythonem/dzien 25/squirrel_count.csv",)