#financial analysis

#import csv
import csv
import os

total_months = []
profit_loss_change = []
cur_monthr = 0
prev_monthr = 0

file_path = os.path.join ("Resources", "budget_data.csv")
open("Pybankhw.txt", "w+")

with open(file_path, "r") as f:
    reader = csv.reader(f)
    
next(reader)

for row in (csvreader):
    total_month = total_month + 1 
    total.months.append(row[0])
    cur_monthr = int(row[1])
    total_revenue = total_revenue + int(row[1])
    if total_months >1:
        rchange = current_monthr - prev_monthr 
        rchange.append(rchange)

rchange = 0

        sum_changesr = sum(rchange)
        average_change = sum_changesr / (total_month -1)
        max_change = max(rchange)
        min_change = min(rchange)
        max_month = rchange(max_change)
        min_month = rchange(min_change)
        max_month = total_months[max_month]
        min_month = total_months[min_month]

print("financial analysis")
print("----------------------------------------")
print(f"total months: {len(months)}")
print(f"total revenue: ${total_revenue}")
print(f"average revenue change: ${average_change}")
print(f"greatest increase in revenue: {max_month} (${max_change})")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change})")

with open("./results.txt",'w') as text:
   text.write("financial analysis" + "\n")
   text.write("----------------------------------------" + "\n")
   text.write(f"total months: {month_count}" + "\n")
   text.write(f"total revenue: ${total_revenue}" + "\n")
   text.write(f"average revenue change: ${average_change}" + "\n")
   text.write(f"greatest r increase: {max_month} (${max_change})" + "\n")
   text.write(f"greatest r decrease: {min_month} (${min_change})" + "\n")

