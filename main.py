import json
import os

DATA_FILE = "quotes.json"

def load_quotes():
    # 如果檔案不存在，回傳空列表
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_quotes(quotes):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        # ensure_ascii=False 讓中文能正常顯示
        json.dump(quotes, f, ensure_ascii=False, indent=4)