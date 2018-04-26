# coding: UTF-8

class Neuron:
   inputSum = 0.0
   def setInput(self, input):
       self.inputSum += input
       print self.inputSum

class NeuralNetwork:
   neuron = Neuron()
   def commit(self, inputData):
       for data in inputData:
           self.neuron.setInput(data)

neuralNetwork = NeuralNetwork()

trialData = [1.0, 2.0, 3.0]
neuralNetwork.commit(trialData)
