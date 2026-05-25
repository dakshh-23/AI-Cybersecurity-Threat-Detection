import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv(
    "data/KDDTrain+.txt",
    header=None
)

print("Dataset Loaded Successfully")

# Remove missing values
data.dropna(inplace=True)

# Encode ONLY object/string columns
for col in data.select_dtypes(include=['object']).columns:

    le = LabelEncoder()

    data[col] = le.fit_transform(data[col])

print("Encoding Completed")

# Features and labels
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Normalize features
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("Normalization Completed")

print("Shape:")
print(X_scaled.shape)

print("Preprocessing Successful")