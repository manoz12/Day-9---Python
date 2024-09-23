# Writing to the file
with open('data.txt', 'w') as file:
    file.write('Python is a great programming language.\n')
    file.write('It is widely used for web development, data science, and more.\n')

# Reading from the file
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)
    
with open('data.txt', 'r') as file:
    content = file.read()
    words = content.split()  # Split the content into words
    word_count = len(words)  # Count the number of words
    print(f'The number of words in the file is: {word_count}')
    
source_file = 'data.txt'
destination_file = 'copy_data.txt'

with open(source_file, 'r') as file:
    content = file.read()

with open(destination_file, 'w') as file:
    file.write(content)

print(f'Content copied from {source_file} to {destination_file}.')
# Read all lines into a list
with open('data.txt', 'r') as file:
    lines = file.readlines()

# Modify the second line
lines[1] = 'This is the modified second line.\n'

# Write back the modified lines to the file
with open('data.txt', 'w') as file:
    file.writelines(lines)

print('Second line modified successfully.')
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

