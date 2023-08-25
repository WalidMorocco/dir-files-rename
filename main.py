import os

def rename_files_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if "_" in filename:
            new_filename = filename.replace("_", "-")
            old_file_path = os.path.join(directory_path, filename)
            new_file_path = os.path.join(directory_path, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    dir_path = input("Enter the directory path: ")
    rename_files_in_directory(dir_path)
print("Hello World")