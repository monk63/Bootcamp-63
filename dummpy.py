from random import randint
#from sklearn.datasets import load_boston
import numpy as np
import pandas as pd
#from skimage.io import imread
#from skimage.transform import resize
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import matplotlib.cm as cm
np.random.seed(1)

from keras.layers import Dense, Activation
from keras.models import Sequential


'''
y = np.array([44,21,37])
print (y)
print (y.shape)

X = np.array([[1.1, 1, 545, 1],[4.6, 0, 345, 2],
[7.2, 1, 754, 3]])
print (X)
'''

'''
n=1000
examples = set(range(n))
results = list()
for j in range(10000):
# your boostrapped sample
    chosen = [randint(0,n) for k in range(n)]
# out-of-sample
    results.append((1000-len(set(chosen)&examples))
                    /float(n))
print ("Out-of-boostrap: %0.1f %%" %
        (np.mean(results)*100)) 
'''

#This code demonstates how to perform replacement task.
'''
data = pd.DataFrame([[1,2,np.nan],[np.nan,2,np.nan],[3,np.nan,np.nan],
                    [np.nan,3,8], [5,3,np.nan]],columns=['A','B','C'])

print(data,'\n')

print(data.isnull().sum(axis=0))
'''

'''
 # matplotlib inline
boston = load_boston()
X, y = boston.data, boston.target
X = pd.DataFrame(X, columns=boston.feature_names)
X.boxplot('LSTAT',return_type='axes')
'''

'''
X = np.array([[1,2,3],[3,2,1]])
def poly_expansion(A):
    return np.array([[x*y for x in row for y in row] for row in A])

poly_X = poly_expansion(X)
print ('Dimensions after expanding : %s' % str(poly_X.shape))
print (poly_X) 
'''

'''
example_file = ("pic2.jpg")
image = imread(example_file, as_grey=True)
plt.imshow(image, cmap=cm.gray)
plt.show()
'''

'''        
# Generate a sequence of numbers from -10 to 10 with 100 steps in between
x = np.linspace(-10, 10, 100)
# Create a second array using sine
y = np.sin(x)
# The plot function makes a line chart of one array against another
plt.plot(x, y, marker="x")        
'''

'''
X = np.array([[0,1,0],
             [1,0,0],
             [1,1,1],
             [0,1,1]])

y = np.array([[0,1,1,0]]).T

def sigmoid(x):
    return 1/(1+np.exp(-x))

def bce_loss(y,y_hat):
    N = y.shape[0]
    loss = -1/N * np.sum((y*np.log(y_hat) + (1 - y)*np.log(1-y_hat)))
    return loss  

W = 2*np.random.random((3,1)) - 1
b = 0

alpha = 1
epochs = 20

N = y.shape[0]
losses = []

for i in range(epochs):
    # Forward pass
    z = X.dot(W) + b
    A = sigmoid(z)
# Calculate loss
    loss = bce_loss(y,A)
    print('Epoch:',i,'Loss:',loss)
    losses.append(loss)
# Calculate derivatives
    dz = (A - y)
    dW = 1/N * np.dot(X.T,dz)
    db = 1/N * np.sum(dz,axis=0,keepdims=True)
# Parameter updates
    W -= alpha * dW
    b -= alpha * db

plt.plot(losses)
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

'''

'''
z1 = X.dot(W1) + b1

a1 = np.tanh(z1)

z1 = a1.dot(W2) + b2

a2 = sigmoid(z2)

# Calculate loss derivative with respect to the output
dz2 = bce_derivative(y=y,y_hat=a2)
# Calculate loss derivative with respect to second layer weights
dW2 = (a1.T).dot(dz2)

# Calculate loss derivative with respect to second layer bias
db2 = np.sum(dz2, axis=0, keepdims=True)
# Calculate loss derivative with respect to first layer
dz1 = dz2.dot(W2.T) * tanh_derivative(a1)
# Calculate loss derivative with respect to first layer weights
dW1 = np.dot(X.T, dz1)
# Calculate loss derivative with respect to first layer bias
db1 = np.sum(dz1, axis=0)
'''

model = Sequential()
model.add

model.add(Dense(3,input_dim=2))

model.add(Activation('tanh'))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.summary()

model.compile(optimizer='sgd',
    loss='binary_crossentropy',
    metrics=['acc'])

history = model.fit(X,y,epochs=900)












