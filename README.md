# Quote Collector
Quote Collector is a command-line interface (CLI) tool built with Python, designed to help users collect, save, and review their favorite quotes at any time.
This project serves as a practice exercise to hone my Python skills, specifically focusing on the practical application of File I/O, JSON Data Handling, and Git VC

## Features
 * **Add Quotes:** Easily input quote content and author names; the system automatically saves the entry.
 * **Data Persistence:** Uses JSON format for storage, ensuring data is preserved even after the program is closed.
 * **Browse Collection:** Clearly lists all collected quotes and their authors.
 * **Error Handling:** Includes mechanisms to handle scenarios where data files do not exist or are formatted incorrectly (Robustness).

## Tech Stack
 * Language: Python 3
 * Data Storage: JSON
 * Version Control: Git

## Quick Start
### 1. Clone the Repository
```
git clone https://github.com/your-username/quote-collector.git
cd quote-collector
```
### 2. Run
```
python main.py
```

### 3. Example
```
=== 佳句採集器 ===
1. 新增佳句
2. 瀏覽佳句
3. 離開
請選擇功能 (1/2/3): 1
請輸入佳句：天下沒有白癡的晚餐
請輸入作者（若無可直接 Enter）：yishan-s
佳句已儲存！
=== 佳句採集器 ===
1. 新增佳句
2. 瀏覽佳句
3. 離開
請選擇功能 (1/2/3): 2
--- 目前共有 1 句收藏 ---
1. 「天下沒有白癡的晚餐」 —— yishan-s
----------------------------------
```
