from qiskit import QuantumCircuit, Aer, transpile, assemble

class QuantumAlgorithm:
    def __init__(self):
        self.circuit = QuantumCircuit(2)

    def run(self):
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.circuit.measure_all()

        simulator = Aer.get_backend('qasm_simulator')
        compiled_circuit = transpile(self.circuit, simulator)
        qobj = assemble(compiled_circuit)
        result = simulator.run(qobj).result()
        counts = result.get_counts(self.circuit)
        return counts