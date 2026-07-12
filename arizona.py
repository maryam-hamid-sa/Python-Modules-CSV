import csv

# Read CSV file and print all records
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\arizona.csv", "r")
data = csv.reader(file)
for row in data:
    print(row)

file.close()


# filter 1
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\arizona.csv", "r")
data = csv.reader(file)
for row in data:
        if row[7] == "pedestrian":
            print(row)

file.close()


# filter 2
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\arizona.csv", "r")
data = csv.reader(file)
for row in data:
        if row[7] == "vehicular":
            print(row)

file.close()


# filter 3
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\arizona.csv", "r")
data = csv.reader(file)
for row in data:
        if row[8] == "WHI":
            print(row)

file.close()


# filter 4
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\arizona.csv", "r")
data = csv.reader(file)
for row in data:
        if row[1].startswith("2008"):
            print(row)

file.close()
