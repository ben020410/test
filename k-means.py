# fundamental libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv("Data_1.csv")

# input for the process
data1_array = np.column_stack([data1['x1'], data1['x2']])

# visualization of the data
plt.scatter(data1['x1'], data1['x2'], marker='.', color='black', s=20)
plt.xlabel('X1', fontsize = 10)
plt.ylabel('X2', fontsize = 10)
plt.grid(True, alpha=0.3, linestyle="--")
plt.show()
