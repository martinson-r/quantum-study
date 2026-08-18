from qiskit import QuantumCircuit

circuit = QuantumCircuit(1, 1)

circuit.h(0)
circuit.measure(0, 0)

print(circuit)