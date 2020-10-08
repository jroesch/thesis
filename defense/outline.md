# Principled Optimization of Dynamic Neural Networks

### Intro

PSA: today when I talk about optimization I mean PROGRAM optimization

When I began this work it was possible to write dynamic
    neural networks either by hand or using frameworks.
A central challenge of defining these networks were
    odd control-flow constructs, lack
    of data structures, and poor support for dynamic shapes.
In particular optimizing programs using these features
    was a challenge, leading to dynamic neural networks
    often paying a large performance cost.

The central issue limiting the optimization of dynamic
    neural network was a focus on runtime based approaches.
Previous work tries to solve the above problems by detecting
    dynamic cases and using runtime modifications, or
    recasting the dynamic problem as a static problem
    in order to avoid needing to ever perform dynamic
    execution.
Instead of avoiding dynamic features we focus on
    how to make them as fast as can be in static
    subsets and gracefully handle more dynamic cases.

The key realization is that we can eliminate the need
    for ad-hoc runtime and compiler modifications
    with a principled compiler design motivated
    by the last 40+ years of compiler research.
In compilation the key challenges tend to be representation,
    optimizations, and code generation or execution.
In machine learning this story is a bit more complex.

In this thesis I propose that we can generalize overspecialized
  compilation & runtime techniques applied to static dataflow graphs,
  the predominant programming model of deep learning,
  to fully dynamic neural networks.
These generalizations are powered by a simple insight:
  dynamic neural networks are just programs which manipulate tensors.
The challenge is how to build a representation that captures this generality
  in a principled manner, enabling state-of-the-art performance without limiting the programming model.

To do this we believe there are 4 key pieces
    * representation, we need a compiler representation rich enough to capture dynamic behaviors
    * differentiation, in machine learning applications it is essential we can perform automatic differentiation of programs
    * optimization, we need optimizations that work both in dynamic and static cases
    * execution, finally we need an efficient mechanism for executing the remaining dynamic features with minimal overhead

The remainder of this talk discusses how we adapted
    ideas from the traditional compiler literature
    to deep learning, and achieved state-of-the-art
    performance on key models.

My thesis is split into the above 4 parts, we will first discuss the design of
    our representation, how to perform automatic differentiation on it,
    focus in on a specific set of dynamic optimizations, and finally
    how we efficiently execute dynamic features.

Finally I will complete the talk with some case studies
    of other research and practice which has built on
    my thesis work.

### Representation

### Differentiation

### Optimization

### Execution

### Case Studies

### Future Work
