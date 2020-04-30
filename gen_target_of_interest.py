import glob
import json
from times_analizer import times_analizer
from collections import Counter


# slackからエクスポートしたデータのパスを読み込む
path = glob.glob("./mather_data/*")
times_path = [path_ for path_ in path if "times" in path_]
print(len(times_path))

# 各times毎に、誰が何回ずつ発言しているかを辞書に格納
all_data = {}
for earh in [times_path[26]]:
    daily_path = glob.glob(earh+"/*")

    analizer = times_analizer(daily_path)
    data = analizer.count_words()
    # print(data)
    c_ayami = Counter(data)
    print(c_ayami.most_common())
    # print(c_ayami.get)

    

# jsonファイルに書き込み
# with open("correlation.json", "w", encoding="utf-8") as f:
#     json.dump(all_data, f, ensure_ascii=False)