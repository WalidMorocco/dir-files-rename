import os

def rename_files_in_directory(directory_path, old_char, new_char):
    # Walk through directory_path, including its subdirectories
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            # Check if filename contains the character/string to be replaced
            if old_char in filename:
                # Create the new filename by replacing old_char with new_char
                new_filename = filename.replace(old_char, new_char)
                # Get the full path for both old and new filenames
                old_file_path = os.path.join(dirpath, filename)
                new_file_path = os.path.join(dirpath, new_filename)
                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed {old_file_path} to {new_file_path}")

if __name__ == "__main__":
    dir_path = input("Enter the directory path: ")
    char_to_replace = input("Enter the character or string you want to replace: ")
    replacement_char = input("Enter the character or string you want to replace it with: ")
    rename_files_in_directory(dir_path, char_to_replace, replacement_char)
