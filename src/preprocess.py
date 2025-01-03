import cv2
import os
import numpy as np
from config import DATA_DIR
def preprocess_image(image_path):
    """Preprocess the captured image and flatten it for model prediction"""
    # Convert to grayscale
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize the image to 128x128 (or the size the model expects)
    resized = cv2.resize(gray, (128, 128))  # Make sure this size matches model's training input

    # Flatten the image to a 1D array (model expects this)
    flattened = resized.flatten()  # This results in 16,384 features if the image is 128x128

    return flattened



def load_data():
    """Load and preprocess all data."""
    data = []
    labels = []

    for gesture in os.listdir(DATA_DIR):
        gesture_path = os.path.join(DATA_DIR, gesture)
        if not os.path.isdir(gesture_path):
            continue

        for img_file in os.listdir(gesture_path):
            img_path = os.path.join(gesture_path, img_file)
            img = preprocess_image(img_path)
            data.append(img)
            labels.append(gesture)

    return np.array(data), np.array(labels)
