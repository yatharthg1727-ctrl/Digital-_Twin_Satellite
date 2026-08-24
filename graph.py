import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

plt.plot(data["Battery"])

plt.title("Battery Trend")

plt.xlabel("Reading")

plt.ylabel("Battery")

plt.show()