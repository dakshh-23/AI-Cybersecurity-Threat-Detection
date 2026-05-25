import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

print("[*] Generating dummy cybersecurity dataset for training...")
# Ek random realistic dataset generate kar rahe hain training ke liye
np.random.seed(42)
X_normal = np.random.normal(loc=[300, 0, 20], scale=[50, 0.5, 5], size=(4000, 3))
X_attack = np.random.normal(loc=[1300, 8, 400], scale=[100, 2, 50], size=(1000, 3))
X = np.vstack((X_normal, X_attack))
y = np.array([0]*4000 + [1]*1000)

print("[*] Training the Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Model ko save kar rahe hain root directory me
model_path = "cybersecurity_model.pkl"
joblib.dump(model, model_path)
print(f"[+] Success! '{model_path}' file generated in your project folder.")