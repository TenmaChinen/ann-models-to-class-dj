
linear = lambda x : x;

relu = lambda x : np.maximum(0,x);

sigmoid = lambda x : 1/(1 + np.exp(-x));

softsign = lambda x : x/(1 + abs(x));

tanh = lambda x : np.tanh(x);

leaky_relu = lambda x : np.where(x > 0, x, x * 0.01);

def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x/exp_x.sum(axis=1, keepdims=True);