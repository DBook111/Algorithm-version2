import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

x = np.linspace(-10, 10, 400)
y_relu = relu(x)
y_sigmoid = sigmoid(x)
y_softmax = softmax(x)

# plt.plot(x, y_relu, label="ReLU", color="red")
# plt.plot(x, y_sigmoid, label="Sigmoid", color="green")
plt.plot(x, y_softmax, label="Softmax", color="blue")

plt.xlabel("input")
plt.ylabel("output")
plt.title("Softmax")
plt.legend()
plt.grid(True)
plt.savefig(r"C:\Yan3\Algorithm-version2\Painting\PaperPainting\Softmax.png")
plt.show()