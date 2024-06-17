from .quantum_computing import QuantumAlgorithm
from .ai_algorithms import AIAlgorithm

class HybridSystem:
    def __init__(self):
        self.quantum_algo = QuantumAlgorithm()
        self.ai_algo = AIAlgorithm()

    def execute(self):
        quantum_result = self.quantum_algo.run()
        ai_result = self.ai_algo.train()
        return {
            "quantum_result": quantum_result,
            "ai_result": ai_result
        }