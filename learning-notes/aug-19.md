# 08/19

ok so I understand that |0⟩ and |1⟩ are two states for the qubit. 

|0⟩ has vector representation of [1,0] |1⟩ has a vector representation of [0,1] 

- But why is a qubit represented by a vector in 2 dimensional space?


Because a single qubit has two basis states you need to describe relative to: |0⟩ and |1⟩.

So its state needs two components.

You can write a general qubit state as:

[

a

b

]

(I'm not coding the notation properly, live with it)

where a tells you “how much of |0⟩” and b tells you “how much of |1⟩.”
(a and b are amplitudes associated with the |0⟩ and |1⟩ basis states. They are not probabilities directly.)

That’s why:

∣0⟩=
[
1
0
]

means “100% aligned with the |0⟩ basis state, 0% with |1⟩,” while:

∣1⟩=
[
0
1
]

means the opposite.


- This is not ordinary physical 2D space like x/y coordinates on a screen. It’s an abstract 2D vector space whose two axes are basically:

axis 1 = |0⟩
axis 2 = |1⟩

So conceptually, think:

state = [amount of |0⟩, amount of |1⟩]

- H takes [1, 0] and and transforms it into a state with both components present
when you add a second qubit, the space becomes 4-dimensional, not 2-dimensional, because there are four basis states:

|00⟩
|01⟩
|10⟩
|11⟩

So n qubits have 2ⁿ-dimensional state space

- A general qubit state can be thought of as a point/vector in this abstract 2D state space, but its coordinates must satisfy a normalization rule.
- the qubit-state vector has to stay normalized — its total “length” has to remain 1.

### Why does the H gate use `1/√2`?

For a 2D vector, its length (also called its **magnitude** or **norm**) is calculated using the Pythagorean theorem.

For a vector:

$$
[a, b]
$$

its length is:

$$
\sqrt{a^2 + b^2}
$$

For example, the vector:

$$
[3, 4]
$$

has length:

$$
\sqrt{3^2 + 4^2}
=
\sqrt{9 + 16}
=
\sqrt{25}
=
5
$$

A valid qubit state must have a total vector length of `1`. This is called being **normalized**.

After applying the H gate to $|0\rangle$, we want the two components of the state vector to be equal, because the resulting measurement probabilities for `0` and `1` should be equal.

So imagine the resulting vector is:

$$
[a, a]
$$

Its length would be:

$$
\sqrt{a^2 + a^2}
$$

Because a qubit state must have length `1`:

$$
\sqrt{a^2 + a^2} = 1
$$

Combine the two equal terms:

$$
\sqrt{2a^2} = 1
$$

Square both sides:

$$
2a^2 = 1
$$

Divide by 2:

$$
a^2 = \frac{1}{2}
$$

Take the square root:

$$
a = \frac{1}{\sqrt{2}}
$$

So the H gate transforms:

$$
|0\rangle
=
[1,0]
$$

into:

$$
\left[
\frac{1}{\sqrt{2}},
\frac{1}{\sqrt{2}}
\right]
$$

The `1/√2` is therefore not arbitrary.

It is the number that lets both components be equal while keeping the whole vector's length equal to `1`.

Later, when the qubit is measured, the probability of each outcome comes from squaring the magnitude of the corresponding component:

$$
\left(\frac{1}{\sqrt{2}}\right)^2
=
\frac{1}{2}
$$

So the measurement probabilities are:

- `0`: 50%
- `1`: 50%
