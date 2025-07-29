# 🚀 ЁУ!
# docs/Description_data_structure.md 

**Как у нас всё лежит и зачем**  

## 📦 Где живёт датасет  
Google Drive:  
[https://drive.google.com/drive/folders/17Wfp3kLH8beWT5GRcoV5iwuVch_BtTu1?usp=sharing](https://drive.google.com/drive/folders/17Wfp3kLH8beWT5GRcoV5iwuVch_BtTu1?usp=sharing)  

Локально всё зеркалируется в `datasets/`.

---

## 📂 Итоговая локальная структура (`handwriting_recognition/`)
```
datasets/                       # ➊ корень всех данных
├── raw/                        # «как скачал» — не трогаем
│   ├── photos/                 # сырые фото конспектов (*.jpg, *.png)
│   ├── words/                  # разметка «bbox + текст слова»
│   └── letters/                # разметка «bbox + символ»
├── interim/                    # ➋ промежуточные артефакты
│   ├── crops/
│   │   ├── pages/              # вырезанные страницы
│   │   └── words/              # вырезанные слова
│   └── splits/                 # train/val/test *.txt / *.csv
└── processed/                  # ➌ готовое к обучению
├── detection/              # YOLO / COCO
│   ├── images/
│   └── labels/
└── recognition/            # 64×64 символы
├── images/
└── labels.csv          # image_id,label
models/                         # сохранённые чекпоинты
├── detection/
│   ├── best.pt
│   └── config.yaml
└── recognition/
├── crnn.pth
└── hparams.json
```
---

## 🗃️ Подробно по каждому уровню

| Уровень | Назначение | Правило |
|---------|------------|---------|
| **raw/photos** | Сырые сканы / фото тетрадей | Никогда не редактируются |
| **raw/words** | JSON / XML / TXT: bbox + transcription | Заливаем из Label Studio |
| **raw/letters** | JSON / XML / TXT: bbox + символ | Заливаем из Label Studio |
| **interim/crops/pages** | Автовырезанные страницы после детектора | Можно перегенерировать |
| **interim/crops/words** | Автовырезанные слова | Можно перегенерировать |
| **interim/splits** | train.txt / val.txt / test.txt | Генерируется скриптом |
| **processed/detection** | Нормализованные изображения + лейблы YOLO/COCO | Генерируется скриптом |
| **processed/recognition** | 64×64 символы, labels.csv | Генерируется скриптом |

---

## 🏷️ Схема именования файлов

| Тип | Пример имени | Пояснение |
|-----|--------------|-----------|
| Фото тетради | `nb_001.jpg` | `nb_<номер>` |
| Размеченное слово | `word_001.json` | `word_<id>.json` |
| Размеченная буква | `char_001.json` | `char_<id>.json` |
| Вырезанная страница | `page_001_003.png` | `page_<фото>_<номер_страницы>.png` |
| Вырезанное слово | `w_001_003_007.png` | `w_<фото>_<страница>_<номер_слова>.png` |
| Готовый символ | `a_00042.png` | `<символ>_<порядковый_номер>.png` |

---

## 🔄 Как данные попадают в обработку

1. **Скачивание**  
   `scripts/sync/download.py` → `datasets/raw`

2. **Детекция**  
   - `scripts/prepare_detection_ds.py`  
   - `raw/photos` → `processed/detection`

3. **Кроп слов**  
   - `scripts/crop_words.py`  
   - `processed/detection` → `interim/crops/words`

4. **Распознавание символов**  
   - `scripts/prepare_recognition_ds.py`  
   - `interim/crops/words` → `processed/recognition`

---

## 📊 Итоговые форматы лейблов

| Модель | Формат | Пример |
|--------|--------|--------|
| **Детектор (YOLO)** | `.txt` | `class x_center y_center width height` (нормированные) |
| **Детектор (COCO)** | `annotations.json` | стандарт COCO |
| **Распознаватель** | `labels.csv` | `image_id,label` |

---

## 🧹 Правила «чистоты»

- В `raw/` никогда не редактируем файлы вручную.  
- В `interim/` можно всё перегенерировать без потери данных.  
- В `processed/` только то, что готово к обучению.  
- Названия папок – строго **snake_case**, файлы – **строчные**, номера – **с ведущими нулями**.
