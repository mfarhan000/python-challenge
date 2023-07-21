import os
import csv

file_to_load = os.path.join ("Resources", "budget_data.csv")
file_to_output = os.path.join ("analysis", "budget_analysis.txt")

# Module 3 Challenge Questions: PyBank Instructions 

# Print Financial Analysis
print ("Financial Analysis")

# Print ----------------------------
print ("----------------------------")

# The total number of months included in the dataset
total_months = []
print (f'Total_Months: {total_months}')
# The net total amount of "Profit/Losses" over the entire period
net_total_profit_losses = []
total_net = []
print (f'total_net_profit: ${total_net}')
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
changes_in_profit_losses = [] 
# The greatest increase in profits (date and amount) over the entire period
greatest_increase_profits = [] 
# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease_profits = []

# Open and read csv file 

def count_months (file_path):
    try:
        with open(file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)

