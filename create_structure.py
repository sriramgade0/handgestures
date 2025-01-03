import os

def create_project_structure(base_dir):
    structure = {
        "data": [],
        "models": [],
        "src": ["utils.py", "train.py", "predict.py", "preprocess.py", "capture.py", "config.py"],
        "tests": [],
        ".env": None,
        "requirements.txt": None,
        "README.md": None
    }

    def create_items(root, structure_dict):
        for folder, items in structure_dict.items():
            folder_path = os.path.join(root, folder)
            os.makedirs(folder_path, exist_ok=True)
            if isinstance(items, list):  # If the folder contains files or subdirectories
                for item in items:
                    # If the item ends with .py, it's a file
                    if isinstance(item, str) and item.endswith('.py'):
                        with open(os.path.join(folder_path, item), 'w') as f:
                            pass  # Create the Python file
                    elif isinstance(item, str) and not item.endswith('.py'):
                        # It's an empty directory
                        os.makedirs(os.path.join(folder_path, item), exist_ok=True)
            elif items is None:  # File with no subitems
                with open(os.path.join(root, folder), 'w') as f:
                    pass  # Create an empty file
    
    # Create the root project directory
    os.makedirs(base_dir, exist_ok=True)
    create_items(base_dir, structure)

if __name__ == "__main__":
    create_project_structure("hand_gesture_recognition")
