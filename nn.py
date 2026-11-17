import random
from engine import Value
# zero every gradient to start calculating the loss

class  Module:
    def zero_grad(self):
        for parameter in self.parameters():
            parameter.grad = 0
    
    def parameters (self):
        return[]

class Neuron(Module):
    #initializing our parameters of weights and biases and setting our bias to 0. The range for the weights is from -1 to 1 because we will be using relu instead of softmax as our activation , or for our non-linearity
    def __init__(self,nin,nonlin=True):
        self.w =[Value(random.uniform(-1,1))for _ in range (nin)]
        self.b = Value(0)
        self.nonlin = nonlin
    # calling the ain fuunction of the neural network  that is weights @ nin + bias, the sum of the dot products of the weights and nins is put in a zip then summed with the bias. for the first loop the bias is zero why ???? im bout to find out

    def __call__(self,x):
        act = sum((wi*xi for wi,xi in zip(self.w,x)),self.b)
        return act.relu() if self.nonlin else act
    def parameters(self):
        return self.w + [self.b]   
    
    def __repr__(self):
        return f"Neuron({len(self.w)})"
    
class Layer(Module):
    def __init__(self,nin,nout,**kwargs):
        self.neurons =[Neuron(nin,**kwargs) for _ in range(nout)]
    
    def __call__(self,x):
        out =[n(x) for n in self.neurons]
        return out[0] if len(out)==1 else out
    
    def parameters(self):
        return [p for neuron in self.neurons for p in neuron.parameters()]
    
    def __repr__(self):
        return f"Layer of [{', '.join(str(n) for n in self.neurons)}]"
    
class MLP(Module):
    def __init__(self,nin,nouts):
        sz =[nin]+nouts
        self.layers =[Layer(sz[i],sz[i+1]) for i in range(len(nouts))]
    
    def __call__(self,x):
        for layer in self.layers:
            x = layer(x)
        return x
    
    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]
    
    def __repr__(self):
        return f"MLP of [{', '.join(str(layer) for layer in self.layers)}]"

