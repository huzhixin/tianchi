#main.py 
import json
import csv

num = 0
numbers = []
with open('/tcdata/num_list.csv') as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        #numbers.append(row[0])
        number = int(row[0])
        num += number
        numbers.append(number)

numbers.sort(reverse = True)
f.close()
#print(numbers)
data = json.dumps({'Q1': 'Hello world', 'Q2': num, 'Q3':numbers[:10]})
json_file = open('result.json', 'w')
json_file.write(data)
json_file.close()
