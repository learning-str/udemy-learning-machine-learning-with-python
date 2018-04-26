# coding: UTF-8
import math
import matplotlib.pyplot as plt

def sigmoid(a):
    return 1.0 / (1.0 + math.exp(-a))

class Neuron:
   inputSum = 0.0
   output = 0.0
   def setInput(self, input):
       self.inputSum += input
   def getOutput(self):
       self.output = sigmoid(self.inputSum)
       return self.output

class NeuralNetwork:
    weight = [1.5, -2.5, -0.5]
    neuron = Neuron()
    def commit(self, inputData):
        for i in range(len(self.weight)):
            self.neuron.setInput(inputData[i] * self.weight[i])
        return self.neuron.getOutput()

referPoint0 = 34.5
referPoint1 = 137.5

trialData = []
trialDataFile = open('trialData.txt', 'r')
for list in trialDataFile:
    line = list.rstrip().split(',')
    trialData.append(
        [float(line[0]) - referPoint0, float(line[1]) - referPoint1]
    )
trialDataFile.close()

neuralNetwork = NeuralNetwork()

position = [[], []]
for data in trialData:
    position[0].append(data[1] + referPoint1)
    position[1].append(data[0] + referPoint0)

plt.scatter(
    position[0], position[1], c = 'red', label = 'Position', marker = '+'
)
plt.legend()
plt.show()
