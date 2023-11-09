import os

def open_output_folder():
    folder_path = "logs/"
    if os.name == "nt":
        folder_path = folder_path.replace('/', '\\')
        os.system(f"start explorer {folder_path}")

if __name__ == '__main__':
    print(':v')