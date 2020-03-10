import numpy as np

M = np.array([[0.6, 0.0, 0.3, 0.1, 0.0],
              [0.0, 0.1, 0.9, 0.0, 0.0],
              [0.0, 0.0, 0.8, 0.0, 0.2],
              [0.0, 0.0, 0.5, 0.2, 0.3],
              [0.0, 0.4, 0.0, 0.0, 0.6]])
M = np.transpose(M)
v = np.array([1.0, 0.0, 0.0, 0.0, 0.0])

for i in range(20):
    M = np.matmul(M, M)

print(np.matmul(M, v))


M = np.array([[0.6, 0.0, 0.3, 0.1, 0.0],
              [0.0, 0.1, 0.9, 0.0, 0.0],
              [0.0, 0.0, 0.9, 0.0, 0.1],
              [0.0, 0.0, 0.5, 0.2, 0.3],
              [0.0, 0.4, 0.4, 0.0, 0.2]])
M = np.transpose(M)
v = np.array([1.0, 0.0, 0.0, 0.0, 0.0])

for i in range(20):
    M = np.matmul(M, M)

print(np.matmul(M, v))


M = np.array([[0.675, 0.075, 0.175, 0.075],
              [0.225, 0.325, 0.225, 0.225],
              [0.125, 0.125, 0.325, 0.425],
              [0.1, 0.5, 0.1, 0.3]])
M = np.transpose(M)
v = np.array([1.0, 0.0, 0.0, 0.0])

for i in range(20):
    M = np.matmul(M, M)

print(np.matmul(M, v))
