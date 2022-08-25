import csv
in_file = "Resources/budget_data.csv"
out_file= "analysis/budget_analysis_1.txt"


total_months = 0
previous_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999]
total_Profit_Losses = 0



with open(in_file) as revenue_data:
    reader = csv.DictReader(revenue_data)
    header = next(reader)
    # first_row = next(reader)
    # total_months += 1
    # total_Profit_Losses = total_Profit_Losses + int(first_row["Profit/Losses"])
    # previous_revenue = int(first_row["Profit/Losses"])

    for row in reader:
        # int(row["Profit/Losses"])
   
        total_months += 1
        total_Profit_Losses = total_Profit_Losses + int(row["Profit/Losses"])

        revenue_change = int(row["Profit/Losses"]) - previous_revenue
        previous_revenue = int(row["Profit/Losses"])
        revenue_change_list += [revenue_change]
        month_of_change += [row["Date"]]

        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"] 
            greatest_decrease[1] = revenue_change   

revenue_avg = sum(revenue_change_list)/ len(revenue_change_list)

output =  (f"/nFinancial Analysis\n",
    f"-------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Profit/Losses : ${total_Profit_Losses}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${'greastest_increase'[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")



print(output)

with open(out_file, "w")  as txt_file:
    txt_file.write(output)
    