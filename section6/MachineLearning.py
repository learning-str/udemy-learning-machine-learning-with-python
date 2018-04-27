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
        self.outputLayer.setInput(
            self.middleLayer[0].getOutput() * self.weightMO[0],
        )
        self.outputLayer.setInput(
            self.middleLayer[1].getOutput() * self.weightMO[1],
        )
        self.outputLayer.setInput(self.middleLayer[2] * self.weightMO[2])

        return self.outputLayer.getOutput()

    def learn(self, inputData):
        learningRate = 0.3
        correctValue = inputData[2]

        # output
        outputData = self.commit([inputData[0], inputData[1]])

        # outputLayer -> middleLayer
        deltaWeightMO = (correctValue - outputData) * outputData *\
            (1.0 - outputData)
        oldWeightMO = list(self.weightMO)
        self.weightMO[0] += self.middleLayer[0].output * deltaWeightMO *\
            learningRate
        self.weightMO[1] += self.middleLayer[1].output * deltaWeightMO *\
            learningRate
        self.weightMO[2] += self.middleLayer[2] * deltaWeightMO * learningRate

        # middleLayer -> inputLayer
        deltaWeightIM = [
            deltaWeightMO * oldWeightMO[0] * self.middleLayer[0].output *\
                (1.0 - self.middleLayer[0].output),
            deltaWeightMO * oldWeightMO[1] * self.middleLayer[1].output *\
                (1.0 - self.middleLayer[1].output),
        ]
        self.weightIM[0][0] += self.inputLayer[0] * deltaWeightIM[0] *\
            learningRate
        self.weightIM[0][1] += self.inputLayer[0] * deltaWeightIM[1] *\
            learningRate
        self.weightIM[1][0] += self.inputLayer[1] * deltaWeightIM[0] *\
            learningRate
        self.weightIM[1][1] += self.inputLayer[1] * deltaWeightIM[1] *\
            learningRate
        self.weightIM[2][0] += self.inputLayer[2] * deltaWeightIM[0] *\
            learningRate
        self.weightIM[2][1] += self.inputLayer[2] * deltaWeightIM[1] *\
            learningRate

referPoint0 = 34.5
referPoint1 = 137.5

trainingData = []
trainingDataFile = open('trainingData.txt', 'r')
for line in trainingDataFile:
    line = line.rstrip().split(',')
    trainingData.append([
        float(line[0]) - referPoint0,
        float(line[1]) - referPoint1,
        int(line[2]),
    ])
trainingDataFile.close()

neuralNetwork = NeuralNetwork()

# learning
for t in range(0, 1000):
    for data in trainingData:
        neuralNetwork.learn(data)
print neuralNetwork.weightIM
print neuralNetwork.weightMO
dataToCommit = [
    [34.6, 138.0], [34.6, 138.18], [35.4, 138.0], [34.98, 138.1],
    [35.0, 138.25], [35.4, 137.6], [34.98, 137.52], [34.5, 138.5],
    [35.4, 138.1],
]

for data in dataToCommit:
    data[0] -= referPoint0
    data[1] -= referPoint1

positionTokyoLearned = [[], []]
positionKanagawaLearned = [[], []]

for data in dataToCommit:
    if neuralNetwork.commit(data) < 0.5:
        positionTokyoLearned[0].append(data[1] + referPoint1)
        positionTokyoLearned[1].append(data[0] + referPoint0)
    else:
        positionKanagawaLearned[0].append(data[1] + referPoint1)
        positionKanagawaLearned[1].append(data[0] + referPoint0)

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
    c = 'red', label = 'TokyoLearn', marker = '+',
)
plt.scatter(
    positionKanagawaLearning[0], positionKanagawaLearning[1],
    c = 'blue', label = 'KanagawaLearn', marker = '+',
)
plt.scatter(
    positionTokyoLearned[0], positionTokyoLearned[1],
    c = 'red', label = 'Tokyo', marker = 'o',
)
plt.scatter(
    positionKanagawaLearned[0], positionKanagawaLearned[1],
    c = 'blue', label = 'Kanagawa', marker = 'o',
)


plt.legend()
plt.show()
