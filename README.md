# 🖋️ HandScript-AI

![schema](docs\assets\images.png)


«Что тут вообще происходит»
## 📌 TL;DR
Две нейронки:
1. Детектор – находит рукописный текст на фото.
2. Распознаватель – читает найденный текст посимвольно.

Данные живут на Google Drive.
Локально всё зеркалируется в datasets/.
Размечаем в Label Studio (инструкция в docs/label-studio.md).
___

## 🗂️ Структура проекта
```
handwriting_recognition/
├── symbols                 # все символы/буквы
├── data/                   # ВСЕ ДАННЫЕ
│   ├── raw/                # как скачал
│   ├── interim/            # вырезанные куски, сплиты
│   └── processed/          # то, что жрёт модель
├── models/                 # чекпоинты
├── notebooks/              # EDA, тренировки, эксперименты
├── src/                    # основной код
├── scripts/                # CLI-хелперы
├── docs/                   # доки
├── requirements.txt
└── environment.yml
```
[Подробно](docs/Description_data_structure.md)
___

## 🚀 Быстрый старт

(когданибудь допишу)

1. Conda
``` bash
# 1. Клонировать
git clone https://github.com/<you>/handwriting_recognition.git
cd handwriting_recognition

# 2. Создать окружение из готового файла
conda env create -f environment.yml   # в файле уже нужные версии

# 3. Активировать
conda activate handscript
```

2. pip + requirements.txt
``` bash
# 1. Клонировать (см. выше)

# 2. Создать venv
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 3. Установить
pip install -r requirements.txt
```

3. Проверка после восстановления
``` bash
conda env create -f environment.yml   # или
pip install -r requirements.txt
``` 
В новом окружении:
``` bash
python -c "import torch, cv2, label_studio; print('OK')"
``` 

3. Скачать датасет 
(скоро чет придумаю)
4. Поднять Label Studio
(Смотри – docs/label-studio.md)

---

## 🎯 Что уже есть / что делается
(*Пишу только для себя*)

|       Готово       |       В процессе       |
|--------------------|------------------------|
| ✅ Структура папок | 🔲 Структурирование данных |
| ✅ Label-Studio гайд | 🔲 Перенести все сырые данны на гугл диск |
| ✅ Какие то данные | 🔲 Перенести датасет слов с кагла на гугл диск | 
| ✅ Гайдик как воссоздать окружение |

___

## 📊 Статистика данных
|     Что     |  Кол-во  |  Примечание  |
|-------------|----------|--------------|
| Фото Конспектов | 3150 | |
| Размеченные слова | +- 72к | |
| Размеченные буквы | 0 |  |
| Размеченные символы | 0 |  |

___

## ❓FAQ
Q: Что со спец-символами?
A: Соберём после основного алфавита; пока ? → ambiguous/.

Q: Сколько видеокарты нужно?
A: Для 51k символов хватит и 6 ГБ VRAM; детектор можно на CPU.

Q: Когда будут данные?
A: ХЗ.

Q: Когда будет готово?
A: Когда то точно будет готово.
