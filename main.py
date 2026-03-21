import os
from dotenv import load_dotenv  # 新增這行
from google import genai

# 自動搜尋並讀取同目錄下的 .env 檔案
load_dotenv() 

try:
    # Client 會自動從環境變數抓取 GOOGLE_API_KEY
    client = genai.Client() 
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite-preview-02-05", # 建議用這個穩定版本
        contents="用100自字自繁體中文樹莓派5硬體規格"
    )
    print(response.text)
except Exception as e:
    print(f"發生錯誤：{e}")
