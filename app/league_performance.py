import os


class LeastGoalPerformer(object):
	filename = 'football-league-results.txt'

	def confirmFileIntergrity(self, filename):
		if  filename.endswith('.txt') and os.path.isfile(filename) and os.stat(filename).st_size > 0:
			return filename
		else:
			raise ValueError
		pass
		