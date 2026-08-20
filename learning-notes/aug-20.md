
## Work done today
Mostly Khan Academy, Linear Algebra (unit vectors) with some detours for trigonometry/college algebra/precalc/calc etc. topics or formulas I completely forgot. 
Finished the beginning of Unit 1 (Vectors) for Linear Algebra.


## Notes

Sine and cosine are ratios that describe the shape of a right triangle. That’s the core idea.

Take a right triangle and pick one non-90° angle, call it θ.

Relative to that angle, the sides are:

hypotenuse = the long side
adjacent = the side next to the angle
opposite = the side across from the angle

Then:

cos(θ) = adjacent / hypotenuse

sin(θ) = opposite / hypotenuse
	​
For vectors (calculating components from magnitude and direction):

x = magnitude × cos(θ)

y = magnitude × sin(θ)


## Parametrization

Parametrization is a way of describing points on a line, curve, or other object using a **parameter**.

A common parameter is `t`.

### What `t` is

`t` is basically a **slider value** telling the equation how much of a vector to add.

It is just a number.

For example:

```text
t = 0
t = 0.5
t = 1
t = 2
t = -1
```

Each value of `t` gives a different point.

---

## Important: the starting point and the direction vector are different things

Suppose we have:

$$
\mathbf{r}(t) = (2,3) + t(4,2)
$$

The two ordered pairs are doing different jobs.

### `(2,3)` is the starting point

It tells us:

> Start here.

It does **not** tell us the direction of the line.

### `(4,2)` is the direction vector

It tells us:

> From wherever I currently am, move 4 units right and 2 units up.

The vector `(4,2)` has its own direction and magnitude.

Its angle does **not** need to match the angle from the origin to `(2,3)`.

The starting point and direction vector are independent.

---

## Why this works

A vector can be moved around without changing the vector.

The vector:

$$
(4,2)
$$

means:

> Move 4 in the x direction and 2 in the y direction.

It can be drawn starting at the origin, but it does not have to stay there.

We can conceptually pick it up and place its tail at `(2,3)`.

So:

$$
(2,3) + (4,2) = (6,5)
$$

means:

> Start at `(2,3)`, then move 4 right and 2 up.

---

## What `t` does to the direction vector

In:

$$
(2,3) + t(4,2)
$$

`t` controls how much of `(4,2)` we use.

### `t = 0`

$$
(2,3) + 0(4,2)
$$

The direction vector is multiplied by zero:

$$
(0,0)
$$

so we stay at:

$$
(2,3)
$$

### `t = 1`

$$
(2,3) + 1(4,2)
$$

We use one full copy of the direction vector:

$$
(2,3) + (4,2) = (6,5)
$$

### `t = 2`

$$
(2,3) + 2(4,2)
$$

First scale the vector:

$$
2(4,2) = (8,4)
$$

Then add it:

$$
(2,3) + (8,4) = (10,7)
$$

### `t = 0.5`

$$
(2,3) + 0.5(4,2)
$$

Half the direction vector is:

$$
(2,1)
$$

so:

$$
(2,3) + (2,1) = (4,4)
$$

### `t = -1`

$$
(2,3) - (4,2)
$$

A negative value sends us in the opposite direction:

$$
(-2,1)
$$

---

## General form

A parametrized line is often written:

$$
\mathbf{x} = \mathbf{a} + t\mathbf{v}
$$

where:

* $\mathbf{a}$ = starting point
* $\mathbf{v}$ = direction vector
* $t$ = slider controlling how much of the direction vector to use

So I can read:

$$
\mathbf{x} = \mathbf{a} + t\mathbf{v}
$$

as:

> **Start at `a`. Then move `t` times along vector `v`.**

The direction of the line comes from **`v`**, not from the starting point.

---

## Programming analogy

```js
function pointOnLine(t) {
  return {
    x: 2 + t * 4,
    y: 3 + t * 2
  };
}
```

Here:

* `(2,3)` is effectively the initial position.
* `(4,2)` describes the direction/step.
* `t` is the function argument controlling how much of that step is used.

Examples:

```js
pointOnLine(0)
// { x: 2, y: 3 }

pointOnLine(0.5)
// { x: 4, y: 4 }

pointOnLine(1)
// { x: 6, y: 5 }

pointOnLine(2)
// { x: 10, y: 7 }
```

The key concept:

> **The starting point tells me where the line is. The direction vector tells me which way the line goes. `t` tells me how far along it to travel.**

## Generalizing from a line through the origin to a shifted line
https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/vectors/v/linear-algebra-parametric-representations-of-lines
Khan arrives at that model by first teaching “all scalar multiples of a vector”, then adding the translation vector.

Video becomes worthwhile at timestamp 19:19

## Parametric line through two points

Suppose I have two points in 3D:

$$
\mathbf{p}_1 =
\begin{bmatrix}
-1 \\
2 \\
7
\end{bmatrix}
$$

and

$$
\mathbf{p}_2 =
\begin{bmatrix}
0 \\
3 \\
4
\end{bmatrix}
$$

A line through both points can be described parametrically as:

$$
L =
\left\{
\mathbf{p}_1 + t(\mathbf{p}_1 - \mathbf{p}_2)
\mid t \in \mathbb{R}
\right\}
$$

### What the pieces mean

- $\mathbf{p}_1$ = one point on the line
- $\mathbf{p}_2$ = another point on the line
- $\mathbf{p}_1 - \mathbf{p}_2$ = a direction vector connecting the two points
- `t` = a scalar parameter: basically a slider controlling how much of that direction vector gets added

First calculate the direction vector:

$$
\mathbf{p}_1 - \mathbf{p}_2
=
\begin{bmatrix}
-1 \\
2 \\
7
\end{bmatrix}
-
\begin{bmatrix}
0 \\
3 \\
4
\end{bmatrix}
=
\begin{bmatrix}
-1 \\
-1 \\
3
\end{bmatrix}
$$

So the line can be written as:

$$
\mathbf{p}_1 +
t
\begin{bmatrix}
-1 \\
-1 \\
3
\end{bmatrix}
$$

or:

$$
\begin{bmatrix}
-1 \\
2 \\
7
\end{bmatrix}
+
t
\begin{bmatrix}
-1 \\
-1 \\
3
\end{bmatrix}
$$

### Mental model

Read:

$$
\mathbf{p}_1 + t(\mathbf{p}_1-\mathbf{p}_2)
$$

as:

> Start at $\mathbf{p}_1$, then move `t` times along the direction connecting $\mathbf{p}_1$ and $\mathbf{p}_2$.

`t` acts like a slider.

- `t = 0` → stay at $\mathbf{p}_1$
- positive values move in the direction of $\mathbf{p}_1-\mathbf{p}_2$
- negative values move in the opposite direction
- changing `t` sweeps out the entire line

### Important idea

The subtraction:

$$
\mathbf{p}_1-\mathbf{p}_2
$$

is what creates the **direction vector**.

This is the useful connection:

> Two points define a line because subtracting the points gives a direction vector between them.

Then parametrization uses `t` to scale that direction vector and generate every point on the line.

## Parametrization in video game code

This is basically the same pattern I have already used in game/animation code:

```js
position = start + t * direction
```

In 2D:

```js
x = startX + t * dx
y = startY + t * dy
```

Where:

- `start` = the starting position
- `direction` = the direction vector
- `t` = a scalar controlling how far along that direction to move

Example:

```js
const start = { x: 2, y: 3 };
const direction = { x: 4, y: 2 };

function pointOnLine(t) {
  return {
    x: start.x + t * direction.x,
    y: start.y + t * direction.y
  };
}
```

So:

```js
pointOnLine(0)
// { x: 2, y: 3 }

pointOnLine(0.5)
// { x: 4, y: 4 }

pointOnLine(1)
// { x: 6, y: 5 }

pointOnLine(2)
// { x: 10, y: 7 }
```

This is the same mathematical structure as:

$$
\mathbf{p} + t\mathbf{v}
$$

where:

- $\mathbf{p}$ is the starting point
- $\mathbf{v}$ is the direction vector
- `t` controls how far along the vector to go

### If I have two points instead of a direction vector

In game code, I might calculate the direction from two positions:

```js
const start = { x: 2, y: 3 };
const end = { x: 6, y: 5 };

const direction = {
  x: end.x - start.x,
  y: end.y - start.y
};
```

which gives:

```js
direction = { x: 4, y: 2 };
```

Then:

```js
function pointOnLine(t) {
  return {
    x: start.x + t * direction.x,
    y: start.y + t * direction.y
  };
}
```

Mathematically, that is:

$$
\mathbf{p}_1 + t(\mathbf{p}_2-\mathbf{p}_1)
$$

### Mental model

> Parametrization is basically taking the familiar game-code pattern `start + t * direction` and expressing it formally.

The underlying operation is not new to me; the linear algebra notation is.

# TLDR
t scales the direction vector; adding another vector shifts the resulting line.