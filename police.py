import csv

# Read CSV file and print all records
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\police.csv", "r")
data = csv.reader(file)
for row in data:
    print(row)

file.close()


# filter 1
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\police.csv", "r")
data = csv.reader(file)
for row in data:
        if row[3] == "F":
            print(row)

file.close()


# filter 2
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\police.csv", "r")
data = csv.reader(file)
for row in data:
        if row[8] == "Speeding":
            print(row)

file.close()


# filter 3
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\police.csv", "r")
data = csv.reader(file)
for row in data:
        if row[6] == "Black":
            print(row)

file.close()


# filter 4
file = open("c:\\Users\\MARYAM HAMID\\Downloads\\Assignment 4 CSV\\police.csv", "r")
data = csv.reader(file)
for row in data:
        if row[12] == "True":
            print(row)

file.close()
