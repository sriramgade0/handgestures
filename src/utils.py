import os
import cv2
from dotenv import load_dotenv

def create_directory(path):
    """Create a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def read_env_variable(var_name, default=None):
    """Read environment variable from the .env file."""
    load_dotenv()
    return os.getenv(var_name, default)

def display_frame_with_quit(frame, window_name="Frame"):
    """Display a frame and quit on pressing 'q'."""
    cv2.imshow(window_name, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return False
    return True
