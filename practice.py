import csv

# Read CSV file and print all records
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\practice.csv", "r")
data = csv.reader(file)
for row in data:
    print(row)

file.close()


# filter 1
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\practice.csv", "r")
data = csv.reader(file)
for row in data:
    if "B" in row[1] and "f_50-99" in row[3]:
        print(row)

file.close()


# filter 2
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\practice.csv", "r")
data = csv.reader(file)
for row in data:
    if row[0] == "2020":
        print(row)

file.close()


# filter 3
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\practice.csv", "r")
data = csv.reader(file)
for row in data:
    if row[4] == "Total income":
        print(row)

file.close()


# filter 4
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\practice.csv", "r")
data = csv.reader(file)
for row in data:
    value = row[5]
    if value.isdigit() and int(value) > 1000:
        print(row)

file.close()



    