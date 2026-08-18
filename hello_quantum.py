from qiskit import QuantumCircuit

# This script constructs a Qiskit QuantumCircuit object: a software description of a quantum circuit.
# It does not yet execute the circuit on a simulator or real quantum hardware.
# it's like printing an electrical schematic or a flowchart
# so this is the "instructions" stage

circuit = QuantumCircuit(1, 1)
# I understand I am now creating a circuit by passing parameters into QuantumCircuit which looks like a... class? So now circuit is an object created from QuantumCircuit.

# In this particular constructor call, the two positional integers mean:
# QuantumCircuit(number_of_qubits, number_of_classical_bits)
# so create 1 qubit and create 1 classical bit

# IBM’s current docs describe a quantum circuit as having quantum bits plus classical bits/registers for ordinary classical data (need citation)

# that's what the 2 horizontal lines in the printed diagram represent
# q: ──H──M──
#        │
# c: ────╫──
#        0

# The q line belongs to the qubit

# The c line belongs to the classical bit where we are going to store the measurement

# IMPORTANT: you don’t always need classical bits
# circuit = QuantumCircuit(1) creates a circuit with one qubit and no classical bits. That’s valid if you’re just building quantum operations and aren’t measuring into classical storage yet.

circuit.h(0)

# Apply the H gate to logical qubit 0 (the qubit at index 0)
# the 0 is "array-like" in the programming sense
# Qiskit exposes qubits as an ordered, list-like collection, so 0 means "the first logical qubit in this circuit."
# This is a logical circuit index, not necessarily a specific physical qubit on quantum hardware.

# H is reversible and is its own inverse:
# applying H twice returns the qubit to its original state.

# If we measure after the first H, however, we no longer have the same
# pre-measurement quantum state to reverse.
# Measurement produces a classical outcome, 0 or 1.

circuit.measure(0, 0)
# peek in the box; measurement changes the quantum state, so we can no longer simply apply H again to recover the pre-measurement state

print(circuit)
# this line asks Qiskit to render the QuantumCircuit object as ASCII art
# print(circuit) displays the circuit diagram but it does not execute the circuit.


# Other Notes:

# H(H|0⟩) = |0⟩
# Applying H twice returns |0⟩ to its original state.
# H is its own inverse.

# A qubit state can be represented as a vector.
# The H gate can be represented as a matrix.
# Applying H to a qubit means multiplying the H matrix by the qubit-state vector.

# I do not fully understand this yet because I need a linear algebra refresher.
# Current goal: understand vectors, matrices, and matrix × vector multiplication well enough
# to understand what H is doing mathematically.