import qrcode
import base64

# 1. Читаем файл в бинарном виде
with open("my_script.py", "rb") as f:
    file_data = f.read()

# 2. Кодируем в base64
encoded_data = base64.b64encode(file_data).decode("utf-8")

# 3. Генерируем QR с данными
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(encoded_data)
qr.make(fit=True)

# 4. Сохраняем картинку
img = qr.make_image(fill_color="black", back_color="white")
img.save("my_script_qr.png")

print("QR-код сохранён в 'my_script_qr.png'")
