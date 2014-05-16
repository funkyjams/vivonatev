#!/bin/env python

import sys

def exit(str):
	print str
	sys.exit()




if __name__ == "__main__":
	
	usage = "vect2 vector_length mpileup_input_file [output_file]"
	
	if (len(sys.argv) < 3) or (len(sys.argv) > 4):
		exit(usage)

	try:
	 	vect_len = int(sys.argv[1])
		infile_name = sys.argv[2]
		if len(sys.argv) == 4:
			outfile_name = sys.argv[3]
			out = open(outfile_name, 'w')
		else:
			out = sys.stdout
		
		vector = [0]*vect_len
		infile = open(infile_name, 'r')
		inlines = infile.readlines()

		for line in inlines:
			splitline = line.split()
			vector[ int(splitline[1]) - 1] = int(splitline[3])

		i=0
		while (i < vect_len):
			out.write( str(i + 1) + ' ' + str(vector[i]) + '\n' )
			i+=1

		infile.close()
	
	except IOError as e:
		print "input file " + infile_name + " does not exist"
		print e
	finally:
		if sys.argv == 4:
			out.close()
