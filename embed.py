import qrcode

# ТВОЙ Instagram-URL
url = "https://www.instagram.com/0kam1_s3/?locale=ru"

# Создаём QR-код
img = qrcode.make(url)

# Сохраняем картинку
img.save("instagram_qr.png")

print("✅ QR-код сохранён как instagram_qr.png")
