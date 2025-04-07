# 🚀 Оу-у! Ща поднимем Label Studio

Ща кратко и по делу как поднять Label Studio, чтоб не е*#%ться с разметкой

### 🖥️ Че ДЕЛАЕМ:
1. **Cоздаем окружение**:
```bash
conda create --name label-studio
```

2. **Смотрим. Если на горизонте ошибки (см по ситуации)**:
```bash
conda create -n label-studio python=3.8
```

3. **Залетаем в окружение**:
```bash
conda activate label-studio
```

4. **ЗАПУСКАЕМ МОЗГОПРАК (старт сервера)**:

    1. **Простой вариант**:
    ```bash
    label-studio
    ```
    2. **Тут что то на харде**:
    ```bash
    label-studio start my_handwriting_project \
      --init \
      --template image_bbox \
      --user-email мыло@waaa.ru
    ```

### 🔥 ЧТО ПОЛУЧАЕМ:
- Локально: http://localhost:8080
- По сети: http://твой_ip:8080 
- Если ненравятся порты то: Ручками! Меняем ручками!

### 💾 КОМАНДЫ НА ЗАКРЕП:
```bash
# Экспорт в COCO (чтоб нейронка жрала)
label-studio export --format COCO --output-dir ./exported_data

# Сброс пароля (если опять забыл)
label-studio reset-password -e мыло@waaa.ru
```

### ⚠️ ПРО ВАЖНОЕ:
- Для команды запускаем с --host 0.0.0.0
- Лучше ставить на линукс (на винде могут быть костыли)
- Перед разметкой выпить кофе b и запастись терпением (без шуток)