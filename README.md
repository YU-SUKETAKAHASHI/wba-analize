## wba東北支部のslackにおける人物相関の解析

### 事前準備
```
git clone https://github.com/YU-SUKETAKAHASHI/wba-analize
```
リポジトリをクローンした後、slackの発言データをエクスポートしたフォルダ(mather_data)をgen_correlation.pyと同階層に配置する。

### timesでの人間相関ネットワークを作成する
```
python gen_correlation.py
python visualize_network.py
```
gen_correlation.pyを実行すると、以下のようなjsonファイル(correlation.json)が作成される。
visualize_network.pyを実行して、jsonファイルを読み込みグラフに描画する。
```
{"timesAの主": {"メンバーB": 発言回数, "メンバーC": 100, "メンバーD": 36, "メンバーE": 2}, 
"timesBの主": {"メンバーA": 261, "メンバーC": 352, "メンバーF": 5, "メンバーG": 26, "メンバーH": 13}
"timesCの主": {"メンバーA": 13, "メンバーD": 3, "メンバーE": 4, "メンバーF": 3, "メンバーG": 1}, 
・・・
"timesZの主": {"メンバーH": 1, "メンバーT": 5}, }
```

## timesの頻出単語を出力する
```
準備中・・・
```
