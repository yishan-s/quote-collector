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

def add_quote(quotes):
    content = input("請輸入佳句：")
    author = input("請輸入作者（若無可直接 Enter）：")
    
    # 建立字典
    quote = {
        "content": content,
        "author": author if author else "Unknown"
    }
    
    quotes.append(quote)
    save_quotes(quotes) # 每次新增就存檔
    print("✅ 佳句已儲存！")

def show_quotes(quotes):
    if not quotes:
        print("📭 目前沒有任何佳句，快去採集吧！")
        return

    print(f"\n--- 目前共有 {len(quotes)} 句收藏 ---")
    for idx, q in enumerate(quotes, 1):
        print(f"{idx}. 「{q['content']}」 —— {q['author']}")
    print("----------------------------------\n")