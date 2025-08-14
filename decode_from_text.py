import base64

# Сюда вставь строку из сканированного QR
encoded_data = """cHJpbnQoIkhlbGxvIGZyb20gUV...B7aX0iKQ0K"""  # ← вставь полный текст

# Декодируем Base64 в байты
file_data = base64.b64decode(encoded_data)

# Сохраняем в .py файл
with open("restored_script.py", "wb") as f:
    f.write(file_data)

print("✅ Файл сохранён как 'restored_script.py'")
