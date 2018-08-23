from numpy import loadtxt,where
from pylab import  scatter,show,legend,xlabel,ylabel
import numpy as np

#载入data
data = loadtxt('F:\\logicalregression\\test\\data1.txt',delimiter=',')

X = data[:,0:2]
y = data[:,2]

pos = where(y == 1)
neg = where(y == 0)
scatter(X[pos,0],X[pos,1],marker = 'o',c = 'b')
scatter(X[neg,0],X[neg,1],marker='x',c = 'r')
xlabel('Feature1/Exam 1 score')
ylabel('Feature2/Exam 2 score')
legend(['Fail','Pass'])
show()


def sigmoid(X):
    '''Compute sigmoid function '''
    den = 1.0 + np.e ** (-1.0 * X)
    gz = 1.0 / den
    return gz


def compute_cost(theta, X, y):
    '''computes cost given predicted and actual values'''
    m = X.shape[0]  # number of training examples
    theta = np.reshape(theta, (len(theta), 1))

    J = (1. / m) * (
                -np.transpose(y).dot(np.log(sigmoid(X.dot(theta)))) - transpose(1 - y).dot(log(1 - sigmoid(X.dot(theta)))))

    grad = np.transpose((1. / m) * np.transpose(sigmoid(X.dot(theta)) - y).dot(X))
    # optimize.fmin expects a single value, so cannot return grad
    return J[0][0]  # ,grad


def compute_grad(theta, X, y):
    '''compute gradient'''
    m = X.shape[0]
    theta.shape = (1, 3)
    grad = np.zeros(3)
    h = sigmoid(X.dot(theta.T))
    delta = h - y
    l = grad.size
    for i in range(l):
        sumdelta = delta.T.dot(X[:, i])
        grad[i] = (1.0 / m) * sumdelta * -1
    theta.shape = (3,)
    return grad
def predict(theta, X):
    '''Predict label using learned logistic regression parameters'''
    m, n = X.shape
    p = np.zeros(shape=(m,1))
    h = sigmoid(X.dot(theta.T))
    for it in range(0, h.shape[0]):
        if h[it]>0.5:
            p[it,0]=1
        else:
            p[it,0]=0
    return p

p = predict(np.array(theta), X)
print('Train Accuracy: %f'%((y[where(p == y)].size / float(y.size))*100.0))