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
    # weight
    weightIM = [[0.496, 0.512], [-0.501, 0.998], [0.498, -0.502]]
    weightMO = [0.121, -0.4996, 0.200]
    # declaration
    inputLayer = [0.0, 0.0, 1.0]
    middleLayer = [Neuron(), Neuron(), 1.0]
    outputLayer = Neuron()
    def commit(self, inputData):
        # reset
        self.inputLayer[0] = inputData[0]
        self.inputLayer[1] = inputData[1]
        self.middleLayer[0].reset()
        self.middleLayer[1].reset()
        self.outputLayer.reset()

        # inputLayer -> middleLayer
        self.middleLayer[0].setInput(self.inputLayer[0] * self.weightIM[0][0])
        self.middleLayer[0].setInput(self.inputLayer[1] * self.weightIM[1][0])
        self.middleLayer[0].setInput(self.inputLayer[2] * self.weightIM[2][0])

        self.middleLayer[1].setInput(self.inputLayer[0] * self.weightIM[0][1])
        self.middleLayer[1].setInput(self.inputLayer[1] * self.weightIM[1][1])
        self.middleLayer[1].setInput(self.inputLayer[2] * self.weightIM[2][1])

        # middleLayer -> outputLayer
        self.outputLayer.setInput(self.middleLayer[0].getOutput() * self.weightMO[0])
        self.outputLayer.setInput(self.middleLayer[1].getOutput() * self.weightMO[1])
        self.outputLayer.setInput(self.middleLayer[2] * self.weightMO[2])

        return self.outputLayer.getOutput()

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
