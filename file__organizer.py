import os
import shutil

def organize_folder(target_directory):
    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
        "Documents": [".pdf", ".docx", ".txt", ".csv", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi"],
        "Music": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".7z", ".tar"],
        "Executables": [".exe", ".msi"]
    }
    try:
        os.chdir(target_directory)
        files_moved = 0

        for file in os.listdir():
            if os.path.isdir(file):
                continue

            filename, extension = os.path.splitext(file)
            extension = extension.lower()

            for folder, extensions in file_categories.items():
                if extension in extensions:
                    if not os.path.exists(folder):
                        os.makedirs(folder)
                    shutil.move(file, os.path.join(folder, file))
                    print(f"Moved: {file} -> {folder}/")
                    files_moved += 1
                    break

        print(f"\nAll done! Sorted {files_moved} files.")

    except Exception as e:
        print(f"Whoops, something went wrong: {e}")

if __name__ == "__main__":
    print("--- TechnoHacks File Organizer ---")
    user_path = input("Type in the full path of the folder you want to organize: ")

    if os.path.exists(user_path):
        organize_folder(user_path)
    else:
        print("That path doesn't look right. Double-check the folder location and try again.")

