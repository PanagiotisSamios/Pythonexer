import calendar
calendar.setfirstweekday(calendar.SUNDAY)
month = int(input('Give month in number '))
if month > 12 or month < 0:
	print ('not valid month')
else:
	year = int(input('Give year '))
	print ('\t', '\t', calendar.month_name[month], year, '\n')
	print ("S\tM\tT\tW\tT\tF\tS")
	calendar = calendar.monthcalendar(year, month)
	for i in range (len(calendar)):	
		for j in range (7):
			if calendar[i][j] == 0:
				print ('\t', end='')
			else:
				print ( calendar[i][j],'\t', end='')
		print ('\n') 
