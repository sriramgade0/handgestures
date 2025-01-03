import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from preprocess import load_data
from config import MODEL_DIR
from utils import create_directory
import pickle
import os

def train_model():
    data, labels = load_data()
    X_train, X_test, y_train, y_test = train_test_split(data.reshape(len(data), -1), labels, test_size=0.2, random_state=42)

    # Train a classifier
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train, y_train)

    # Evaluate the model
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Save the model
    create_directory(MODEL_DIR)
    model_path = os.path.join(MODEL_DIR, "gesture_model.pkl")
    with open(model_path, "wb") as f:
        pickle.dump(clf, f)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model()
