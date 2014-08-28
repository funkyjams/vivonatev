#!/bin/env python

import sys
import re

class NoAlignmentException(Exception):
	def __init__(self, message):
		self.message = message

def isAboveThreshold(log, threshold):
	if threshold == 0:
		return True

	lines = log.readlines()

	for line in lines:
		if re.search("aligned 0 times", line):
			num = float(line.split()[1][1:6])
			
			if (num > (100 - threshold)):
				return False
			else:
				return True

	raise NoAlignmentException("Alignement not found") 

if __name__=="__main__":

	if len(sys.argv) != 3:
		print "Wrong usage: "
		print "isAboveThreshold logfile threshold"
		sys.exit()

	logfile = open(sys.argv[1], 'r')
	threshold = float(sys.argv[2])
	try:
		print isAboveThreshold(logfile, threshold)
	except NoAlignmentException as e:
		print e.message
	except Exception as e:
		print "Other error:"
		print e.message
