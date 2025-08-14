import base64
import cv2
from pyzbar.pyzbar import decode
from pathlib import Path

# === Настройки ===
image_path = "qr_photo.jpg"  # сюда укажи путь к фото QR-кода

# Проверка существования файла
if not Path(image_path).is_file():
    print(f"Файл '{image_path}' не найден")
    exit()

# Загружаем изображение
image = cv2.imread(image_path)

# Пробуем распознать QR
decoded_objects = decode(image)

if not decoded_objects:
    print("QR-код не найден. Попробуй сделать фото чётче или обрезать лишнее.")
    exit()

# Берём данные из первого найденного QR
encoded_data = decoded_objects[0].data.decode("utf-8")

# Декодируем Base64 обратно в бинарный файл
file_data = base64.b64decode(encoded_data)

# Сохраняем в файл
output_file = "restored_script.py"
with open(output_file, "wb") as f:
    f.write(file_data)

print(f"✅ Файл восстановлен как '{output_file}'")
