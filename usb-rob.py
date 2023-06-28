import os
import shutil

def copy_files_to_usb(file_paths, usb_path):
    for file_path in file_paths:
        if os.path.exists(file_path):
            file_name = os.path.basename(file_path)
            destination = os.path.join(usb_path, file_name)
            shutil.copy2(file_path, destination)
            print(f"{file_path} başarıyla kopyalandı.")
        else:
            print(f"{file_path} bulunamadı.")

if __name__ == "__main__":
    # Kopyalanacak dosya yollarını ve USB bellek yolunu burada belirleyin
    file_paths = [
        "C:/"
    ]
    usb_path = "E:\\a"

    copy_files_to_usb(file_paths, usb_path)
