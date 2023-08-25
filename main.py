import os

def rename_files_and_dirs(directory_path, old_char, new_char, recursive=False):
    if recursive:
        # Start from the deepest directories to ensure we don't disrupt the os.walk traversal
        for dirpath, dirnames, filenames in sorted(os.walk(directory_path, topdown=False), key=lambda x: x[0]):
            # Rename files
            for filename in filenames:
                rename_if_needed(dirpath, filename, old_char, new_char)

            # Rename subdirectories
            for dirname in dirnames:
                rename_if_needed(dirpath, dirname, old_char, new_char)
    else:
        # Only process files in the top-level directory
        for name in os.listdir(directory_path):
            rename_if_needed(directory_path, name, old_char, new_char)

def rename_if_needed(dirpath, name, old_char, new_char):
    if old_char in name:
        # Create the new name by replacing old_char with new_char
        new_name = name.replace(old_char, new_char)
        # Get the full path for both old and new names
        old_path = os.path.join(dirpath, name)
        new_path = os.path.join(dirpath, new_name)
        # Rename the file or directory
        os.rename(old_path, new_path)
        print(f"Renamed {old_path} to {new_path}")

if __name__ == "__main__":
    dir_path = input("Enter the directory path: ")
    char_to_replace = input("Enter the character or string you want to replace: ")
    replacement_char = input("Enter the character or string you want to replace it with: ")
    recursive_choice = input("Do you want to rename files and subdirectories inside subdirectories as well? (yes/no): ").strip().lower()
    recursive = recursive_choice == "yes"
    rename_files_and_dirs(dir_path, char_to_replace, replacement_char, recursive)
