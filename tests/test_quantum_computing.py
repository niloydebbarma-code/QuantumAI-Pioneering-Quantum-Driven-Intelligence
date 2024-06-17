import unittest
from quantumai.quantum_computing import QuantumAlgorithm

class TestQuantumAlgorithm(unittest.TestCase):
    def test_run(self):
        quantum_algo = QuantumAlgorithm()
        result = quantum_algo.run()
        self.assertIsInstance(result, dict)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()