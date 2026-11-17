# micro-grad engine

Mathematical functions eg f(x)=g(x)usually show a relationship between independent and dependent variables. Knowing this relationships are really useful in aiding us to observe the movement of the dependent variiable relative to the independent variable and tweak it to our liking.

for example :
  
       a = b + c

  in this classic example , we know for sure that adding c by 1 will increase a by 1 and will have no effect on b, because b is independent and a is dependent on both c and b.Hence any change in c or b will change a.

  One could argue the other way around and change the equation to take the form:

       b + c = a 
       
  where a takes the form of an independent variable and b and c takes the form of the dependent variables. In such a situation a change in a affects both b and c but the degree to which a affects b and c is what is mathematically appealing because given a perfect a , you could run your way back to the proper values of b and c.

This activity is known as backpropagation, where we look at the relationship between the independent variables relative to the dependent ones and tweak our independent variables to get the shape that we want for our dependent variable.

It is useful in the training of neuralnetworks to ensure high accuracy in learning.During the training of neural networks we have our desired observation, known as y_true.The neural network which is just a huge mathematical function taking the form of:
    
     y_pred = weights @ inputs + bias

has to predict the true value of y given the independent variables of inputs, weights and biases.Since the training data cannot be tweaked, the weights and biases have to carry the weight of updating the equation to satisfy the true value of y.This is where backpropagation comes into play.

Given the true y , we can compute the relationship between y and the independent variables and adjust the weights and biases appropriately to fit the true y.However we cant just start updating the weights and biases without a ruler to measure how far we've adjusted the equation. This is where the loss calculation comes to play. The difference between the predicted value of y and the true y will be the ruler to guide the adjustments of the wieghts and biases. Using this loss ,we have a now clear goal other than adjust the weights to match the true y.Our goal now becomes to minimise the loss to obtain the clossest value to the true y for a million of the predictions.

This repo aims at making the micrograd engine , an inspiration from Andrej karpathy's course zero to hero neural networks. In an aim to understand how backpropagation works ini brute force, without having to fancy pytorch.It is a test for the understanding of the basic properties of neuural network mechanics among which is 

   1. The design of Neural Networks
   2. How a neural networks work and flow of information through the neural networks
   3. Optimization and loss calculation in a Neural network
   4. Training habits of a neural network.



