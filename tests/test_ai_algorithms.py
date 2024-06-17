import unittest
from quantumai.ai_algorithms import AIAlgorithm

class TestAIAlgorithm(unittest.TestCase):
    def test_train(self):
        ai_algo = AIAlgorithm()
        accuracy = ai_algo.train()
        self.assertIsInstance(accuracy, float)
        self.assertGreater(accuracy, 0.5)

if __name__ == '__main__':
    unittest.main()