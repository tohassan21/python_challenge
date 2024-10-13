# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
first_row = 0
net_change = []
previous_profit = None
months = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change
    # Track the total and net change
    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1
        total_net += int(row[1])
        month = row[0]
        
        # Track the net change
        current_profit = int(row[1])
        if previous_profit is not None:
            change = current_profit - previous_profit
            net_change.append(change)
            months.append(month) #to add corresponding month
        previous_profit = current_profit

if len(net_change) > 0:
    # Calculate the greatest increase in profits (month and amount)
    max_change = max(net_change)
    max_index = net_change.index(max_change) #get index of max change
    max_month = months[max_index] #get corresponding month

    # Calculate the greatest decrease in losses (month and amount)
    min_change = min(net_change)
    min_index = net_change.index(min_change) #get index of min change
    min_month = months[min_index] #get corresponding month  

    # Calculate the average net change across the months
    avg_change = sum(net_change) / len(net_change)

# Generate the output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase In Profits: {max_month} (${max_change})\n"
    f"Greatest Decrease In Profits: {min_month} (${min_change})\n"
)

# Print the output
print(output)     

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
