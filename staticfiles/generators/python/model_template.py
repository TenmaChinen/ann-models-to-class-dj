import numpy as np

class Model:
    def __init__(self):
        self.l_layers = {code_l_layers_class_instantiation}
        
    def predict(self,x):
        output = x.copy()
        for layer in self.l_layers:
            output = layer(output)
            
        return output
    
{code_layer_classes}
{code_activation_functions}