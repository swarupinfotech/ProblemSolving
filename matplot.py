import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Student': ['A', 'B', 'C', 'D'],
    'Marks': [70, 85, 60, 90]
}

df = pd.DataFrame(data)
print(df)

plt.bar(df['Student'], df['Marks'])
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()
