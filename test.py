import numpy as np


# First Define Re-usable Perceptron Class
class Perceptron():
    # how many wieghts we need to learn
    # threshold is the number of epochs to iterate through
    # lr (learning rate) used to determine the magnitude of change for weights during each step
    def __init__(self, no_of_inputs, threshold=100, lr=0.01):
        self.w = np.zeros(no_of_inputs + 1)
        self.threshold = threshold
        self.lr = lr

    # accepts array of inputs equal to the number of inputs
    def make_prediction(self, inputs):
        # check if dot product of inputs and weights is greater or equal to 0
        sum = np.dot(inputs, self.w[1:]) + self.w[0]
        return 1 if sum >= 0 else 0

    def we_train(self, tri, outputs):
        # iterate to range of threshold
        for _ in range(self.threshold):
            for inputs, output in zip(tri, outputs):
                # compare current input with current weight
                prediction = self.make_prediction(inputs)
                self.w[1:] += self.lr * (output - prediction) * inputs

                # update the bias weight value
                self.w[0] += self.lr * (output - prediction)


def main():

    # Training input data
    tri = np.array([
            [1, 1],
            [1, 0],
            [0, 1],
            [0, 0]
        ])

    inputs1 = np.array([1, 1])
    inputs2 = np.array([0, 0])


    print('\n')
    # Perceptron 1 - And
    output1 = np.array([1, 0, 0, 0])
    ptron1 = Perceptron(2)
    ptron1.we_train(tri, output1)
    print('And:', inputs1, ptron1.make_prediction(inputs1))
    print('And:', inputs2, ptron1.make_prediction(inputs2))

    print('\n')
    # Perceptron 2 - Or
    output2 = np.array([1, 1, 1, 0])
    ptron2 = Perceptron(2)
    ptron2.we_train(tri, output2)

    print('Or: ', inputs1, ptron2.make_prediction(inputs1))
    print('Or: ', inputs2, ptron2.make_prediction(inputs2))

    print('\n')
    # Perceptron 3 - Not
    output3 = np.array([0, 1, 1, 1])
    ptron3 = Perceptron(2)
    ptron3.we_train(tri, output3)

    print('NAND:', inputs1, ptron3.make_prediction(inputs1))
    print('NAND:', inputs2, ptron3.make_prediction(inputs2))


main()

