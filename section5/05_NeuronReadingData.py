# coding: UTF-8
import math

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

print trialData

neuralNetwork = NeuralNetwork()

trialData = [1.0, 2.0, 3.0]
print neuralNetwork.commit(trialData)
