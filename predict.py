import pickle
import cv2
import os
import numpy as np
from preprocess import preprocess_image
from config import MODEL_DIR
from utils import display_frame_with_quit

def predict_gesture():
    model_path = os.path.join(MODEL_DIR, "gesture_model.pkl")
    with open(model_path, "rb") as f:
        clf = pickle.load(f)

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = preprocess_image(frame)
        prediction = clf.predict(processed_frame.flatten().reshape(1, -1))
        print(f"Predicted Gesture: {prediction}")

        if not display_frame_with_quit(frame, "Prediction"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    predict_gesture()
