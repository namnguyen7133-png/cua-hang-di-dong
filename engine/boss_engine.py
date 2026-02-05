import json, random
import pandas as pd

def select_boss(today_element):
    # Đọc dữ liệu từ repo
    try:
        friends = pd.read_csv("data/friends.csv")
        switches = json.load(open("rules/switches.json", encoding="utf-8"))
        rules = json.load(open("rules/boss_rules.json", encoding="utf-8"))
    except Exception as e:
        print(f"❌ Lỗi đọc file: {e}")
        return None

    # Đọc history để tránh trùng Sếp cũ
    try:
        history = pd.read_csv("data/history.csv")
        past_bosses = history['boss_name'].tail(5).tolist()
    except:
        past_bosses = []

    candidates = friends.copy()
    if 'name' in candidates.columns:
        candidates = candidates[~candidates['name'].isin(past_bosses)]
    
    if candidates.empty: 
        candidates = friends.copy()

    # Lọc theo luật mệnh Ngày > Tuần > Tháng
    for level in rules.get("priority_order", []):
        if not switches.get(f"use_{level}", True):
            continue
        if level in candidates.columns:
            temp = candidates[candidates[level] == today_element]
            if len(temp) == 1: return temp.iloc[0]
            if len(temp) > 1: candidates = temp

    # Nếu vẫn còn nhiều người, chọn người điểm cao nhất
    if switches.get("use_5_pillars_score", True):
        score_col = f"score_{today_element}"
        if score_col in candidates.columns:
            max_score = candidates[score_col].max()
            candidates = candidates[candidates[score_col] == max_score]

    return candidates.sample(1).iloc[0]
