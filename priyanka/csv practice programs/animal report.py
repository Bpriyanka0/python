import csv

with open("C:/Users/DELL/OneDrive/Desktop/animal report.csv","r")as file_object:

    data_table =csv.reader(file_object)

    for line in data_table:

        print(line[1])