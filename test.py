import unittest
from login import emailLogin

testcase = unittest.TestLoader().loadTestsFromTestCase(emailLogin)
testcase.run()


if __name__ == '__main__':
    reportFoler = "Report"
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output=reportFoler, title='Test report', open_in_browser=True))
