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

    def learn(self, inputData):
        print inputData

referPoint0 = 34.5
referPoint1 = 137.5

trainingData = []
trainingDataFile = open('trainingData.txt', 'r')
for line in trainingDataFile:
    line = line.rstrip().split(',')
    trainingData.append([
        float(line[0]) - referPoint0,
        float(line[1]) - referPoint1,
        int(line[2])
    ])
trainingDataFile.close()

neuralNetwork = NeuralNetwork()

# learning
neuralNetwork.learn(trainingData[0])

# preperation of display
positionTokyoLearning = [[], []]
positionKanagawaLearning = [[], []]
for data in trainingData:
    if data[2] < 0.5:
        positionTokyoLearning[0].append(data[1] + referPoint1)
        positionTokyoLearning[1].append(data[0] + referPoint0)
    else:
        positionKanagawaLearning[0].append(data[1] + referPoint1)
        positionKanagawaLearning[1].append(data[0] + referPoint0)

# plot
plt.scatter(
    positionTokyoLearning[0], positionTokyoLearning[1],
    c = 'red', label = 'tokyoLearn', marker = '+'
)
plt.scatter(
    positionKanagawaLearning[0], positionKanagawaLearning[1],
    c = 'blue', label = 'kanagawaLearn', marker = '+'
)

plt.legend()
plt.show()
