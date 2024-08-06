import tkinter as tk  # GUI作成のためのモジュールをインポート
from Logic import NameManager  # 名前管理クラスをインポート

class NamePickerGUI:
    def __init__(self, master):
        self.master = master  # メインウィンドウの参照を保持
        self.name_manager = NameManager()  # 名前管理クラスのインスタンスを作成
        self.setup_ui()  # GUIのセットアップ

    def setup_ui(self):
        self.master.title("ランダム名前選択アプリ")  # ウィンドウのタイトルを設定
        self.master.geometry("400x400")  # ウィンドウのサイズを設定

        # フレームの作成
        self.input_frame = tk.Frame(self.master)
        self.button_frame = tk.Frame(self.master)
        self.status_frame = tk.Frame(self.master)
        self.list_frame = tk.Frame(self.master)

        # フレームの配置
        self.input_frame.pack(pady=10)
        self.button_frame.pack(pady=10)
        self.status_frame.pack(pady=10)
        self.list_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # ラベルとエントリの作成
        tk.Label(self.input_frame, text="名前を登録してください:").pack()
        self.entry = tk.Entry(self.input_frame)
        self.entry.pack()
        self.entry.bind("<Return>", self.register_name)  # Enterキーで名前を登録

        # ボタンの作成と配置
        tk.Button(self.button_frame, text="ランダム選択", command=self.choose_random_name).pack(side=tk.LEFT, padx=10)
        tk.Button(self.button_frame, text="登録", command=self.register_name).pack(side=tk.LEFT, padx=10)
        tk.Button(self.button_frame, text="リセット", command=self.reset_picked_names).pack(side=tk.LEFT, padx=10)

        # ステータスラベルの作成と配置
        self.status_label = tk.Label(self.status_frame, text="")
        self.status_label.pack()

        # 名前リストボックスとスクロールバーの作成と配置
        tk.Label(self.list_frame, text="登録済みの名前:").pack()
        self.name_listbox = tk.Listbox(self.list_frame, height=10, width=30)
        self.name_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(self.list_frame, orient=tk.VERTICAL, command=self.name_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.name_listbox.config(yscrollcommand=scrollbar.set)

        # 削除ボタンの作成と配置
        tk.Button(self.list_frame, text="削除", command=self.delete_selected_name).pack(side=tk.BOTTOM, pady=10)

        self.update_name_list()  # 名前リストを更新

    def choose_random_name(self):
        result = self.name_manager.pick_random_name()  # ランダムに名前を選ぶ
        if result:
            self.status_label.config(text=result)  # 選ばれた名前をラベルに表示
        else:
            self.status_label.config(text="選ぶ名前がありません")

    def register_name(self, event=None):
        name = self.entry.get()  # エントリから名前を取得
        if self.name_manager.register_name(name):
            self.entry.delete(0, tk.END)  # エントリをクリア
            self.status_label.config(text=f"{name} を登録しました")
            self.update_name_list()  # 名前リストを更新
        else:
            self.status_label.config(text="名前が入力されていないか、既に登録されています")

    def reset_picked_names(self):
        self.name_manager.reset_picked_names()  # 選ばれた名前リストをリセット
        self.status_label.config(text="選択履歴をリセットしました")

    def delete_selected_name(self):
        selected = self.name_listbox.curselection()  # リストボックスで選択された項目を取得
        if selected:
            name = self.name_listbox.get(selected[0])  # 選択された名前を取得
            if self.name_manager.delete_name(name):
                self.update_name_list()  # 名前リストを更新
                self.status_label.config(text=f"{name} を削除しました")
        else:
            self.status_label.config(text="削除する名前を選択してください")

    def update_name_list(self):
        self.name_listbox.delete(0, tk.END)  # リストボックスをクリア
        for name in self.name_manager.names:
            self.name_listbox.insert(tk.END, name)  # 名前リストをリストボックスに追加

if __name__ == "__main__":
    root = tk.Tk()  # メインウィンドウを作成
    app = NamePickerGUI(root)  # アプリケーションのインスタンスを作成
    root.mainloop()  # メインループを開始