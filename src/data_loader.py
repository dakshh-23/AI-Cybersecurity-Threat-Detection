import pandas as pd

# Load dataset
data = pd.read_csv(
    "data/KDDTrain+.txt",
    header=None
)

# Show first 5 rows
print("First 5 Rows:\n")

print(data.head())

# Show dataset shape
print("\nDataset Shape:\n")

print(data.shape)

# Show column information
print("\nDataset Information:\n")

print(data.info())