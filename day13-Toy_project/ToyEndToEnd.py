# ==============================
# 1. Import Libraries
# ==============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from mlxtend.plotting import plot_decision_regions
import pickle


# ==============================
# 2. Load Dataset
# ==============================
df = pd.read_csv("ml2.csv")

# Remove unnecessary first column (if index-like)
df = df.iloc[:, 1:]

# Display dataset
print("Dataset:\n", df)


# ==============================
# 3. Data Visualization
# ==============================
plt.scatter(df['CGPA'], df['IQ'], c=df['Placement'])  # c means comour coding 
plt.xlabel("CGPA")
plt.ylabel("IQ")
plt.title("CGPA vs IQ (Placement)")
plt.show()


# ==============================
# 4. Split Features & Target
# ==============================
X = df[['CGPA', 'IQ']]   # Features
y = df['Placement']      # Target


# ==============================
# 5. Train-Test Split
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42
)


# ==============================
# 6. Feature Scaling
# ==============================
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# ==============================
# 7. Train Model
# ==============================
model = LogisticRegression()
model.fit(X_train, y_train)


# ==============================
# 8. Make Predictions
# ==============================
y_pred = model.predict(X_test)

print("\nActual Values:\n", y_test.values)
print("\nPredicted Values:\n", y_pred)


# ==============================
# 9. Model Accuracy
# ==============================
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)


# ==============================
# 10. Decision Boundary Plot
# ==============================
plot_decision_regions(
    X=X_train,
    y=y_train.values.astype(int),
    clf=model,
    legend=2
)

plt.xlabel("CGPA")
plt.ylabel("IQ")
plt.title("Decision Boundary")
plt.show()


# ==============================
# 11. Save Model
# ==============================
pickle.dump(model, open('model.pkl', 'wb'))