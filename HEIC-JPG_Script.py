import os
from PIL import Image

def convert_heic_to_jpg(heic_path, jpg_path):
    try:
        img = Image.open(heic_path)
        img.save(jpg_path, "JPEG")
        print(f"Converted {heic_path} to {jpg_path}")
    except Exception as e:
        print(f"Error converting {heic_path}: {e}")

def main(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    heic_files = []  # List to store HEIC files

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".heic"):
            heic_files.append(filename)

    if not heic_files:
        print(f"No HEIC files found in the folder '{folder_path}', now move to the next folder.")
    else:
        print(f"Detected {len(heic_files)} HEIC file(s) in the folder '{folder_path}'. Converting...")

        for heic_filename in heic_files:
            heic_path = os.path.join(folder_path, heic_filename)
            jpg_filename = os.path.splitext(heic_filename)[0] + ".jpg"
            jpg_path = os.path.join(folder_path, jpg_filename)
            convert_heic_to_jpg(heic_path, jpg_path)

if __name__ == "__main__":
    folder_path = r"2023\06-June\29-06-23"  # Change this to your desired folder path
    #Finished till here
    main(folder_path)
