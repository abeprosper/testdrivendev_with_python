import os


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
					leagueClubName = ' '.join(leagueClubName) #Mosudi: Creating club name for each line
					leagueClubNameList.append(leagueClubName) #Mosudi: Add club name to leagueClubNameList
			#print leagueClubNameList
			return leagueClubNameList
		pass

	def goalDifList(self, filename):
		with open(filename) as leagueResult:
			goalDifList = []	#Mosudi: Initialise list for league team goal difference
			leagueResult.next() #Mosudi : Skiiping the 1st lines from the iteration procedure.
			for line in leagueResult: #Mosudi: Iterating over  each line.
				teamDataList = [] #Mosudi: Initialise list to collate data for each team. 
				line = line.split() #Mosudi: Making list out of "words" seperated by white space on each line.
				for leagueData in line: #Mosudi: Iterate life for each line for club names(string) and data(int)
					try:
						leagueData = int(leagueData) #Mosudi: League data
						teamDataList.append(leagueData) #Mosudi:
					except ValueError:
						pass
				if len(teamDataList) > 0 : #Mosudi: Iteration over the two lists(teamDataList and leagueClubList) while skipping empty lists create out of blank line
					goalFor = int(teamDataList[4]) #Mosudi: Extracting target data: Goal For
					goalAgainst = int(teamDataList[5]) #Mosudi: Extracting target data: Goal Against
					goalDifList.append(goalFor - goalAgainst) #Mosudi: Add goal difference to goalDifList			#print leagueClubNameList
			#print goalDifList
			return goalDifList
		pass

	