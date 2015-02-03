#! /usr/bin/env python

#Created by @binkybear and @byt3bl33d3r

import sys
import re
import os
from keyseed import *
import argparse
from decimal import Decimal #for conversion milliseconds -> seconds

parser = argparse.ArgumentParser(description='Converts USB rubber ducky scripts to a Nethunter format', epilog="Quack Quack")
parser.add_argument('-l', type=str, dest='layout', choices=['us', 'fr', 'de', 'es','sv', 'it', 'uk', 'ru','dk','no','pt','be'], help='Keyboard layout')
parser.add_argument('duckyscript', help='Ducky script to convert')

args = parser.parse_args()

# Input file is argument / output file is output.txt
infile = open(args.duckyscript)
tmpfile = open("tmp.txt", "w")
#args.layout = sys.argv[2]

def duckyRules (source):

	tmpfile = source

	for (k,v) in rules.items():
		regex = re.compile(k)
		tmpfile  = regex.sub(v, tmpfile)

	return tmpfile

if __name__ == "__main__": 

	rules = { 
	 r'ALT' : u'alt',
	 r'GUI' : 'left-meta',
	 r'WINDOWS' : 'left-meta',
	 r'ALT' : 'alt',
	 r'CONTROL' : 'left-ctrl',
	 r'CTRL' : 'left-ctrl',
	 r'SHIFT' : 'left-shift',
	 r'MENU' : 'left-shift f10',
	 r'APP' : 'escape',
	 r'ESCAPE' : 'escape',
	 r'ESC' : 'esc',
	 r'END' : 'end',
	 r'SPACE' : 'space',
	 r'TAB' : 'tab',
	 r'PRINTSCREEN' : 'print',
	 r'ENTER' : 'enter',
	 r'UPARROW' : 'up',
	 r'UP' : 'up',
	 r'DOWNARROW' : 'down',
	 r'DOWN' : 'down',
	 r'LEFTARROW' : 'left',
	 r'LEFT' : 'left',
	 r'RIGHTARROW' : 'right',
	 r'RIGHT' : 'right',
	 r'CAPSLOCK' : 'capslock',
	 r'F1' : 'f1',
	 r'F2' : 'f2',
	 r'F3' : 'f3',
	 r'F4' : 'f4',
	 r'F5' : 'f5',
	 r'F6' : 'f6',
	 r'F7' : 'f7',
	 r'F8' : 'f8',
	 r'F9' : 'f9',
	 r'F10' : 'f10',
	 r'DELETE' : 'delete',
	 r'INSERT' : 'insert',
	 r'DELAY' : 'sleep',
	 r'DEFAULT_DELAY' : '"',
	 r'REPEAT' : '"'}
    

	# For general keyboard commands
	prefix = "print '''"
	suffix = " | hid-keyboard /dev/hidg0 keyboard'''"

	# Process input text
	prefixinput = "print '''echo -ne "
	prefixoutput = " > /dev/hidg0 '''"

	with infile as text:
		new_text = duckyRules(text.read())
		infile.close()

	# Write regex to tmp file
	with tmpfile as result:
		result.write(new_text)
		tmpfile.close()

	src = open('tmp.txt', 'r')
	dest = open('output.txt', 'w')
	for line in src:

		if line.startswith('sleep'):
			line = line.split()
			seconds = (Decimal(line[1]) / Decimal(1000)) % 60
			line[1] = str(seconds)
			line = ' '.join(line)
			dest.write('%s%s%s\n' % (prefix, line.rstrip('\n').strip(), suffix))

		elif line.startswith('REM'):
			line = '#' + line.rstrip('\n').strip('REM')
			dest.write('%s\n' % line.rstrip('\n').strip())

		elif line.startswith('STRING'):
			line = line.strip('STRING ')
			for char in line:
				
				if args.layout=="us" : line = dict_us[char]
				elif args.layout=="fr" : line = dict_fr[char]
				elif args.layout=="de" : line = dict_de[char]
				elif args.layout=="es" : line = dict_es[char]
				elif args.layout=="sv" : line = dict_sv[char]
				elif args.layout=="it" : line = dict_it[char]
				elif args.layout=="uk" : line = dict_uk[char]
				elif args.layout=="ru" : line = dict_ru[iso_ru[char]]
				elif args.layout=="dk" : line = dict_dk[char]
				elif args.layout=="no" : line = dict_no[char]
				elif args.layout=="pt" : line = dict_pt[char]
				elif args.layout=="be" : line = dict_be[char]
				
				dest.write('%s%s%s\n' % (prefixinput, line.rstrip('\n').strip(), prefixoutput))

		else:
			dest.write('%s%s%s\n' % (prefix, line.rstrip('\n').strip(), suffix))

	print "File saved to output.txt"