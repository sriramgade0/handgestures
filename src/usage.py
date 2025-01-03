import cv2
import os
from utils import create_directory, display_frame_with_quit
from config import DATA_DIR, FRAME_WIDTH, FRAME_HEIGHT, GESTURES
import pickle

# Load the trained model
with open('models\\gesture_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def preprocess_image(image):
    """Preprocess the captured image and flatten it for model prediction"""
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize the image to 128x128 (or the size the model expects)
    resized = cv2.resize(gray, (128, 128))  # Adjust the size as per model training

    # Flatten the image to 1D (model expects a flat array, not a 2D image)
    flattened = resized.flatten()
    return flattened

def capture_gestures():
    """Capture gestures via webcam and predict gesture in real-time."""
    create_directory(DATA_DIR)
    
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    cap.set(3, FRAME_WIDTH)
    cap.set(4, FRAME_HEIGHT)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Preprocess the current frame for prediction
        processed_frame = preprocess_image(frame)

        # Make prediction using the model
        predicted_gesture = model.predict([processed_frame])  # Predict the gesture

        # Get the predicted label
        gesture_label = predicted_gesture[0]  # Gesture label
        
        # Display the frame with predicted label
        cv2.putText(frame, f'Predicted Gesture: {gesture_label}', (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        # Show the frame
        cv2.imshow('Gesture Prediction', frame)
        
        # Check for the 'q' key to quit the webcam feed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_gestures()
