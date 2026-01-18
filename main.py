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
    print("佳句已儲存！")

def show_quotes(quotes):
    if not quotes:
        print("📭 目前沒有任何佳句，快去採集吧！")
        return

    print(f"\n--- 目前共有 {len(quotes)} 句收藏 ---")
    for idx, q in enumerate(quotes, 1):
        print(f"{idx}. 「{q['content']}」 —— {q['author']}")
    print("----------------------------------\n")

def main():
    quotes = load_quotes()
    
    while True:
        print("\n=== 佳句採集器 ===")
        print("1. 新增佳句")
        print("2. 瀏覽佳句")
        print("3. 離開")
        
        choice = input("請選擇功能 (1/2/3): ")
        
        if choice == "1":
            add_quote(quotes)
        elif choice == "2":
            show_quotes(quotes)
        elif choice == "3":
            print("Bye Bye!")
            break
        else:
            print("無效輸入，請重試。")

if __name__ == "__main__":
    main()
