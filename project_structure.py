import os

def save_project_structure(root_dir, output_file='project_structure.txt'):
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(root_dir):
            level = root.replace(root_dir, '').count(os.sep)
            indent = ' ' * 4 * level
            file.write(f"{indent}{os.path.basename(root)}/\n")
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                file.write(f"{subindent}{f}\n")
    print(f"Project structure saved to {output_file}")

if __name__ == "__main__":
    project_root = '.'  # Use '.' to point to the current directory
    save_project_structure(project_root)



#exit
