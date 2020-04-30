import glob
import json
from times_analizer import times_analizer

# slackからエクスポートしたデータのパスを読み込む
path = glob.glob("./mather_data/*")
times_path = [path_ for path_ in path if "times" in path_]
print(len(times_path))

# 各times毎に、誰が何回ずつ発言しているかを辞書に格納
all_data = {}
for earh in times_path:
    daily_path = glob.glob(earh+"/*")

    analizer = times_analizer(daily_path)
    data = analizer.count_remarks_per_member()
    owner_name = analizer.get_ownername()
    all_data[owner_name] = data
    print(f"{owner_name} 終わり～")

# jsonファイルに書き込み
with open("correlation.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False)