fake_words = ["shocking", "secret", "must watch", "breaking"]

news = input("Enter news headline: ").lower()

if any(word in news for word in fake_words):
    print("⚠️ Possibly Fake News")
else:
    print("✅ Looks Legit")
