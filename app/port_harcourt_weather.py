import os
class SmallestTemperatureSpread(object):
	"""docstring for SmallestTemperatureSpread"""

	filename = 'port-harcourt-weather.txt'


	def confirmFileIntergrity(self, filename):
		if filename.endswith('.txt') and os.path.isfile(filename):
			return filename
		else:
			raise ValueError
		pass



















	'''def __init__(self, arg):
					super(SmallestTemperatureSpread, self).__init__()
					self.arg = arg'''
		