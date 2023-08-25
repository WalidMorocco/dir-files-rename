import os

def rename_files_in_directory(directory_path, old_char, new_char):
    # List all files in the directory
    for filename in os.listdir(directory_path):
        # Check if filename contains the character/string to be replaced
        if old_char in filename:
            # Create the new filename by replacing old_char with new_char
            new_filename = filename.replace(old_char, new_char)
            # Get the full path for both old and new filenames
            old_file_path = os.path.join(directory_path, filename)
            new_file_path = os.path.join(directory_path, new_filename)
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    dir_path = input("Enter the directory path: ")
    char_to_replace = input("Enter the character or string you want to replace: ")
    replacement_char = input("Enter the character or string you want to replace it with: ")
    rename_files_in_directory(dir_path, char_to_replace, replacement_char)
