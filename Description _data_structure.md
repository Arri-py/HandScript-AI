# 🚀 ЁУ!

**Ща будет разбор полётов по структуре датасета**  
После серчинга, мозгового штурма и 3 чашек кофе родил систему, которая:  
✓ Кастомная под мой workflow  
✓ Масштабируется на 100500 конспектов  
✓ Не вызывает желания выкинуть ноут в окно  

## 📌 Где живет датасет?  
**[Гугл Диск](https://drive.google.com/drive/folders/17Wfp3kLH8beWT5GRcoV5iwuVch_BtTu1?usp=sharing)**

## � Структура-магистратура 

/project
│
├── /data                    # 📂 Всё что накопал/разметил
│   │
│   ├── /raw                 # 🗃️ "Сырые" данные:
│   │   │
│   │   ├── /text_detection   # 
│   │   │   ├── /images          # 📸 Фото конспектов
│   │   │   │   ├── notebook_001.jpg
│   │   │   │   ├── notebook_002.jpg
│   │   │   │   └── ...
│   │   │   │
│   │   │   └── /annotations     # Разметка в разных форматах
│   │   │       ├── /coco        # В формате COCO (annotations.json)
│   │   │       ├── /yolo        # В формате YOLO (.txt файлы)
│   │   │       └── /pascal_voc  # В формате VOC (.xml файлы)
│   │   │
│   │   └── /text_recognition    # Для модели распознавания символов
│   │       ├── /ru_а            # Пример: 50+ вариантов буквы "а"
│   │       │   ├── a_001.png    # Имя файла: символ_номер.расширение
│   │       │   ├── a_002.png
│   │       │   └── ...
│   │       ├── /ru_б
│   │       ├── ...
│   │       ├── /digits          # Цифры 0-9
│   │       │   ├── /1
│   │       │   │   ├── 1_001.png 
│   │       │   │   ├── 1_002.png 
│   │       │   │   └── ...
│   │       │   ├── /2
│   │       │   └── ...
│   │       ├── /punctuation     # Знаки препинания
│   │       │   ├── /punctuation_1
│   │       │   │   ├── punctuation_001.png 
│   │       │   │   ├── punctuation_002.png 
│   │       │   │   └── ...
│   │       │   ├── /punctuation_2
│   │       │   └── ...
│   │       └── /ambiguous       # Сложные/неразборчивые символы
│   │
│   ├── /processed           # Данные после предварительной обработки
│   │   ├── /document_detection
│   │   │   ├── /images      # Нормализованные изображения (одинаковый размер и т.д.)
│   │   │   └── /labels      # Преобразованные аннотации в едином формате
│   │   │
│   │   └── /text_recognition
│   │       ├── /augmented   # Аугментированные символы
│   │       └── /resized     # Символы приведенные к единому размеру
│   │
│   ├── /interim             # Промежуточные данные
│   │   ├── cropped_pages     # Вырезанные страницы после 1-й модели
│   │   └── text_blocks      # Обнаруженные текстовые блоки
│   │
│   └── /splits              # Разделение на обучающие/валидационные/тестовые наборы
│       ├── /document_detection
│       │   ├── train.txt
│       │   ├── val.txt
│       │   └── test.txt
│       └── /text_recognition
│           ├── train.csv    # Формат: путь_к_изображению,метка
│           ├── val.csv
│           └── test.csv
│
├── /models                 🤖 models/ # Сейвы обученных сеток
│   ├── /document_detection
│   │   ├── model_weights.h5
│   │   └── config.json
│   └── /text_recognition   
│       ├── crnn_model.pth
│       └── params.yaml
│
├── /notebooks              # Jupyter ноутбуки для анализа и экспериментов
│   ├── 1_Data_Exploration.ipynb
│   ├── 2_Document_Detection.ipynb
│   └── 3_Text_Recognition.ipynb
│
├── /scripts                # Вспомогательные скрипты
│   ├── data_preparation
│   │   ├── prepare_detection_data.py
│   │   └── augment_characters.py
│   ├── training
│   │   ├── train_detector.py
│   │   └── train_recognizer.py
│   └── utils
│       ├── visualization.py
│       └── metrics.py
│
└── /docs                   # всякое эдакое
    ├── Filq_1.md # Инструкция по разметке
    └── File_2.md    



