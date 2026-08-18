# Quantum Computing Notebook

## Resources

### Communities
- Qiskit Slack
- Quantum Computing Stack Exchange
- Qiskit GitHub
- [Qiskit YouTube](https://www.youtube.com/@qiskit)

### Documentation
- [Qiskit docs](https://quantum.cloud.ibm.com/)

### Courses and Tutorials
- [Khan Academy Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
- [IBM Courses](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information)

---

## Concepts

### Qubit
A quantum unit of information.

### Gate
An operation that changes a qubit's state.

### Measurement
Turns the quantum state into a classical result.

### Hadamard gate
TODO: understand this better than "poke the cat."

---

## Experiments

### 2026-08-17 — First circuit

```python
circuit = QuantumCircuit(1, 1)
circuit.h(0)
circuit.measure(0, 0)
```

#### Current understanding:

1. one qubit
1. apply a Hadamard gate
1. measure it
1. store the result in a classical bit


#### Questions to Explore
1. What exactly does the Hadamard gate do?
1. What does “state” mean mathematically?
1. Why does measurement produce 0 or 1?
1. How do I run the circuit many times?
