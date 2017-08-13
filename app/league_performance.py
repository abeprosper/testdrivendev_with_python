import os


class LeastGoalPerformer(object):
	filename = 'football-league-results.txt'

	def confirmFileIntergrity(self, filename):
		if os.path.isfile(filename):
			return filename
		pass
		