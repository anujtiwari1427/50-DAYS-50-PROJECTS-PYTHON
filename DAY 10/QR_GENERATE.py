import qrcode
import os
from datetime import datetime

data = input("Enter text or URL: ")

file_name = f"qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
qr = qrcode.make(data)
qr.save(file_name)

# Auto open file
os.startfile(file_name)

print("🎉 QR Code opened automatically!")

