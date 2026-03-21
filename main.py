import os
from google import genai

print(os.getenv("GEMINI_API_KEY", "未設定")[:15])

try:
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="介紹樹莓派5"
    )
    print(response.text)
except Exception as e:
    print(e)
