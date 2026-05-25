import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv(
    "data/KDDTrain+.txt",
    header=None
)

# Count attack types
attack_counts = data[41].value_counts().head(10)

# Create graph
attack_counts.plot(kind='bar')

# Titles
plt.title("Top 10 Attack Types")

plt.xlabel("Attack Type")

plt.ylabel("Count")

# Show graph
plt.show()