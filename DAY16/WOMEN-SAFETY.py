import time

panic = input("Press P if in danger: ")

if panic.lower() == "p":
    print("📍 Sending location to emergency contacts...")
    time.sleep(2)
    print("🚔 Help Alert Sent!")
