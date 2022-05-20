import unittest
from TestSuites.GeneralSuite import GeneralTestSuites

class RunClass():
    def run(self, suite):
        runner = unittest.TextTestRunner()
        runner.run(suite)


if __name__ == "__main__":
    runner = RunClass()
    suite = GeneralTestSuites.GeneralSuiteClass()
    runner.run(suite.generate_suite())
