import os
class SmallestTemperatureSpread(object):
	"""docstring for SmallestTemperatureSpread"""

	filename = 'port-harcourt-weather.txt'


	def confirmFileIntergrity(self, filename):
		if filename.endswith('.txt') and os.path.isfile(filename) and os.stat(filename).st_size > 0:
			return filename
		else:
			raise ValueError
		pass

	def weatherLists(self,filename):
		with open(filename) as phweather:
			dailyList = []		#Mosudi: Initialise list to collate days of the month
			dailyHighList = []	#Mosudi: Initialise list to collate daily high temperature
			dailyLowList = []	#Mosudi: Initialise list to collate low temperature
			dailyTempSpread = []	#Mosudi: Initialise list to collate daily temperature spread
			phweather.next() #Mosudi Skipping the first line
			phweather.next() #Mosudi Skipping the second line#I will later use confirm if list empty
			for line in phweather: #Mosudi: Iterating over  each line
				line.strip()
				dayDailyTempSpread = []
				#print line
				line = line.split() #creating list for each line
				#print line
				try: #attempt to extract my relevant data, namely cols: 1,2 & 3
					dayNum = int(line[0]) #avoid the last row starting with string "mo", even if the month is 31
					dailyHigh = int(line[1])
					dailyLow = int(line[2])
				except ValueError:
					pass
				dailyList.append(dayNum), dailyHighList.append(dailyHigh), dailyLowList.append(dailyLow), dailyTempSpread.append(dailyHigh - dailyLow)
		return dailyList , dailyTempSpread
		pass

















	'''def __init__(self, arg):
					super(SmallestTemperatureSpread, self).__init__()
					self.arg = arg'''
		