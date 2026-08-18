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

## Learning Plan
### 2026-08-18 — Qiskit basics + math refresh
Goal: Understand what Qiskit is, refresh only the math needed to follow basic quantum concepts, and be able to explain the first circuit in my own words.

1. Watch "What is Qiskit?" video

[x] Done when: I can explain Qiskit in 2–3 sentences.

2. Math refresher — 15–20 minutes

[ ] Done when: I either complete one small lesson/exercise set OR identify the exact prerequisite I need next.

3. Open hello_quantum.py. Add code notation for each line, explaining what it does.

[x] Done when: I can explain the circuit without looking up the explanation.

------------

## Math refresh

I graduated college a long time ago and remember substantially less algebra than quantum computing requires.

Current refresh work - Khan Academy:
- Pre-algebra
- Algebra 1
- Algebra 2
- College Algebra (select topics)
- Linear Algebra

Khan Academy progress: https://www.khanacademy.org/profile/martinsonr/progress

The goal is not course completion but to relearn the math needed to understand the quantum concepts explored in this repo.