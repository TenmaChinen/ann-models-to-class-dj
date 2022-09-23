from pathlib import Path
import numpy as np
import json
import re

BASE_DIR = Path(__file__).resolve().parent

#################################################################################
##################   J A V A S C R I P T   G E N E R A T O R   ##################
#################################################################################

def get_model_code(l_layers_obj):
    jsc = JsStringCode()
    
    l_layer_types = { layer['type'] for layer in l_layers_obj }
    l_layer_acts = { layer['activation'] for layer in l_layers_obj if layer.get('activation') }
    
    code_layers_class_instance = layers_to_code_class_instance(l_layers_obj)
    code_apply_func = jsc.get_code_apply_func()
    code_acts_func = jsc.get_code_activations_func(l_layer_acts)
    code_layers_class = jsc.get_code_layers_class(l_layer_types)
    code_matrix = jsc.load_code_matrix()
    
    code_model_template = jsc.load_code_model_template()
    
    code_full = code_model_template % (
        code_layers_class_instance,
        code_apply_func,
        code_acts_func,
        code_layers_class,
        code_matrix
    )
    
    return code_full


def layers_to_code_class_instance(l_layers_obj):
    
    l_code_layers_instant = []
    for d_layer_obj in l_layers_obj:
        layer_type = d_layer_obj['type']
        d_kwargs = { k : d_layer_obj[k] for k in ['activation','units'] if d_layer_obj.get(k) }
        
        if 'weights' in d_layer_obj:
            d_kwargs['weights'] = list_to_str(d_layer_obj['weights'])
    
        str_args = ', '.join([ f'{v}' for v in d_kwargs.values()])
        l_code_layers_instant.append( f'new {layer_type}({str_args})' )
    
    code_layers_class_instant = list_to_str(l_code_layers_instant)
    return code_layers_class_instant


def list_to_str(l_list):
    l_list = list(map(value_to_str,l_list)) 
    return f"[ {', '.join(l_list)} ]"

def value_to_str(value):
    type_value = type(value)
    if type_value is str:
        return value
    elif type_value is np.ndarray :
        l_values = value.tolist()
        if len(value.shape) == 1:
            l_values = [l_values]
        return f'new Matrix({l_values})'
    elif type_value is None:
        return '0'
    else:
        return str(value)

#################################################################################

class JsStringCode:
    
    def __init__( self ):
        self.code_layers_class = self.load_code_layers_class()
        self.code_acts_func = self.load_code_activations_funcs()
    
    #######################################
    #####   S i n g l e   F e t c h   #####
    #######################################
    
    def get_code_activation_func(self, activation_name):
        pattern = f'(?<![/ *])(function )?{activation_name}[^#]*'
        result = re.search(pattern, self.code_acts_func)
        if result:
            return result.group()
        return ''
    
    def get_code_layer_class(self, layer_type):
        pattern = f'(?<![/ *])class {layer_type}[^#]*'
        result = re.search(pattern, self.code_layers_class)
        if result : return result.group()
    
    #######################################
    ###   M u l t i p l e   F e t c h   ###
    #######################################
            
    def get_code_activations_func(self, l_activations):
        return '\n'.join(map(self.get_code_activation_func, l_activations))

    def get_code_layers_class(self, l_layers_type):
        return '\n'.join(map(self.get_code_layer_class, l_layers_type))
    
    #######
    
    def get_code_apply_func(self):
        pattern = 'function applyFunc[^#]*'
        return re.search( pattern , self.code_acts_func ).group()
    
    @staticmethod
    def load_code_model_template():
        return load_code_str('model_template.js')

    @staticmethod
    def load_code_activations_funcs():
        return load_code_str('activations.js')

    @staticmethod
    def load_code_layers_class():
        return load_code_str('layers.js')
    
    @staticmethod
    def load_code_matrix():
        return load_code_str('matrix.js')

    
def load_code_str(file_name):
    file = open( BASE_DIR / file_name,'r')
    str_code = file.read()
    file.close()
    return str_code


def save_code_model(file_name, code_model):
    file = open( file_name , 'w' )
    file.write(code_model)
    file.close()