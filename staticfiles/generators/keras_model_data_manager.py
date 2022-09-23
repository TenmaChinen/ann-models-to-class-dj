#################################################################################
####################   K E R A S   D A T A   M A N A G E R   ####################
#################################################################################

import json
import h5py

def get_model_data(h5_path,json_path=None):
    '''
        output: l_layers_objs
    '''
    h5_file = h5py.File(h5_path,'r')

    if h5_file.attrs['keras_version'] != '2.7.0' :
        print('Keras Version == 2.7.0 Only Supported')
        return None

    if 'model_config' in h5_file.attrs:
        d_model_config = json.loads(h5_file.attrs['model_config'])
        d_model_weights = h5_file['model_weights']
    elif json_path:
        d_model_config = load_model_config(json_path)
        d_model_weights = h5_file
    else:
        print('Json File Needed!')
        return None
    
    if d_model_config['class_name'] != 'Sequential' :
        print('Non Sequential Models Still Not Supported')
        return None
    
    l_layers_cnf = get_layers_cnf(d_model_config)
    l_layers_objs = get_weights_and_acts(l_layers_cnf,d_model_weights)
    
    h5_file.close()
    return l_layers_objs


def get_layers_cnf(d_model_config):
    l_keys = ['name','units','dtype','activation','use_bias']
    l_layers_cnf = []
    for layer in d_model_config['config']['layers']:
        if layer['class_name'] not in [ 'InputLayer','Dropout' ] :
            d_layer_cnf = { k : layer['config'][k] for k in l_keys }
            d_layer_cnf[ 'class_name' ] = layer['class_name']
            l_layers_cnf.append(d_layer_cnf)
    return l_layers_cnf


def get_weights_and_acts(l_layers_cnf,d_model_weights):
    l_layers_obj = []
    
    for d_layer_cnf in l_layers_cnf:

        class_name = d_layer_cnf['class_name']
        layer_name = d_layer_cnf['name']
        use_bias = d_layer_cnf['use_bias']
        activation = d_layer_cnf['activation']
        d_layer_data = { 'type' : class_name }
        
        if class_name == 'Dense':
            d_weights = d_model_weights[layer_name][layer_name]
            kernel = d_weights['kernel:0'][:]
            bias = d_weights['bias:0'][:] if use_bias else 0
            d_layer_data.update( {'activation' : activation, 'weights' : [kernel,bias] } )
            
        elif class_name == 'LSTM':
            d_weights, *_ = d_model_weights[layer_name][layer_name].values()
            units = d_layer_cnf['units']
            kernel = d_weights['kernel:0'][:]
            bias = d_weights['bias:0'][:]
            rec_kernel = d_weights['recurrent_kernel:0'][:]
            d_layer_data.update( {'activation' : activation, 'units' : units, 'weights' : [kernel,bias,rec_kernel]} )
        
        l_layers_obj.append( d_layer_data )
        
    return l_layers_obj

def load_model_config(json_path):
    file = open(json_path,'r')
    d_model_config = json.load(file)
    file.close()
    return d_model_config