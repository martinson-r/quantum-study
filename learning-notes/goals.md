# Ultimate Goals

I am **not** trying to become a quantum physicist.

My goal is to become technically competent enough to design, build, and evaluate useful UX for quantum computing tools without hand-waving past the underlying concepts.

## 1. Build a reliable working understanding of quantum computing

I want to understand the core computational model well enough that I know what the software is actually representing.

This includes:

* qubits
* quantum states
* gates
* measurement
* superposition
* entanglement
* quantum circuits
* basis states and basis changes
* amplitudes and probabilities
* the role of linear algebra
* how quantum programs are executed on simulators and real hardware

I do not need to derive every theorem from first principles, but I do want to understand the mathematics behind the operations I expose in an interface.

## 2. Learn enough math to reason correctly

The objective is not to become a mathematician or complete every prerequisite course.

I want enough mathematical fluency to understand the concepts I am designing around.

Primary areas:

* vectors
* vector spaces
* normalization and norms
* matrices
* matrix-vector multiplication
* linear transformations
* basis and change of basis
* complex numbers
* probability
* algebra needed to support the above

Linear algebra will be the main path because it maps more naturally to my background in coding and animation.

When missing algebra skills become a blocker, I will patch those skills as needed and return to the problem that required them.

The path through the prerequisites may therefore be, regrettably, non-linear.

## 3. Distinguish intuition from formal understanding

Useful mental models are not the same thing as complete explanations.

For concepts I study, I want to distinguish between:

* **Current intuition** — the model I currently use to reason about the concept
* **Formal understanding** — what the mathematics and underlying system actually say
* **Open questions / caveats** — where my understanding is incomplete or where the intuition stops being accurate

I do not want to mistake familiarity with terminology for understanding.

## 4. Understand where simplifications break

Before designing an educational visualization or abstraction around a quantum concept, I should be able to answer:

* What is this representation simplifying?
* What does it represent accurately?
* Where does it become misleading?
* What assumptions does it make?
* What would an expert object to?

A visualization can be useful without being literally complete, but I should know the boundary.

## 5. Become competent with real quantum-development tools

I want practical experience with the tools people actually use.

Initial focus:

* Qiskit
* quantum circuits
* local simulation
* executing circuits on quantum hardware
* interpreting results
* debugging quantum programs
* reading SDK documentation
* understanding common quantum-development workflows

Later, I may compare Qiskit with other frameworks where useful.

## 6. Investigate quantum computing as a UX problem

My eventual focus is not simply writing quantum programs.

I want to study where existing quantum-development tools create problems for humans.

Areas of interest include:

* circuit visualization
* debugging
* state visualization
* measurement and probability displays
* error communication
* hardware constraints
* explaining transformations
* helping developers understand what their circuit is doing
* making difficult concepts inspectable without making them incorrect
* workflows for people who understand software better than physics
* accessibility in highly technical interfaces

## 7. Build tools, not just complete courses

Courses and tutorials are resources, not the final product.

The primary evidence of progress should eventually be:

* GitHub commits
* experiments
* prototypes
* visualizations
* technical notes
* UX analyses
* small Qiskit tools
* interactive explainers
* portfolio case studies

The preferred cycle is:

**learn → experiment → build → document → correct → build again**

rather than:

**learn → learn → learn → maybe someday build**

## 8. Keep a public record of how the understanding develops

The notebook and commit history are part of the project.

They should preserve:

* early questions
* incorrect assumptions
* corrections
* math refreshers
* useful resources
* experiments
* changes in understanding
* unresolved questions
* design implications

The goal is not to pretend I began with expertise.

If I eventually produce useful quantum UX work, someone with real domain expertise should be able to trace the work backward and evaluate whether I understood the concepts well enough to make the design decisions I made.

## 9. Know when expert validation is necessary

I do not need to independently possess every piece of domain knowledge relevant to every project.

I do need enough understanding to recognize when I am operating beyond my depth.

For technically sensitive work, I should be able to collaborate with physicists, quantum developers, researchers, or other domain experts and understand their feedback well enough to incorporate it correctly.

Expert review is part of responsible design, not evidence that I failed to learn enough.

## 10. Ultimate target

The target is:

> **Working knowledge deep enough to reason correctly about quantum computing systems, build with the actual tools, identify misleading abstractions, and design interfaces that domain experts can trust enough to use or evaluate seriously.**

I do not need to become a quantum physicist.

I need to become a technically literate UX engineer working in quantum computing who knows both what I understand and where the boundaries of that understanding are.
