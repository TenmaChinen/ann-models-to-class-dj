
class Dense:
    def __init__( self , activation, l_weights):
        self.activation = activation
        self.kernel, self.bias = l_weights

    def __call__(self,x):
        return self.activation(np.dot(x,self.kernel) + self.bias)
;

class LSTM:
    def __init__(self,units,activation,l_weights):
        self.units = units
        self.activation = activation
        kernel, bias, rec_kernel = l_weights
        self.w_i, self.w_f, self.w_c, self.w_o = np.split(kernel, 4 , axis = 1 )
        self.b_i, self.b_f, self.b_c, self.b_o = np.split(bias, 4 , axis = 0 )
        self.u_i, self.u_f, self.u_c, self.u_o = np.split(rec_kernel, 4 , axis = 1 )
                 
    def __call__(self,x):
        
        l_states = []
        for x_batch in x:
            
            h_t_1 = np.zeros((1,self.units)) # h_{t-1}
            c_t_1 = np.zeros((1,self.units)) # c_{t-1}

            for x_t in x_batch[:,None]:
                i_t = sigmoid( np.dot(x_t, self.w_i) + np.dot(h_t_1, self.u_i) + self.b_i )

                c_t_tilda = self.activation(np.dot(x_t, self.w_c) + np.dot(h_t_1, self.u_c) + self.b_c) # tanh

                f_t = sigmoid( np.dot( x_t, self.w_f ) + np.dot( h_t_1, self.u_f ) + self.b_f )

                c_t = i_t * c_t_tilda + f_t * c_t_1
                o_t = sigmoid( np.dot( x_t, self.w_o ) + np.dot( h_t_1, self.u_o ) + self.b_o )
                h_t = o_t * self.activation( c_t ) # tanh

                h_t_1 = h_t
                c_t_1 = c_t
            
            l_states.append(h_t)

        return np.vstack(l_states)
;