import unittest
import tests_12_3

runnerTS = unittest.TestSuite()
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

TextTestRunner = unittest.TextTestRunner(verbosity=2)
TextTestRunner.run(runnerTS)
