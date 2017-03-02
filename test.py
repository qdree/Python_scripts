import datetime, time

today = datetime.date.today()

# time00 = datetime.datetime.strptime("{} 00:00:00".format(today), "%Y-%m-%d %H:%M:%S")
# time12 = datetime.datetime.strptime("{} 12:00:00".format(today), "%Y-%m-%d %H:%M:%S")
# time19 = datetime.datetime.strptime("{} 19:00:00".format(today), "%Y-%m-%d %H:%M:%S")
# time15 = datetime.datetime.strptime("{} 15:00:00".format(today), "%Y-%m-%d %H:%M:%S")
# time21 = datetime.datetime.strptime("{} 21:00:00".format(today), "%Y-%m-%d %H:%M:%S")

time00 = datetime.time(hour=00)
time12 = datetime.time(hour=12)
time19 = datetime.time(hour=19)
time15 = datetime.time(hour=15)
time21 = datetime.time(hour=21)

time3 = datetime.time(hour=3)

now = datetime.datetime.time((datetime.datetime.now()))
print (now)

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

class Carrier(object):
	def __init__(self, days, hours):
		schedule = {}		
		self.hours = hours

		for d in days:
			for h in hours:
				schedule[d] = (hours[0],hours[1])

		print (schedule)
		# for h in hours:
		# 	print (str(h))

	def findCarriers(self, *carrier_names):
		pass

car = Carrier(weekdays, (time00, time12))

print (car.hours[0] > now)