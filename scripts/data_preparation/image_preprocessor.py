import cv2
import os
import numpy as np
from tqdm import tqdm

def convert_to_bw(input_dir, output_dir, threshold=180):
    """
    Конвертирует все изображения в папке в чёрно-белые с адаптивной бинаризацией
    :param input_dir: Папка с исходными изображениями
    :param output_dir: Папка для результатов
    :param threshold: Порог бинаризации (0-255)
    """
    os.makedirs(output_dir, exist_ok=True)
    
    for root, _, files in os.walk(input_dir):
        for file in tqdm(files, desc="Обработка изображений"):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff')):
                # Создаем аналогичную структуру папок
                rel_path = os.path.relpath(root, input_dir)
                os.makedirs(os.path.join(output_dir, rel_path), exist_ok=True)
                
                # Обработка изображения
                img_path = os.path.join(root, file)
                img = cv2.imread(img_path)
                
                # Конвертация в grayscale
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                
                # Адаптивная бинаризация
                bw = cv2.adaptiveThreshold(
                    gray, 255,
                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                    cv2.THRESH_BINARY_INV,
                    blockSize=21,
                    C=7
                )
                
                output_path = os.path.join(output_dir, rel_path, file)
                cv2.imwrite(output_path, bw)

input_folder = "data/data_1_test/raw/"  # Папка с исходными изображениями
output_folder = "data/data_1_test/processed/"  # Папка для чёрно-белых версий

convert_to_bw(input_folder, output_folder)