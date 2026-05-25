import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# Load dataset
data = pd.read_csv(
    "data/KDDTrain+.txt",
    header=None
)

print("Dataset Loaded")

# Remove missing values
data.dropna(inplace=True)

# Encode text columns
for col in data.select_dtypes(include=['object']).columns:

    le = LabelEncoder()

    data[col] = le.fit_transform(
        data[col]
    )

print("Encoding Completed")

# Features
X = data.iloc[:, :-1]

# Labels
y = data.iloc[:, -1]

# Normalize features
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("Normalization Completed")

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

print("Dataset Split Completed")

# Create AI model
model = RandomForestClassifier(
    n_estimators=100
)

# Train model
model.fit(X_train, y_train)

print("Model Training Completed")

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(
    y_test,
    y_pred
)

print(f"Accuracy: {accuracy * 100:.2f}%")

# Report
print(classification_report(
    y_test,
    y_pred
))

# Save model
joblib.dump(
    model,
    "models/cybersecurity_model.pkl"
)

print("Model Saved Successfully")