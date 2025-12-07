import os
import shutil


folder_path = input("Enter folder path: ")

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
}


for file in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file)

    
    if os.path.isdir(file_path):
        continue

    
    _, ext = os.path.splitext(file)

    moved = False

   
    for category, extensions in categories.items():
        if ext.lower() in extensions:
            category_folder = os.path.join(folder_path, category)

           
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

            
            shutil.move(file_path, category_folder)
            print(f"Moved {file} → {category}")
            moved = True
            break

   
    if not moved:
        other_folder = os.path.join(folder_path, "Others")

        if not os.path.exists(other_folder):
            os.makedirs(other_folder)

        shutil.move(file_path, other_folder)
        print(f"Moved {file} → Others")

print("\n✔ All files organized successfully!")
