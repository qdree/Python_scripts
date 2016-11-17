import time
def check1sec():
	start = time.time()
	while True:
		current = time.time()
		if (current - start) >= 2:
			return
		else:
			print (current - start)


def wait(seconds):
	start_time = time.time()
	while True:
		current_time = time.time()
		#print (float(current_time - start_time))
		if float(current_time - start_time) >= seconds:
			break

#check1sec()
print "hi, after 5 sec u\'ll see new message"
wait(5)
print "here is message as promised"