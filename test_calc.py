import unittest
import calc


class TestCase(unittest.TestCase):
    def test_sum1(self):
        self.assertEqual(calc.add(5,4),9)
    def test_sum2(self):
        self.assertEqual(calc.add(5,-4),1)
    def test_sum3(self):
        self.assertEqual(calc.sub(5,4),1)
    def test_sum4(self):
        self.assertEqual(calc.sub(0,-4),4)
    def test_sum5(self):
        self.assertEqual(calc.mul(5,0),0)
    def test_sum6(self):
        self.assertEqual(calc.mul(50,-4),-200)
    def test_sum7(self):
        self.assertEqual(calc.div(5,2),2.5)
    def test_sum8(self):
        self.assertEqual(calc.div(5,0),None)
if __name__ == "__main__":
    unittest.main(verbosity=2)
