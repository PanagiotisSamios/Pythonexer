import datetime
from datetime import date
Date = datetime.date.today().strftime("%d")
Date = int(Date)
Day = datetime.date.today().strftime("%A")
Month = datetime.date.today().strftime("%m")
Month = int(Month)
Year = datetime.date.today().strftime("%Y")
Year = int(Year)
print (Date, Day, Month, Year)
count = 0
for Year in range (Year, Year + 11):
	for Month in range (Month,13):
		if Month < 12: 
			month_days = (date(Year, Month + 1, 1) - date(Year, Month, 1)).days
		else:
			month_days = 31
		if month_days == 28 and Date <= 28:
			Day_2 = datetime.date(Year, Month, Date).strftime("%A")
			if Day_2 == Day:
				count = count + 1
		elif month_days == 29 and Date <= 29:
			Day_2 = datetime.date(Year, Month, Date).strftime("%A")
			if Day_2 == Day:
				count = count + 1
		elif month_days == 30 and Date <=30:
			Day_2 = datetime.date(Year, Month, Date).strftime("%A")
			if Day_2 == Day:
				count = count + 1
		elif month_days == 31 and Date <= 31:
			Day_2 = datetime.date(Year, Month, Date).strftime("%A")
			if Day_2 == Day:
				count = count + 1
	Month = 1
print ("The next 10 years will have ", count, Day,"'s", " that will be the ", Date, " of a month including today.") 
		

		
		
