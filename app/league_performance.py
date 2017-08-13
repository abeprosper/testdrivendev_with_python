import os


class LeastGoalPerformer(object):
	filename = 'football-league-results.txt'

	def confirmFileIntergrity(self, filename):
		if  filename.endswith('.txt') and os.path.isfile(filename):
			return filename
		else:
			raise ValueError
		pass
		