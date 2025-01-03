# src/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Directory paths
DATA_DIR = os.getenv("DATA_DIR", "./data")
MODEL_DIR = os.getenv("MODEL_DIR", "./models")

# Camera settings
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Define gestures to capture
GESTURES = ["thumbs_up", "thumbs_down", "ok_sign"]
