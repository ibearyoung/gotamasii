#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  WearingYuhun.py
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

class YuhunProperties(object):
	maxViceProperties = 4
	location = 6
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
	
class Assistant(object):
	def __init__(self, name, attack=1000, life=2000, defence=200, speed=110, cdr=0.1, cd=1.5):
		self.__name = name
		self.__attack = attack
		self.__life = life
		self.__defence = defence
		self.__speed = speed
		self.__cdr = cdr
		self.__cd = cd
		
	def set_name(self, name):
		self.__name = name
	
	def get_name(self):
		return self.__name
	
	
class Yuhun(object):
	fileName = "yuhun.txt"
	
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
		with open(self.fileName, 'a') as f:
			f.write("Name:" + self.__name + cl)
			f.write("Level:" + str(self.__level) + cl)
			f.write("Position:" + str(self.__position) + cl)
			for k in self.__mainProperty:
				f.write(k + ":" + str(self.__mainProperty[k]) + cl)
			for k in self.__viceProperty:
				f.write(k + ":" + str(self.__viceProperty[k]) + cl)
			f.write(cl)
	
	@classmethod
	def gather_info(cls, n=0):
		t = n
		no = 0
		finished = False
		tMPrper = {}
		tVPrper = {}
		
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
				print("Main Property:")
				prper4show = YuhunProperties.mainProperties[position]
				prperLen = len(prper4show)
				print_list_with_order_number(prper4show)
				mainProperty = int(input())
				if mainProperty in (list(range(1, prperLen+1))):
					while(True):
						mainValue = float(input("Value:"))
						if mainValue > 0: break
					break
			tMPrper[YuhunProperties.mainProperties[position][mainProperty-1]] = mainValue
			
			tv = 1
			goon = ""
			tvno = 0
			while(tv <= YuhunProperties.maxViceProperties):
				tvno += 1
				print("Vice Property %s#:" % (tvno))
				prper4show = YuhunProperties.properties
				prperLen = len(prper4show)
				print_list_with_order_number(prper4show)
				viceProperty = int(input())
				viceValue = 0
				if viceProperty in (list(range(1, prperLen+1))):
					while(True):
						viceValue = float(input("Value:"))
						if viceValue > 0: break
				tVPrper[YuhunProperties.properties[viceProperty-1]] = viceValue
				while(True):
					goon = input("Vice Property completed?(Yes/No)").upper()
					if goon in ("YES", "NO"): break
				if goon == "YES": break
			
			tYH = cls(name, level, position, tMPrper, tVPrper)
			tYH.write2file()
			no += 1
			print("No. %s:%s Saved!" % (no, tYH.get_name()))
			
			goon = ""
			if n <= 0:
				while(True):
					print("Continue?(Yes/No)")
					goon = input().upper()
					if goon in ("YES", "NO"): break
				if goon == "NO": finished = True
			else:
				t -= 1
				if t == 0: finished = True
		
	
def store_assistant(n=0):
	pass
	
def main(args):
    return 0

if __name__ == '__main__':
	import sys
	
	Yuhun.gather_info()
	
	#a = Assistant()
	#a.set_name("WhiteWolf")
	#y = Yuhun("Needle Woman", 6, 1, {"Attack" : 98}, {"Speed" : 10, "Attack Inc": 0.03})
	
	#print(y)
	#y.write2file()
	#store_yuhun(3)
	
	
	
    
