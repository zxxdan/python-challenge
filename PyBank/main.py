import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv) as csvfileread:
    csvreader = csv.reader(csvfileread, delimiter=",")
    csv_header = next(csvreader)

    num_month = 0
    total = 0
    great_incr = 0
    great_decr = 0
    great_incr_mth = 0
    great_decr_mth = 0
    previous = 0
    delta = 0
    
    for row in csvreader:

        # The net total amount of "Profit/Losses" over the entire period
        total = total + int(row[1])

        # The average of the changes in "Profit/Losses" over the entire period
        
        if num_month > 0:
            # The 
            change = int(row[1]) - previous

            if change > great_incr:
                    great_incr = change
                    great_incr_mth = row[0]

            if change < great_decr:
                    great_decr = change
                    great_decr_mth = row[0]

            delta = delta + change

        previous = int(row[1])

        # The total number of months included in the dataset
        num_month += 1

    average = round(delta/(num_month - 1),2)

    print("==================================================================================================================")
    print("FINANCIAL ANALYSIS")
    print("==================================================================================================================")   
    print(f"Total Months: {num_month}")
    print(f"Total: $ {total}")
    print(f"Average Change: $ {average}")
    print(f"Greatest Increase in Profits: {great_incr_mth}  $ {great_incr}")
    print(f"Greatest Increase in Profits: {great_decr_mth}  $ {great_decr}")
    print("==================================================================================================================") 

output = os.path.join("budget_summary.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output, 'w') as textfile:

    textfile.writelines("==================================================================================================================" + "\n")
    textfile.writelines("FINANCIAL ANALYSIS" + "\n")
    textfile.write("==================================================================================================================" + "\n")       
    textfile.write(f"Total Months: {num_month}" + "\n")
    textfile.write(f"Total: $ {total}" + "\n")
    textfile.write(f"Average Change: $ {average}" + "\n")
    textfile.write(f"Greatest Increase in Profits: {great_incr_mth}  $ {great_incr}" + "\n")
    textfile.write(f"Greatest Increase in Profits: {great_decr_mth}  $ {great_decr}" + "\n")
    textfile.write("==================================================================================================================" + "\n")
