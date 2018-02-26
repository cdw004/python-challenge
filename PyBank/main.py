import os
import csv

csvpath1 = os.path.join('Resources', 'budget_data_1.csv')
csvpath2 = os.path.join('Resources', 'budget_data_2.csv')

#Variables for CSV1
month_count1 = 0
total_revenue1 = 0
CMRI_01=0
LMRI_01=0
RC_01 = 0
RCS_01 = 0
RevChanges01=[]
Month_Changes01 = []

#Variables for CSV2
month_count2 = 0
total_revenue2 = 0
CMRI_02=0
LMRI_02=0
RC_02 = 0
RCS_02 = 0
RevChanges02=[]
Month_Changes02 = []

#CSV 1 - BUDGET_DATA 1 COMMANDS
with open (csvpath1, newline="") as csvfile:
    csvreader1 = csv.reader(csvfile, delimiter=",")
    next(csvreader1)

    for row in csvreader1:
      month_count1 += 1
      Month_Changes01.append(row[0])
      total_revenue1 += int(row[1])
      CMRI_01 = int(row[1])
      if month_count1 > 1:
        RC_01 = CMRI_01 - LMRI_01
        RevChanges01.append(CMRI_01)
        LMRI_01 = CMRI_01

#Finding Revenue Changes Budget_DATA_01
SRevChanges01 = sum(RevChanges01)
average_change01 = SRevChanges01 / (month_count1 -1)
max_change01 = max(RevChanges01)
min_change01 = min(RevChanges01)
max_month_index01 = RevChanges01.index(max_change01)
min_month_index01 = RevChanges01.index(min_change01)
max_month01 = Month_Changes01[max_month_index01]
min_month01 = Month_Changes01[min_month_index01]

#CSV 2 - BUDGET_DATA 2 COMMANDS
with open (csvpath2, newline="") as csvfile:
    csvreader2 = csv.reader(csvfile, delimiter=",")
    next(csvreader2)
    

    for row in csvreader2:
      month_count2 += 1
      Month_Changes02.append(row[0])
      total_revenue2 += int(row[1])
      CMRI_02 = int(row[1])
      if month_count1 > 1:
        RC_02 = CMRI_02 - LMRI_02
        RevChanges02.append(CMRI_02)
        LMRI_02 = CMRI_02

#Finding Revenue Changes Budget_DATA_02
SRevChanges02 = sum(RevChanges02)
average_change02 = SRevChanges02 / (month_count2 -1)
max_change02 = max(RevChanges02)
min_change02 = min(RevChanges02)
max_month_index02 = RevChanges02.index(max_change02)
min_month_index02 = RevChanges02.index(min_change02)
max_month02 = Month_Changes02[max_month_index02]
min_month02 = Month_Changes02[min_month_index02]


#CALCULATING TOTALS
totalmonths = int(month_count1) + int(month_count2)
totalrevenue = int(total_revenue1) + int(total_revenue2)
totalaverage = (int(average_change02) + int(average_change01)) / 2

#For First CSV File
#print("Total Financial Analysis: BUDGET_DATA_1:")
#print("----------------------------")
#print("Total Months for Budget_Data_1: " + str(month_count1))
#print("Total Revenue for Budget_Data_1: " + str(total_revenue1))
#print("Average Changes for Budget_Data_1: " + str(average_change01))
#print("Greatest Increase in Revenue: Date: "+ str(max_month01) +" Increase: $"+ str(max_change01))
#print("Greatest Decrease in Revenue: Date: "+ str(min_month01) +" Decrease: $"+ str(min_change01))

#print("----------------------------")
#print("                            ")
#print("                            ")

#For Second CSV File
#print("Total Financial Analysis: BUDGET_DATA_2:")
#print("----------------------------")
#print("Total Months for Budget_Data_2: " + str(month_count2))
#print("Total Revenue for Budget_Data_2: " + str(total_revenue2))
#print("Average Changes for Budget_Data_2: " + str(average_change02))
#print("Greatest Increase in Revenue: Date: "+ str(max_month02) +" Increase: $"+ str(max_change02))
#print("Greatest Decrease in Revenue: Date: "+ str(min_month02) +" Decrease: $"+ str(min_change02))



#print("----------------------------")
#print("                            ")
#print("                            ")

#Combined Totals
print("Total Financial Analysis: TOTAL")
print("----------------------------")
print("Total Months: " + str(totalmonths))
print("Total Revenue: " + str(totalrevenue))
print("Total average change: " + str(totalaverage))
print("Total Greatest Increase in Revenue: Date: "+ str(max_month01) +" Increase: $"+ str(max_change01))
print("Total Greatest Decrease in Revenue: Date: "+ str(min_month01) +" Decrease: $"+ str(min_change01))