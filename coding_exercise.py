import datetime, time

today = datetime.datetime.today()
end_date = today.date() + datetime.timedelta(days=2)

# time00 = datetime.datetime.strptime("{} 00:00:00".format(end_date), "%Y-%m-%d %H:%M:%S")
# time12 = datetime.datetime.strptime("{} 12:00:00".format(end_date), "%Y-%m-%d %H:%M:%S")
# time15 = datetime.datetime.strptime("{} 15:00:00".format(end_date), "%Y-%m-%d %H:%M:%S")
# time19 = datetime.datetime.strptime("{} 19:00:00".format(end_date), "%Y-%m-%d %H:%M:%S")
# time21 = datetime.datetime.strptime("{} 21:00:00".format(end_date), "%Y-%m-%d %H:%M:%S")

time00 = datetime.datetime.strptime("{} 00:00:00".format(today.date()), "%Y-%m-%d %H:%M:%S")
time12 = datetime.datetime.strptime("{} 12:00:00".format(today.date()), "%Y-%m-%d %H:%M:%S")
time15 = datetime.datetime.strptime("{} 15:00:00".format(today.date()), "%Y-%m-%d %H:%M:%S")
time19 = datetime.datetime.strptime("{} 19:00:00".format(today.date()), "%Y-%m-%d %H:%M:%S")
time21 = datetime.datetime.strptime("{} 21:00:00".format(today.date()), "%Y-%m-%d %H:%M:%S")

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

A = {
	weekdays[0]: (time00, time12), 
	weekdays[1]: (time00, time12),
	weekdays[2]: (time00, time12), 
	weekdays[3]: (time00, time12), 
	weekdays[4]: (time00, time12), 
	weekdays[5]: (time12,), 
	weekdays[6]: (time12,)
	}

B = {
	weekdays[0]: (time19,), 
	weekdays[1]: (time19,),
	weekdays[2]: (time19,), 
	weekdays[3]: (time19,), 
	# weekdays[4]: ("",), 
	# weekdays[5]: ("",), 
	weekdays[6]: (time19,)
	}

C = {
	weekdays[0]: (time15, time21), 
	weekdays[1]: (time15,),
	weekdays[2]: (time15, time21), 
	weekdays[3]: (time15,), 
	weekdays[4]: (time15, time21),
	# weekdays[5]: ("",), 
	# weekdays[6]: ("",)
	}

Carriers_tuple = (A, B, C)

todays_day = datetime.datetime.today().weekday()
current_time = datetime.datetime.now()
# current_time = datetime.datetime.now()

print (weekdays[todays_day])

def findCarrier(carrier):
	carrier_schedule = {}
	if carrier == 'A': carrier_schedule = A
	elif carrier == 'B': carrier_schedule = B
	elif carrier == 'C': carrier_schedule = C
	# print(carrier)

	for schedule in Carriers_tuple:
		# print (carrier)
		if schedule == carrier_schedule:
			for week_day in schedule:
				for hours in schedule[week_day]:
					delta_in_hours = (hours - current_time).total_seconds()/60/60
					if delta_in_hours > 1:
						return (carrier,week_day,str(hours))



print(findCarrier(input("Input carrier: ").upper()))




# s1 = 'Mon Jan 1 01:39:30 2017'
# # s1 = 'Mon Jan 1 01:39:30 2017'.format(day)
# now = datetime.datetime.today()

# d1 = datetime.datetime.strptime(s1, '%a %b %d %H:%M:%S %Y')
# d2 = datetime.datetime.strptime(now.ctime(), '%a %b %d %H:%M:%S %Y')

# delta_in_days = (d1-d2).total_seconds()/60/60/24
# delta_in_hours = (d1-d2).total_seconds()/60/60

# end_date = today.date() + datetime.timedelta(days=2)


# if (delta_in_hours > 3):
# 	print (d2)
# 	print (delta_in_days)
# 	print (delta_in_hours)
# 	print (d1-d2)
# 	print (today.ctime())
# 	print (end_date.weekday())