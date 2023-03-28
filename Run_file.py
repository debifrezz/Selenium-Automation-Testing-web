import unittest
import os
import Req
import Login
import profil
import Sell
import HTMLRunner

direct = os.getcwd()

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):

        Smoke_Testing = unittest.TestSuite()
        Smoke_Testing.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Req.Req1),
            unittest.defaultTestLoader.loadTestsFromTestCase(Req.Req2),
            unittest.defaultTestLoader.loadTestsFromTestCase(Req.Req3),
            unittest.defaultTestLoader.loadTestsFromTestCase(Login.Log1),
            unittest.defaultTestLoader.loadTestsFromTestCase(Login.Log2),
            unittest.defaultTestLoader.loadTestsFromTestCase(Login.Log3),
            unittest.defaultTestLoader.loadTestsFromTestCase(profil.prof),
            unittest.defaultTestLoader.loadTestsFromTestCase(Sell.sell1),
            unittest.defaultTestLoader.loadTestsFromTestCase(Sell.sell2),
            unittest.defaultTestLoader.loadTestsFromTestCase(Sell.sell3)
        ])

        outfile = open(direct + "\Smoke_Testing1.html", "w")

        runner1 = HTMLRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description='testing'
        )

        runner1.run(Smoke_Testing)





if __name__ == '__main__':
    unittest.main()