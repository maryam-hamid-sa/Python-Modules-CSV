import csv

# Read CSV file and print all records
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\arkansas.csv", "r")
data = csv.reader(file)
for row in data:
    print(row)

file.close()


# filter 1
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\arkansas.csv", "r")
data = csv.reader(file)
for row in data:
        if row[6] == "black":
            print(row)

file.close()


# filter 2
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\arkansas.csv", "r")
data = csv.reader(file)
for row in data:
        if row[7] == "female":
            print(row)

file.close()


# filter 3
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\arkansas.csv", "r")
data = csv.reader(file)
for row in data:
        if row[9] == "TRUE":
            print(row)

file.close()


# filter 4
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\arkansas.csv", "r")
data = csv.reader(file)
for row in data:
        age = row[5]
        if age.isdigit() and int(age) >= 50:
            print(row)

file.close()