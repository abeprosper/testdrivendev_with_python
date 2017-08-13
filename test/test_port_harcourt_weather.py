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