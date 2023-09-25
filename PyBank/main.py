# Import the modules
import os
import csv

# Create a path for the csv file from the Resources directory
budgetcsv = os.path.join("Resources", "budget_data.csv")

# Create lists to store the data from the budget_data csv
date = []
# profit = []
# losses = []
profit_losses = []


# Open the budget_data csv file
with open(budgetcsv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

# Pass by the header so the code only works with the raw data
    csvheader = next(csvfile)
    # Append the column data into their specific lists
    for row in csvreader:
        date.append(row[0])
        profit_losses.append(int(row[1]))
# Initialize a dynamic data point for the months in the dataset using the number of rows in the csv
totalmonths = len(date)
# Initialize a dynamic calculation of the revenue
totalrevenue = sum(profit_losses)


# Initialize variables to keep track of the month to month changes
total_mtm_change = 0
mtm_counter = 0
max_change = 0
min_change = 0

# Set a counter to loop through the rows starting from one less than the total number of values in the dataset
for i in range(len(profit_losses) - 1):
    # Use the loop to subtract from the next month's value using a plus one modifier to stay ahead of the next month in the sequence
    change = profit_losses[i + 1] - profit_losses[i]
    # Create a mechanism to automatically update the new calculations found in the loop
    total_mtm_change += change
    # Set an updating counter for the if statement to calculate the average
    mtm_counter += 1

    # Create an if statement to check and update the maximum and minimum value changes in the loop
    if change > max_change:
        max_change = change
        # Initialize a reference number for the month that the updated maximum and minimum values occurred on  
        max_row_ref = i + 1
        
    if change < min_change:
        min_change = change
        min_row_ref = i + 1

# Set an if statement to check that the program will not divide by 0
    if mtm_counter > 0:
        average_change = total_mtm_change / mtm_counter
    else:
        average_change = 0
# Initialize formatted output data from the loop
avg_mtm_change = round(average_change, 2)
format_max_change = round(max_change, 2)
format_min_change = round(min_change, 2)

# Print the output data into a formatted analysis report
print("\n")
print("Financial Analysis")
print("\n")
print("----------------------------")
print("\n")
print(f"Total Months: {totalmonths}")
print(f"Total: ${totalrevenue}")
print(f"Average Change: ${avg_mtm_change}")
print(f"Greatest Increase in Profits: {date[max_row_ref]} ${format_max_change}")
print(f"Greatest Decrease in Profits: {date[min_row_ref]} ${format_min_change}")


# Open and generate a text file to print the financial analysis to the Analysis folder
with open(os.path.join("Analysis", "Financial_Analysis.txt"), "w") as txt:
    # Transpose all of the print lines into the file so it updates with every new entry of the analysis
    txt.write("\n")
    txt.write("Financial Analysis\n")
    txt.write("\n")
    txt.write("----------------------------\n")
    txt.write("\n")
    txt.write(f"Total Months: {totalmonths}\n")
    txt.write(f"Total: ${totalrevenue}\n")
    txt.write(f"Average Change: ${avg_mtm_change}\n")
    txt.write(f"Greatest Increase in Profits: {date[max_row_ref]} ${format_max_change}\n")
    txt.write(f"Greatest Decrease in Profits: {date[min_row_ref]} ${format_min_change}\n")
    txt.close()

