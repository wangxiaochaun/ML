import numpy as np

randMat = np.mat(np.random.rand(4, 4))

inverseRandMat = randMat.I

multiplyMat = randMat * inverseRandMat

error = multiplyMat - np.eye(4)

print(error)