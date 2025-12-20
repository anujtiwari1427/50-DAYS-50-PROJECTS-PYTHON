message = input("Enter job message: ").lower()

scam_words = ["pay first", "registration fee", "urgent hiring"]

if any(word in message for word in scam_words):
    print("🚨 Job Scam Alert!")
else:
    print("✅ Seems Safe")
