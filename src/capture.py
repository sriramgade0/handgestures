import cv2
import os
from utils import create_directory, display_frame_with_quit
from config import DATA_DIR, FRAME_WIDTH, FRAME_HEIGHT, GESTURES
import pickle

# Load the saved model
with open('models\\gesture_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def capture_gestures():
    create_directory(DATA_DIR)
    
    # Initialize camera
    cap = cv2.VideoCapture(0)
    cap.set(3, FRAME_WIDTH)
    cap.set(4, FRAME_HEIGHT)

    for gesture in GESTURES:
        gesture_path = os.path.join(DATA_DIR, gesture)
        create_directory(gesture_path)
        print(f"Capturing {gesture}...")

        count = 0
        while count < 100:  # Collect 100 samples per gesture
            ret, frame = cap.read()
            if not ret:
                break

            # Display the captured frame
            if display_frame_with_quit(frame, f"Capture {gesture}"):
                img_path = os.path.join(gesture_path, f"{gesture}_{count}.jpg")
                cv2.imwrite(img_path, frame)

                # Preprocess the captured frame for prediction (assuming you have a preprocess function)
                processed_frame = preprocess_image(frame)

                # Use the model to predict the gesture
                predicted_gesture = model.predict([processed_frame])  # Process frame into a suitable shape
                print(f"Predicted gesture: {predicted_gesture[0]}")

                count += 1
            else:
                break

    cap.release()
    cv2.destroyAllWindows()

def preprocess_image(image):
    """Preprocess the captured image and flatten it for model prediction"""
    # Convert to grayscale, resize, and flatten it for the model
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (64, 64))  # Assuming your model uses 64x64 images
    flattened = resized.flatten()  # Flatten image
    return flattened

if __name__ == "__main__":
    capture_gestures()
