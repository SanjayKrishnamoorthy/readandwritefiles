import csv

file1 = open('customers.csv', 'r')
file2 = open('customers_country.csv','w')

count = 0




with open('customers.csv', 'r') as file:
    reader = csv.reader(file1)
    next(reader)
    for row in reader:
        file2.write(row[1])
        file2.write(" ")
        file2.write(row[2])
        file2.write(",")
        file2.write(" ")
        file2.write(row[4])
        file2.write("\n")
        count+=1
file1.close()
file2.close()

file2 = open('customers_country.csv','r')

print('Total number of customers: ',count)


file2.close()
