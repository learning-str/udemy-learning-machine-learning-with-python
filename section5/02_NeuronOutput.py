# coding: UTF-8

class Neuron:
   inputSum = 0.0
   output = 0.0
   def setInput(self, input):
       self.inputSum += input
   def getOutput(self):
       self.output = self.inputSum
       return self.output

class NeuralNetwork:
   neuron = Neuron()
   def commit(self, inputData):
       for data in inputData:
           self.neuron.setInput(data)
       return self.neuron.getOutput()

neuralNetwork = NeuralNetwork()

trialData = [1.0, 2.0, 3.0]
print neuralNetwork.commit(trialData)
