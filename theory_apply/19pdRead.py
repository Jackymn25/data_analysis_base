import requests
from bs4 import BeautifulSoup
import json
import time
import pandas as pd

URL = "https://quotes.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; demo-spider/1.0; +https://example.com/spider)"
}

def fetch_page(url):
    # get
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()  # not 200 is error
    return resp.text

def parse_quotes(html):
    soup = BeautifulSoup(html, "html.parser")
    quotes_data = []
    quote_divs = soup.select(".quote")
    for q in quote_divs:
        text = q.select_one(".text").get_text(strip=True)
        author = q.select_one(".author").get_text(strip=True)
        tags = [t.get_text(strip=True) for t in q.select(".tags .tag")]
        quotes_data.append({
            "text": text,
            "author": author,
            "tags": tags,
        })
    return quotes_data

def main():
    html = fetch_page(URL)
    data = parse_quotes(html)

    # json
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("已保存到 data.json，共抓取条数：", len(data))

    # sleep for next page
    time.sleep(1)

if __name__ == "__main__":
    main()

    # Task 01 read csv
    data = pd.read_csv("students_scores_named.csv")
    print(data.head())
    data['Total'] = data.math + data.English + data.science
    print(data.head())
    data.to_csv('Result.csv')

    # Task 02 Read results from web crawling
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    print(df.tail())
    print(df.tags.iloc[0][0])
