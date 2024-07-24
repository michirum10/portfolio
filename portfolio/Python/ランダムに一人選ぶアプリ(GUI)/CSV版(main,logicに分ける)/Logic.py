import random  # ランダムな選択を行うためのモジュールをインポート
import csv  # CSVファイルの読み書きを行うためのモジュールをインポート

# ファイルパスの定義
data_file = "names_data.csv"  # 名前を保存するCSVファイルのパス
picked_file = "picked_names_data.csv"  # 選ばれた名前データを保存するCSVファイルのパス

class NameManager:
    def __init__(self):
        self.names = []  # 登録された名前を格納するリスト
        self.picked_names = []  # 選ばれた名前を格納するリスト
        self.load_data()  # データをロード

    def load_data(self):
        self.names = self._load_csv(data_file)  # 名前データをCSVファイルから読み込む
        self.picked_names = self._load_csv(picked_file)  # 選ばれた名前データをCSVファイルから読み込む

    def _load_csv(self, filename):
        try:
            with open(filename, mode='r', encoding='utf-8-sig') as f:
                return [row[0] for row in csv.reader(f)]  # CSVファイルの各行の最初の要素をリストに追加
        except FileNotFoundError:
            with open(filename, mode='w', newline='', encoding='utf-8-sig') as f:
                pass  # ファイルが存在しない場合、新しいファイルを作成
            return []

    def save_picked_data(self):
        self._save_csv(picked_file, self.picked_names)  # 選ばれた名前データをCSVファイルに保存

    def _save_csv(self, filename, data):
        with open(filename, mode='w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)  # CSVファイルに書き込むためのwriterオブジェクトを作成
            for item in data:
                writer.writerow([item])  # 各データをCSVファイルに書き込む

    def register_name(self, name):
        if name and name not in self.names:
            self.names.append(name)  # 新しい名前をリストに追加
            self._save_csv(data_file, self.names)  # 名前データをCSVファイルに保存
            return True
        return False

    def pick_random_name(self):
        remaining_names = [name for name in self.names if name not in self.picked_names]  # 選ばれていない名前のリストを作成
        if not remaining_names:
            return None  # 選ばれていない名前がない場合はNoneを返す
        picked_name = random.choice(remaining_names)  # ランダムに1つの名前を選ぶ
        self.picked_names.append(picked_name)  # 選ばれた名前をリストに追加
        self.save_picked_data()  # 選ばれた名前データをCSVファイルに保存
        return picked_name

    def reset_picked_names(self):
        self.picked_names = []  # 選ばれた名前のリストをリセット
        self.save_picked_data()  # 空のリストをCSVファイルに保存

    def delete_name(self, name):
        if name in self.names:
            self.names.remove(name)  # 名前をリストから削除
            if name in self.picked_names:
                self.picked_names.remove(name)  # 選ばれた名前リストからも削除
            self._save_csv(data_file, self.names)  # 名前データをCSVファイルに保存
            self.save_picked_data()  # 選ばれた名前データをCSVファイルに保存
            return True
        return False