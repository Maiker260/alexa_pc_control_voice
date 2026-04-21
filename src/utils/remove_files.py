import os

def remove_files(directory, files):
    for file in files:
        path = os.path.join(directory, file)

        try:
            if os.path.exists(path):
                os.remove(path)
                print(f"{file} deleted.")
            else:
                print(f"{file} not found, skipping.")
        except Exception as e:
            print(f"Error deleting {file}: {e}")