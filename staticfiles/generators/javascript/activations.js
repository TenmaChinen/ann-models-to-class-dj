
function applyFunc(matrix,fnc){
    const resMatrix = new Matrix(matrix.mat);
    for (let row = 0; row < matrix.rows; row++) {
        for (let col = 0; col < matrix.cols; col++) {
          resMatrix.mat[row][col] = fnc(matrix.mat[row][col]);
        }
    }
    return resMatrix;
}#

linear = (m) => m;#
relu = (m) => applyFunc(m, (v) => (v<0) ? 0 : v);#
sigmoid = (m) => applyFunc(m, (v) => (1/(1+Math.exp(-v))));#
softsign = (m) => applyFunc(m, (v) => v / (1+Math.abs(v)));#
tanh = (m) => applyFunc(m, (v) => Math.tanh(v));#

// leaky_relu = lambda x : np.where(x > 0, x, x * 0.01);

function softmax(m){
    const matExp = m.sub(m.max()).exp();
    return matExp.divide( matExp.sum(1) ); 
}