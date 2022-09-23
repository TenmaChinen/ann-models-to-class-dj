from pathlib import Path
import numpy as np
import re

BASE_DIR = Path(__file__).resolve().parent

#################################################################################
######################   P Y T H O N   G E N E R A T O R   ######################
#################################################################################

def get_model_code(l_layers_obj):
    psc = PyStringCode()
    
    l_layer_types = { layer['type'] for layer in l_layers_obj }
    l_layer_acts = { layer['activation'] for layer in l_layers_obj if layer.get('activation') }
    
    code_layer_classes = psc.get_code_layers_class(l_layer_types)
    code_act_funcs = psc.get_code_activations_func(l_layer_acts)
    
    l_code_layers_instant = []
    
    for d_layer_obj in l_layers_obj:
        layer_type = d_layer_obj['type']
        d_kwargs = { k : d_layer_obj[k] for k in ['activation','units'] if d_layer_obj.get(k) }
        
        if 'weights' in d_layer_obj:
            d_kwargs['l_weights'] = list_to_str(d_layer_obj['weights'])
    
        str_args = ', '.join([ f'{k}={v}' for k,v in d_kwargs.items()])
        l_code_layers_instant.append( f'{layer_type}({str_args})' )
     
    code_l_layers_classes_instant = list_to_str(l_code_layers_instant)
    
    code_model_template = psc.get_code_model_template()
    code_model = code_model_template.format(
        code_l_layers_class_instantiation = code_l_layers_classes_instant,
        code_layer_classes = code_layer_classes,
        code_activation_functions = code_act_funcs
    )
        
    return code_model


def list_to_str(l_list):
    l_list = list(map(value_to_str,l_list)) 
    return f"[ {', '.join(l_list)} ]"

def value_to_str(value):
    type_value = type(value)
    if type_value is str:
        return value
    elif type_value is np.ndarray :
        return f'np.array({value.tolist()})'
    elif type_value is None:
        return '0'
    else:
        return str(value)

class PyStringCode:
    
    def __init__( self ):
        self.code_layers = self.get_code_layers()
        self.code_acts = self.get_code_activations()
        
    def get_code_layer_class(self, layer_type):
        pattern = f'class {layer_type}[^;]*'
        result = re.search( pattern, self.code_layers)
        if result : return result.group()
    
    def get_code_layers_class(self,l_layers_type):
        return '\n'.join(map(self.get_code_layer_class, l_layers_type))
    
    def get_code_activation_func(self, activation_name):
        pattern = f'(def )?{activation_name}[^;]*'
        result = re.search(pattern, self.code_acts)
        if result:
            return result.group()
        return ''
            
    def get_code_activations_func(self, l_activations):
        return '\n'.join(map(self.get_code_activation_func, l_activations))

    @staticmethod
    def get_code_model_template():
        return load_code_str( BASE_DIR / 'model_template.py')

    @staticmethod
    def get_code_activations():
        return load_code_str( BASE_DIR / 'activations.py')

    @staticmethod
    def get_code_layers():
        return load_code_str( BASE_DIR / 'layers.py')
    
def load_code_str(file_name):
    file = open(file_name,'r')
    code = file.read()
    file.close()
    return code
