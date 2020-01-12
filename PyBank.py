import os
import csv

#Establish variables
months = 0
total_pnl = 0
big_money=0
big_money_date=""
big_loss=0
big_loss_date=""
change_sum = 0
previous_pnl = 0
row_change = 0

#Load the file

file_path = os.path.join("Resources","budget_data.csv")

with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader:
    #The number of months included in the dataset
        months += 1
        profit = int(row[1])
    #The net total amount of "Profit/Losses" over the entire period
        total_pnl += profit
    #The average of the changes in "Profit/Losses" over the entire period
        
        #checking average
        #if months < 4:
        #print(f"last profit was {previous_pnl}")
        #print("new row is", row)
        if months == 1: row_change = 0
        else: row_change = profit - previous_pnl
        previous_pnl = profit
        #print(f"updated profit is {previous_pnl}")
        #print(f"row_change was {row_change}")
        change_sum += row_change
        #print(f"change_sum is {change_sum}")
        #print("")

    #  * The greatest increase in profits (date and amount) over the entire period
    #  * The greatest decrease in losses (date and amount) over the entire period
        if profit > big_money: 
            big_money=profit
            big_money_date = row[0]
        elif profit < big_loss: 
            big_loss=profit
            big_loss_date = row[0]

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)

file = open("PyBank_Results.txt", "w") 
file.write("\nFinancial Analysis")
file.write("\n---------------------------")
file.write("\nTotal Months: " + str(months))
file.write("\nTotal: $" + str(total_pnl))
file.write("\nAverage Change: $"  + str(round(change_sum/(months-1), 2)))
file.write(f"\nGreatest Increase in Profits: {big_money_date} (${big_money})")
file.write(f"\nGreatest Decrease in Profits: {big_loss_date} (${big_loss})")
file.close()

print(open("PyBank_Results.txt", "r").read())

file.close()