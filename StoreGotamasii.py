#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  StoreYuhun.py
#  
#  Copyright 2017 Bear Young <bear@ulaptop>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


class Yuhun(object):
	def __init__(self, name, level=6, position=0, mainProperty={}, viceProperty={}):
		self.__name = name
		self.__level = level
		self.__position = position
		self.__mainProperty = mainProperty	
		self.__viceProperty = viceProperty
	
	def set_name(self, name):
		self.__name = name
	
	def get_name(self):
		return self.__name
	
	def get_level(self):
		return self.__level
	
	def get_position(self):
		return self.__position
	
	def get_mainProperty(self):
		return self.__mainProperty
	
	def get_viceProperty(self):
		return self.__viceProperty
		
	def write2file(self):
		cl = '\n'
		with open("yuhun.txt", 'a') as f:
			f.write("Name:" + self.__name + cl)
			f.write("Level:" + str(self.__level) + cl)
			f.write("Position:" + str(self.__position) + cl)
			f.write("Main Property:" + str(self.__mainProperty) + cl)
			f.write("Vice Property:" + str(self.__viceProperty) + cl)

class Properties(object):
	properties = ["Attack incValue", "Attack incRate", \
				"Life incValue", "Life incRate", \
				"Defence incValue", "Defence incRate", \
				"Speed incValue", \
				"CDR", "CD", \
				"Effect incRate", "Resist incRate"]
	
	mainProperties = {1:["Attack incValue"], \
						2:["Attack incRate", "Life incRate", "Defence incRate", "Speed incValue"], \
						3:["Defence incValue"], \
						4:["Attack incRate", "Life incRate", "Defence incRate", "Effect incRate", "Resist incRate"], \
						5:["Life incValue"], \
						6:["Attack incRate", "Life incRate", "Defence incRate", "CDR", "CD"]}
					
'''
		def get_properties(self):
			return self.__properties
		
		def get_mainProperties(self):
			return self.__mainProperties
'''

def store_yuhun(n=0):
	t = n
	finished = False
	
	while(not(finished)):
		print("Yuhun Name:")
		name = input()
		while(True):
			print("Level:")
			level = int(input())
			if level in (list(range(1, 7))): break
		while(True):
			print("Position")
			position = int(input())
			if position in (list(range(1, 7))): break
		while(True):
			prper4show = Properties.mainProperties[position]
			prperLen = len(prper4show)
			print_list_with_order_number(prper4show)
			mainProperty = int(input())
			if mainProperty in (list(range(1,prperLen+1))): break
		if n <= 0:
			while(True):
				print("Continue?(Yes/No)")
				goon = input().upper()
				if goon in ("YES", "NO"): break
			if goon == "NO": finished = True
		else:
			t -= 1
			if t == 0: finished = True
	
def print_list_with_order_number(l, sequence='head', dot='.'):
	n = 0
	str4show = ""
	for i in l:
		n += 1
		if sequence == "head":
			str4show += str(n) + dot + i
		else:
			str4show += i + dot + str(n)
		str4show += "\t"		
	print(str4show)
		

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    
    store_yuhun(0)
    
