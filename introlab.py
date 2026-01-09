import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arr = np.array([1, 2, 3, 4])
print("Numpy Array:", arr)

data = {'Name': ['A', 'B', 'C'], 'Marks': [80, 85, 90]}
df = pd.DataFrame(data)
print(df)

plt.plot(arr)
plt.title("Simple Plot")
plt.show()
