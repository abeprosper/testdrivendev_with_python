
filename = 'football-league-results.txt'
def leageGoalPerformance(filename):
	with open(filename) as leagueResult:
		leagueClubNameList = []
		goalDifList = []
		leagueResult.next()  #Mosudi : Skiiping the 1st lines from the iteration procedure.
		for line in leagueResult: #Mosudi: Iterating over  each line.
			teamDataList = []     #Mosudi: Initialise list to collate data for each team. 
			leagueClubName = []   #Mosudi: Initialise list to collate team names.
			#line.strip()
			line = line.split()   #Mosudi: Making list out of "words" seperated by white space on each line.
			for leagueData in line: #Mosudi: Iterate life for each line for club names(string) and data(int) 
				try:
					leagueData = int(leagueData) #Mosudi: League data
					teamDataList.append(leagueData) #Mosudi: 
				except ValueError:
					leagueClub = str(leagueData) #Mosudi: League club names
					if leagueClub != '-': leagueClubName.append(leagueClub) #Mosudi: Append to list in bid to extract club names, while removing the lines with several "-"
					pass													
			#print len(teamDataList)
			if len(teamDataList) > 0 : #Mosudi: Iteration over the two lists(teamDataList and leagueClubList) while skipping empty lists create out of blank line
				#print len(teamDataList) 
				goalFor = int(teamDataList[4]) #Mosudi: Extracting target data: Goal For
				goalAgainst = int(teamDataList[5]) #Mosudi: Extracting target data: Goal Against
				del leagueClubName[:1] #Mosudi: Removing Serial numbers from 
				leagueClubName = ' '.join(leagueClubName) #Mosudi: Creating club name for each line
				leagueClubNameList.append(leagueClubName) #Mosudi: Add club name to leagueClubNameList
				goalDifList.append(goalFor - goalAgainst) #Mosudi: Add goal difference to goalDifList

	goalPerformance = dict(zip(leagueClubNameList, goalDifList)) #Mosudi: Create a dictionary of club name and corresponding goal difference			
	minPerf = min(goalPerformance, key=goalPerformance.get)
	LowestDif = min(sorted(goalPerformance.values()))
	#print goalPerformance
	#print minPerf
	#print LowestDif
	print " The team with the smallest difference in for and against goals is " + minPerf + ", with a goal difference of  " + str(LowestDif)

leageGoalPerformance(filename)