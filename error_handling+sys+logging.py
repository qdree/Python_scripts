import sys 
import logging

def errorHandling():
    return "{0}. {1}, line: {2}".format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])

try:
    a+b
except:
    logging.error(errorHandling())

try:
	dict = {1:12}
	dict.append(12)
except:
	logging.error(errorHandling())
