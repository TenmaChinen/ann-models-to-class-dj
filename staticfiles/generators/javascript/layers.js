class Dense {
  
    constructor(activation, weights) {
        this.activation = activation;
        [ this.kernel , this.bias ] = weights;
    }
    
    predict(x){
        return this.activation(x.dot(this.kernel).add(this.bias));
    }   
}#

