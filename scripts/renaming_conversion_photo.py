"""
че оно делает 
берет все файла из папки 
делает еще папку переименовывает файлы и меняет формат 
выглядит как то вот так < photo_0001.jpg >
потом переносит в все в указанную папку и удалает которую создает 
вот и все
"""


import os
from PIL import Image

def process_images(root_folder, output_format='jpg'):
    image_files = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith(('.jpeg', '.jpg', '.png')):
                image_files.append(os.path.join(root, file))
    
    temp_folder = os.path.join(root_folder, "temp_rename")
    os.makedirs(temp_folder, exist_ok=True)
    
    for i, old_path in enumerate(image_files, start=1):
        try:
            # Временное имя файла
            temp_name = f"temp_{i:04d}.{output_format.lower()}"
            temp_path = os.path.join(temp_folder, temp_name)
            
            # Новое постоянное имя
            new_name = f"photo_{i:04d}.{output_format.lower()}"
            new_path = os.path.join(root_folder, new_name)
            
            with Image.open(old_path) as img:
                if output_format.lower() in ('jpg', 'jpeg'):
                    img.convert('RGB').save(temp_path, 'JPEG', quality=95)
                elif output_format.lower() == 'png':
                    img.save(temp_path, 'PNG')
            
            os.remove(old_path)
            
            print(f"Обработано: {os.path.basename(old_path)} -> {new_name}")         # закоментируй если не нравится
            
        except Exception as e:
            print(f"Ошибка в файле {os.path.basename(old_path)}: {str(e)}")
    
    for temp_file in os.listdir(temp_folder):
        temp_path = os.path.join(temp_folder, temp_file)
        new_name = f"photo_{int(temp_file[5:9]):04d}.{output_format.lower()}"
        new_path = os.path.join(root_folder, new_name)
        os.rename(temp_path, new_path)
    
    os.rmdir(temp_folder)

if __name__ == "__main__":
    # относительный путь к папке с изображениями 
    folder_path = r"data\raw\photos\raw_notes_test"
    
    # выбери формат в который преобразуются все фотографии ('jpg' или 'png') 
    desired_format = 'jpg'  
    
    process_images(folder_path, desired_format)
    print("Ну че все готово")