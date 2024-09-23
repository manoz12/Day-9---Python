import json

# Writing JSON data to a file
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

with open('data.json', 'w') as file:
    json.dump(data, file)

# Reading JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
    
import csv

# Writing to a CSV file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'London'])
    writer.writerow(['Bob', 25, 'Paris'])

# Reading from a CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
