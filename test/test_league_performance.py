import unittest
from app.league_performance import LeastGoalPerformer #import the class from target python application

class TddLeastGoalPerformer(unittest.TestCase):

	def setUp(self):
		self.inputFilename = LeastGoalPerformer()
		pass

	def test__return_inputFileIntegrity(self):
		inputFilename = LeastGoalPerformer()
		result = inputFilename.confirmFileIntergrity('football-league-results.txt')
		self.assertEqual('football-league-results.txt', result)
		pass

	def test__return_exception_if_file_extension_not_txt(self):
		self.assertRaises(ValueError, self.inputFilename.confirmFileIntergrity, 'football-league-results')
		pass

	def test__return_error_if_resultfile_empty(self): # touch zerofile-football-league-result.txt
		self.assertRaises(ValueError, self.inputFilename.confirmFileIntergrity, 'zerofile-football-league-result.txt')
		pass

	def test__return_error_if_resultfile_iteration_can_not_produce_to_team_list(self):
		inputFilename = LeastGoalPerformer()
		leagueClubNameList = inputFilename.leagueClubNameList('football-league-results.txt')
		self.assertIsInstance(leagueClubNameList, list)
		pass

	def test__return_error_if_resultfile_iteration_can_not_produce_to_league_team_goalDifference_list(self):
		inputFilename = LeastGoalPerformer()
		goalDifList = inputFilename.goalDifList('football-league-results.txt')
		self.assertIsInstance(goalDifList, list)
		pass

	def test__confirm_if_resultfile_iteration_can_produce_league_team_Name_and_goalDifference_Dictionary(self):
		inputFilename = LeastGoalPerformer()
		goalPerformance = inputFilename.goalPerformance('football-league-results.txt')
		self.assertIsInstance(goalPerformance, dict)
		pass

	def test__return_LeastGoalDiffTeam(self):
		inputFilename = LeastGoalPerformer()
		leastGoalDiff = inputFilename.LeastGoalDiffTeam('football-league-results.txt')
		# 48  -  57 = -9, for 'El-Kanemi Warriors'
		self.assertEqual(-9, leastGoalDiff)
		pass










if __name__ == '__main__':
    unittest.main()