import csv

file1 = open('sales.csv', 'r')
file2 = open('salesreport.csv','w')



with open('sales.csv', 'r') as file:
    reader = csv.reader(file1)
    next(reader)
    print('Customer ID, Total')
    
    current_ID = 250
    current_sales = 0
    total_sales = 0
    for row in reader:
        if row[0] == str(current_ID):
            current_sales = float(row[3]) + float(row[4]) + float(row[5])
            total_sales += current_sales
        else:
            file2.write(str(current_ID))
            file2.write(' ')
            file2.write(str(round(total_sales, 2)))
            file2.write(' ')
            file2.write('\n')
            current_ID = row[0]
            current_sales = 0
            total_sales = 0
            current_sales = total_sales + float(row[3]) + float(row[4]) + float(row[5])
            total_sales += current_sales
    file2.write(str(current_ID))
    file2.write(' ')
    file2.write(str(total_sales))
    file2.write(' ')
    file2.write('\n')
        
            

        
file1.close()
file2.close()





file2.close()
