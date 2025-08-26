import pandas as pd
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris(as_frame=True)
df = iris.frame

# Save into data folder
df.to_csv("data/iris.csv", index=False)

print("✅ Iris dataset saved in data/iris.csv")
