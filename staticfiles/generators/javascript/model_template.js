class Model{
    constructor(){
        // (1) code_layers_class_instance
        this.layers = %s; 
        this.numLayers = this.layers.length;
    }
        
    predict(x){
        let output = parseInput(x);
        for ( let idx = 0; idx < this.numLayers ; idx++){
            output = this.layers[idx].predict(output);
        }
        return output;
    }
}

function parseInput(x){
    if ( x instanceof Matrix ){
        return new Matrix(x.mat);
    } else if ( ( x instanceof Array ) && x.length ){
        if ( x[0] instanceof Array ){
            return new Matrix( x );
        }else{
            return new Matrix( [x] );
        }
    } else {
        return null;
    }
}

// (2) code_apply_func

%s

// (3) code_act_funcs

%s

// (4) code_layers_class

%s

// (5) code_matrix

%s


/* #############################
   ####   D A T A S E T S   ####
   ############################# */

const datasets = {
    xor : new Matrix([[0,0],[0,1],[1,0],[1,1]]),
    iris : new Matrix([
            [0.39, 0.38, 0.54, 0.50],
            [0.11, 0.50, 0.10, 0.04],
            [0.61, 0.33, 0.61, 0.58]
        ])
};