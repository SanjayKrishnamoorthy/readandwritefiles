import csv



file1 = open('EmployeePay.csv', 'r')
count = 0


with open('EmployeePay.csv', 'r') as file:
    reader = csv.reader(file1)
    for row in reader:
        if count !=0:
            salary = int(row[3])
            bonus = float(row[4])
            total_pay = salary + (salary * bonus)
            print('ID: ',row[0], ' Name: ', row[1]+' '+row[2], ' Total Pay: ', total_pay)
        count +=1
        input()
file1.close()



