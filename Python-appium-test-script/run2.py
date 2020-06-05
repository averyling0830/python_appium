import os, HtmlTestRunner

from script import GA_AutoLoginTest

op = os.path.abspath('./result')
runner = HtmlTestRunner.HTMLTestRunner(
    output = op,
)
runner.run(GA_AutoLoginTest.suite())
