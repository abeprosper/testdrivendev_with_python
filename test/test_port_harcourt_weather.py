import unittest
from app.port_harcourt_weather import SmallestTemperatureSpread #import the class from target python application

class TddSmallestTemperatureSpread(unittest.TestCase):

	def setUp(self):
		self.inputFilename = SmallestTemperatureSpread()
		pass

	def test__return_inputFileIntegrity(self):
		inputFilename = SmallestTemperatureSpread()
		result = inputFilename.confirmFileIntergrity('port-harcourt-weather.txt')
		self.assertEqual('port-harcourt-weather.txt', result)
		pass

	def test__return_exception_if_file_extension_not_txt(self):
		self.assertRaises(ValueError, self.inputFilename.confirmFileIntergrity, 'port-harcourt-weather')
		pass

	def test__return_error_if_resultfile_empty(self): # touch zerofile-port-harcourt-weather.txt
		self.assertRaises(ValueError, self.inputFilename.confirmFileIntergrity, 'zerofile-port-harcourt-weather.txt')
		pass

	def test__return_error_if_resultfile_iteration_can_not_produce_dailyList_list(self):
		inputFilename = SmallestTemperatureSpread()
		dailyList = inputFilename.weatherLists('port-harcourt-weather.txt')
		dailyList = list(dailyList) # I have a tuple here, i.e multiple return items from my method
		self.assertIsInstance(dailyList, list)
		pass

	def test__return_error_if_resultfile_iteration_can_not_produce_dailyTempSpread_list(self):
		inputFilename = SmallestTemperatureSpread()
		dailyList, dailyTempSpread = inputFilename.weatherLists('port-harcourt-weather.txt')
		dailyTempSpread = list(dailyTempSpread) # I have a tuple here, i.e multiple return items
		self.assertIsInstance(dailyTempSpread, list)
		pass