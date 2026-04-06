from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

try:
    client = OpenAI(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com"
    )
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": "用100字繁體中文介紹樹莓派5硬體規格"}
        ]
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"發生錯誤：{e}")