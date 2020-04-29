import requests
import json
import glob


class times_analizer:
    def __init__(self, path):
        self.path = path
        self.counter = {}
        self.owner_name = self.get_ownername()
        
    def get_username(self, utterance):
        try:
            return utterance["user_profile"]["real_name"]
        except:
            return False

    def get_text(self, utterance):
        return utterance["text"]
    
    def get_userID(self, utterance):
        return utterance["user"]

    def get_ownername(self):
        def request_ownername(ownerID):
            headers = {"Content-Type":"application/x-www-form-urlencoded"}
            params = {"token":"Bot User OAuth Access Token", "user":ownerID}
            r = requests.get("https://slack.com/api/users.profile.get", headers=headers, params=params)
            owner_name = r.json()["profile"]["real_name"]
            return owner_name

        daily_json = self.daily_json_gen()
        oneday_json = daily_json.__next__() #最初の日のjsonだけ取得
        ownerID = self.get_userID(oneday_json[0]) # 一番最初はchannel_joinなのでそのuserがチャンネル作成者
        owner_name = request_ownername(ownerID)
        if owner_name == "Shunya Takayanagi":
            ownerID = self.get_userID(oneday_json[1]) # さわやくん,五十嵐ユウダイくん用
            owner_name = request_ownername(ownerID)
        if owner_name == "YUKI MINO":
            ownerID = self.get_userID(oneday_json[2]) # 五十嵐未来さん用
            owner_name = request_ownername(ownerID)
        if owner_name == "takeru hayasaka":
            ownerID = self.get_userID(oneday_json[0]) # 高柳さん用
            owner_name = request_ownername(ownerID)
        return owner_name

    def daily_json_gen(self):
        for oneday_path in self.path:
            with open(oneday_path, "r", encoding="utf-8") as f:
                daily_json = json.load(f)
                try:
                    yield daily_json
                except:
                    break
        
    def count_remarks_per_member(self):
        daily_json = self.daily_json_gen()
        for oneday_json in daily_json:
            for utterance in oneday_json:
                user_name = self.get_username(utterance)
                if not user_name or user_name == self.owner_name : 
                    continue # ユーザーネームがない、もしくは発言者がチャンネルのオーナーのときはcontinue
                try:
                    self.counter[user_name] += 1
                except:
                    self.counter[user_name] = 1
        return self.counter


if __name__ == "__main__":
    analizer = times_analizer("./mather_data/times_yusuke_takahashi/*")
    r = analizer.get_ownername()
    print(r)

                

