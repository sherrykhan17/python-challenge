import os
import csv

budget_data_csv = os.path.join("./", "Resources", "budget_data.csv")
budget_data_csv_output = os.path.join("./", "analysis", "budget_data.txt")

print(f'budget_data_csv {budget_data_csv}')
print(f'budget_data_csv_output {budget_data_csv_output}')

total_months = 0
total_profit_loss = 0

past_profit_loss = 0
average_changes_profit_loss = []
greatest_increase_profit = ["", 0]
greatest_decrease_profit = ["", 10000000]

with open(budget_data_csv) as csvbudgetdata:
    reader = csv.DictReader(csvbudgetdata)

    for row in reader:
        total_months = total_months + 1
        total_profit_loss = total_profit_loss + int(row["Profit/Losses"])

        current_average_profit_loss = int(row["Profit/Losses"]) - past_profit_loss
        if past_profit_loss != 0:
            average_changes_profit_loss.append(current_average_profit_loss)

        past_profit_loss = int(row["Profit/Losses"])

        if (current_average_profit_loss > greatest_increase_profit[1]):
            greatest_increase_profit[1] = current_average_profit_loss
            greatest_increase_profit[0] = row["Date"]

        if (current_average_profit_loss < greatest_decrease_profit[1]):
            greatest_decrease_profit[1] = current_average_profit_loss
            greatest_decrease_profit[0] = row["Date"]

avg_profit_lose = sum(average_changes_profit_loss) / len(average_changes_profit_loss)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total : " + "$" + str(total_profit_loss))
print("Average Change: " + "$" + str(round(sum(average_changes_profit_loss) / len(average_changes_profit_loss), 2)))
print("Greatest Increase in Profits: " + str(greatest_increase_profit[0]) + " ($" + str(greatest_increase_profit[1]) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease_profit[0]) + " ($" + str(greatest_decrease_profit[1]) + ")")



with open(budget_data_csv_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total : " + "$" + str(total_profit_loss))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(average_changes_profit_loss) / len(average_changes_profit_loss), 2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase in Profits: " + str(greatest_increase_profit[0]) + " ($" + str(greatest_increase_profit[1]) + ")")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in Profits: " + str(greatest_decrease_profit[0]) + " ($" + str(greatest_decrease_profit[1]) + ")")
    