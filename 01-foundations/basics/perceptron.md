# The Rosenblatt Perceptron

The perceptron is an artificial neuron, that is, a model of a biological neuron.

![pg30_Image_6](https://user-images.githubusercontent.com/62965911/228531087-492b9509-3168-4bb5-a82a-9dbdcf25eddc.jpeg)

The neuron receives stimuli on the dendrites, and in cases of sufficient stimuli, the neuron fires (also known as getting activated or excited) and outputs stimulus on its axon, which is transmitted to other neurons that have synaptic connections to the excited neuron. Synaptic signals can be excitatory or inhibitory; that is, some signals can prevent a neuron from firing instead of causing it to fire.

A **perceptron** is a type of **artificial neuron**. It sums up the inputs to compute an intermediate value _z_, which is fed to an **activation function**. The perceptron uses the **sign function** as an activation function, but **other artificial neurons use other functions**.

The perceptron consists of a computational unit, a number of inputs, each with an associated input weight, and a single output:

![pg31_Image_7](https://user-images.githubusercontent.com/62965911/228531930-d901d5a1-a63e-41e8-8757-74e6147c8f95.jpeg)

## Code snippet

```py
# First element in vector x must be 1.
# Length of w and x must be n+1 for neuron with n inputs.
def compute_output(w, x):
    z = 0.0
    for i in range(len(w)):
        z += x[i] * w[i] # Compute sum of weighted inputs
    if z < 0: # Apply sign function
        return -1
    else:
        return 1
```

## Example of a Two-Input Perceptron

![pg34_Image_11](https://user-images.githubusercontent.com/62965911/228533452-755225d2-dab5-4e6b-b835-3d23d80ce92d.jpeg)

## Perceptron and the NAND Gate

Behavior of a Perceptron with Two Inputs:

| X0 | X1              | X2              | W0\*X0 | W1\*X1 | W2\*X2 | _Z_  | _Y_             |
|----|-----------------|-----------------|--------|--------|--------|------|-----------------|
| 1  | −1<br>`(False)` | −1<br>`(False)` | 0.9    | 0.6    | 0.5    | 2.0  | 1<br>`(True)`   |
| 1  | 1<br>`(True)`   | −1<br>`(False)` | 0.9    | −0.6   | 0.5    | 0.8  | 1<br>`(True)`   |
| 1  | −1<br>`(False)` | 1<br>`(True)`   | 0.9    | 0.6    | −0.5   | 1.0  | 1<br>`(True)`   |
| 1  | 1<br>`(True)`   | 1<br>`(True)`   | 0.9    | −0.6   | −0.5   | −0.2 | −1<br>`(False)` |

The table shows the inputs and the outputs, the intermediate values after applying the weights, as well as the sum before applying the activation function. Note what happens if we interpret the inputs and outputs as Boolean values, where –1 represents `False` and +1 represents `True`. The perceptron with these specific weights implements a `NAND` gate! Paraphrasing Nielsen, this is comforting because we know that by combining multiple `NAND` gates, we can build any logical function, but it is also kind of disappointing because we thought that neural networks were going to be something much more exciting than just Boolean logic (Nielsen, 2015).

## Perceptron Learning Algorithm

<a target="_blank" href="https://colab.research.google.com/gist/sparsh-ai/2f9831067b06b1adfa49455f893b2211/perceptron-learning.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

## Limitation of Perceptron

Perceptron can learn straight line functions (e.g. NAND) but unable to learn curved line functions (e.g. XOR). One suggested solution for this is to use multi-level perceptron, which is close to a deep neural network because of its hidden-layer approach.