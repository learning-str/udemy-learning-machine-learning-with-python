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
   def reset(self):
       self.inputSum = 0
       self.output = 0

class NeuralNetwork:
    weight = [-0.5, 0.5]
    neuron = Neuron()
    def commit(self, inputData):
        self.neuron.reset()
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

# try
positionTokyo = [[], []]
positionKanagawa = [[], []]
for data in trialData:
    if neuralNetwork.commit(data) < 0.5:
        positionTokyo[0].append(data[1] + referPoint1)
        positionTokyo[1].append(data[0] + referPoint0)
    else:
        positionKanagawa[0].append(data[1] + referPoint1)
        positionKanagawa[1].append(data[0] + referPoint0)

# plot
plt.scatter(
    positionTokyo[0], positionTokyo[1],
    c = 'red', label = 'Tokyo', marker = '+'
)
plt.scatter(
    positionKanagawa[0], positionKanagawa[1],
    c = 'blue', label = 'Kanagawa', marker = '+'
)
plt.legend()
plt.show()
