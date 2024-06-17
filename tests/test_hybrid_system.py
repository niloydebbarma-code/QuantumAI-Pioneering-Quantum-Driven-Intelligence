import unittest
from quantumai.hybrid_system import HybridSystem

class TestHybridSystem(unittest.TestCase):
    def test_execute(self):
        hybrid_system = HybridSystem()
        result = hybrid_system.execute()
        self.assertIn('quantum_result', result)
        self.assertIn('ai_result', result)

if __name__ == '__main__':
    unittest.main()