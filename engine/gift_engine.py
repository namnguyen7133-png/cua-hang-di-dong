import json, random
import pandas as pd

def select_gift(boss):
    # Đọc dữ liệu quà và luật
    try:
        rules = json.load(open("rules/gift_rules.json", encoding="utf-8"))
        products = pd.read_csv("data/products.csv")
    except:
        return {"product_name": "Quà tặng may mắn", "product_link": "https://shopee.vn"}

    # Lọc quà theo đúng logic: ký tự cuối và số chữ trong tên
    for rule in rules.get("tie_breakers", []):
        if rule == "last_chars_match":
            match = products[products["last_char"] == boss["last_chars"]]
            if not match.empty: products = match
        elif rule == "word_count_match":
            match = products[products["word_count"] == boss["word_count"]]
            if not match.empty: products = match
        
        if len(products) == 1:
            return products.iloc[0]

    return products.sample(1).iloc[0]
