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
				try: #Mosudi: attempt to extract my relevant data, namely cols: 1,2 & 3
					dayNum = int(line[0]) #Mosudi: avoid the last row starting with string "mo", even if the month is 31
					dailyHigh = int(line[1]) #Mosudi: second col
					dailyLow = int(line[2])	  #Mosudi: third col
				except ValueError:
					pass
				dailyList.append(dayNum), dailyHighList.append(dailyHigh), dailyLowList.append(dailyLow), dailyTempSpread.append(dailyHigh - dailyLow)
		weatherDict = dict(zip(dailyList, dailyTempSpread)) #Mosudi: Creating Dictionary
		smallestTemperatureSpread = min(sorted(weatherDict.values()))
		smallestTemperatureSpreadDay = min(weatherDict, key=weatherDict.get) #Mosudi: Iterate over the dictionary to get the key(day number) of min value(temp spread)
		return dailyList , dailyTempSpread, weatherDict, smallestTemperatureSpread, smallestTemperatureSpreadDay
		pass



class LeastGoalPerformer(object):
	filename = 'football-league-results.txt'

	def confirmFileIntergrity(self, filename):
		if  filename.endswith('.txt') and os.path.isfile(filename) and os.stat(filename).st_size > 0:
			return filename 
		else:
			raise ValueError
		pass

	def leagueClubNameList(self, filename):
		with open(filename) as leagueResult:
			goalDifList = []	#Mosudi: Initialise list for league team goal difference
			leagueClubNameList = []	#Mosudi: Initialise list for league team
			leagueResult.next() #Mosudi : Skiiping the 1st lines from the iteration procedure.
			for line in leagueResult: #Mosudi: Iterating over  each line.
				teamDataList = [] #Mosudi: Initialise list to collate data for each team. 
				leagueClubName = [] #Mosudi: Initialise list to collate each team name per line.
				line = line.split() #Mosudi: Making list out of "words" seperated by white space on each line.
				for leagueData in line: #Mosudi: Iterate life for each line for club names(string) and data(int)
					try:
						leagueData = int(leagueData) #Mosudi: League data
						teamDataList.append(leagueData) #Mosudi:
					except ValueError:
						leagueClub = str(leagueData) #Mosudi: League club names
						if leagueClub != '-': leagueClubName.append(leagueClub) #Mosudi: Append to list in bid to extract club names, while removing the lines with several "-"
						pass
				#print teamDataList, leagueClubName
				if len(teamDataList) > 0 : #Mosudi: Iteration over the two lists(teamDataList and leagueClubList) while skipping empty lists create out of blank line
					del leagueClubName[:1] #Mosudi: Removing Serial numbers from the team names
					goalFor = int(teamDataList[4]) #Mosudi: Extracting target data: Goal For
					goalAgainst = int(teamDataList[5]) #Mosudi: Extracting target data: Goal Against
					goalDifList.append(goalFor - goalAgainst) #Mosudi: Add goal difference to goalDifList			#print leagueClubNameList
					leagueClubName = ' '.join(leagueClubName) #Mosudi: Creating club name for each line
					leagueClubNameList.append(leagueClubName) #Mosudi: Add club name to leagueClubNameList
			goalPerformance = dict(zip(leagueClubNameList, goalDifList)) #Mosudi: Create a dictionary of club name and corresponding goal difference
			LeastGoalDiff = min(sorted(goalPerformance.values()))			#Mosudi: Manipulation the dictionary for minimum vale
			LeastGoalDiffTeamName = min(goalPerformance, key=goalPerformance.get)			#Mosudi: Manipulation the dictionary for minimum vale
			return leagueClubNameList, goalDifList, goalPerformance, LeastGoalDiff, LeastGoalDiffTeamName
		pass