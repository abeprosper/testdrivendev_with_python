import os


class LeastGoalPerformer(object):
	filename = 'football-league-results.txt'

	def confirmFileIntergrity(self, filename):
		if  filename.endswith('.txt') and os.path.isfile(filename):
			with open(filename) as datafile:
				first = datafile.read(1)
				if first:
					return filename
				else:
					raise ValueError
		else:
			raise ValueError
		pass
		