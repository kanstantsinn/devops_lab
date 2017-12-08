import unittest
import t6 



class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_json(self):
        self.assertEqual( t6.version, "Python 3.5.4")
 
if __name__ == '__main__':
    unittest.main()
