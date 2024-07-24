# SQLとclass__init__使って書く

import tkinter as tk  # GUIを作成するためのTkinterモジュールをインポート
from tkinter import ttk, messagebox  # Tkinterの拡張ウィジェットとメッセージボックスをインポート
import random  # ランダムな選択のためのrandomモジュールをインポート
import sqlite3  # SQLiteデータベース操作のためのsqlite3モジュールをインポート
import os  # ファイル操作のためのosモジュールをインポート

class RandomNameSelector:
    # def __init__(self, master):こう書くやつ
    def __init__(self, master):
        self.master = master  # メインウィンドウを保存
        self.master.title("ランダム名前選択アプリ")  # ウィンドウのタイトルを設定
        self.master.geometry("500x400")  # ウィンドウのサイズを設定

        self.db_file = "names_database.db"  # データベースファイル名を設定
        self.create_database()  # データベースを作成または接続

        self.create_widgets()  # GUIウィジェットを作成
        self.load_data()  # データベースからデータを読み込む

    # テーブルを作る
    def create_database(self):
        conn = sqlite3.connect(self.db_file)  # データベースに接続
        cursor = conn.cursor()  # カーソルオブジェクトを作成
        # namesテーブルを作成（存在しない場合）
        cursor.execute('''CREATE TABLE IF NOT EXISTS names
                          (id INTEGER PRIMARY KEY, name TEXT UNIQUE)''')
        # picked_namesテーブルを作成（存在しない場合）
        cursor.execute('''CREATE TABLE IF NOT EXISTS picked_names
                          (id INTEGER PRIMARY KEY, name TEXT UNIQUE)''')
        conn.commit()  # 変更をコミット
        conn.close()  # データベース接続を閉じる

# ウィジェットも関数に
    def create_widgets(self):
        style = ttk.Style()  # スタイルオブジェクトを作成
        style.configure("TButton", padding=6, relief="flat", background="#ccc")  # ボタンのスタイルを設定

        main_frame = ttk.Frame(self.master, padding="10")  # メインフレームを作成
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))  # メインフレームを配置

        # 以下、各ウィジェットを作成し配置
        ttk.Label(main_frame, text="名前を登録してください:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry = ttk.Entry(main_frame, width=30)
        self.entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        self.entry.bind("<Return>", self.register_name)  # Enterキーで登録できるように！

        ttk.Button(main_frame, text="登録", command=self.register_name).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(main_frame, text="ランダム選択", command=self.choose_random_name).grid(row=1, column=0, pady=5)
        ttk.Button(main_frame, text="リセット", command=self.reset_picked_names).grid(row=1, column=1, pady=5)
        ttk.Button(main_frame, text="名前リスト表示", command=self.show_name_list).grid(row=1, column=2, pady=5)

        self.status_label = ttk.Label(main_frame, text="", wraplength=300)
        self.status_label.grid(row=2, column=0, columnspan=3, pady=10)

        self.name_listbox = tk.Listbox(main_frame, height=10, width=40)
        self.name_listbox.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E))

        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.name_listbox.yview)
        scrollbar.grid(row=3, column=3, sticky=(tk.N, tk.S))
        self.name_listbox.configure(yscrollcommand=scrollbar.set)

        ttk.Button(main_frame, text="削除", command=self.delete_name).grid(row=4, column=0, columnspan=3, pady=5)

    # csvデータを読み込む関数
    def load_data(self):
        try:
            conn = sqlite3.connect(self.db_file)  # データベースに接続
            cursor = conn.cursor()  # カーソルオブジェクトを作成
            cursor.execute("SELECT name FROM names")  # namesテーブルから名前を取得
            self.names = [row[0] for row in cursor.fetchall()]  # 取得した名前をリストに格納
            cursor.execute("SELECT name FROM picked_names")  # picked_namesテーブルから名前を取得
            self.picked_names = [row[0] for row in cursor.fetchall()]  # 取得した名前をリストに格納
            conn.close()  # データベース接続を閉じる
            self.update_name_list()  # 名前リストを更新
        except sqlite3.Error as e:
            messagebox.showerror("データベースエラー", f"データの読み込み中にエラーが発生しました: {e}")
    # 登録されている名前リストの更新
    def update_name_list(self):
        self.name_listbox.delete(0, tk.END)  # リストボックスをクリア
        for name in self.names:
            self.name_listbox.insert(tk.END, name)  # 名前をリストボックスに追加
    
    # 登録ボタンが押されたときの処理
    def register_name(self, event=None):
        name = self.entry.get().strip()  # 入力された名前を取得し、前後の空白を削除
        if name and name not in self.names:  # 名前が空でなく、かつ既存のリストにない場合
            try:
                conn = sqlite3.connect(self.db_file)  # データベースに接続
                cursor = conn.cursor()  # カーソルオブジェクト？を作成
                cursor.execute("INSERT INTO names (name) VALUES (?)", (name,))  # 名前をデータベースに挿入
                conn.commit()  # 変更をコミット
                conn.close()  # データベース接続を閉じる
                self.names.append(name)  # 名前をリストに追加
                self.update_name_list()  # 名前リストを更新
                self.entry.delete(0, tk.END)  # 入力フィールドをクリア
                self.status_label.config(text=f"{name} を登録しました")  # ステータスを更新
            except sqlite3.Error as e:
                messagebox.showerror("データベースエラー", f"名前の登録中にエラーが発生しました: {e}")
        else:
            self.status_label.config(text="名前が入力されていないか、既に登録されています")

# ランダム選択ボタンが押されたときの処理
    def choose_random_name(self):
        remaining_names = [name for name in self.names if name not in self.picked_names]  # まだ選ばれていない名前のリストを作成
        if not remaining_names:  # 選ばれていない名前がない場合
            if not self.names:
                self.status_label.config(text="まだ誰も登録されていません")
            else:
                self.status_label.config(text="全員選ばれました。リセットしてください。")
            return
        picked_name = random.choice(remaining_names)  # ランダムに名前を選択
        try:
            conn = sqlite3.connect(self.db_file)  # データベースに接続
            cursor = conn.cursor()  # カーソルオブジェクトを作成
            cursor.execute("INSERT INTO picked_names (name) VALUES (?)", (picked_name,))  # 選ばれた名前をデータベースに挿入
            conn.commit()  # 変更をコミット
            conn.close()  # データベース接続を閉じる
            self.picked_names.append(picked_name)  # 選ばれた名前をリストに追加
            self.status_label.config(text=f"選ばれた人: {picked_name}")  # ステータスを更新
        except sqlite3.Error as e:
            messagebox.showerror("データベースエラー", f"名前の選択中にエラーが発生しました: {e}")

    # リセットボタンが押されたときの処理
    def reset_picked_names(self):
        try:
            conn = sqlite3.connect(self.db_file)  # データベースに接続
            cursor = conn.cursor()  # カーソルオブジェクトを作成
            cursor.execute("DELETE FROM picked_names")  # picked_namesテーブルのすべてのデータを削除
            conn.commit()  # 変更をコミット
            conn.close()  # データベース接続を閉じる
            self.picked_names = []  # picked_namesリストをクリア
            self.status_label.config(text="選択履歴をリセットしました")  # ステータスを更新
        except sqlite3.Error as e:
            messagebox.showerror("データベースエラー", f"リセット中にエラーが発生しました: {e}")

    # 登録した名前リストを表示する関数
    def show_name_list(self):
        if self.names:  # 名前リストが空でない場合
            names_str = "\n".join(self.names)  # 名前リストを文字列に変換
            messagebox.showinfo("登録された名前", names_str)  # メッセージボックスで名前リストを表示
        else:
            messagebox.showinfo("登録された名前", "まだ名前が登録されていません")

    # 選択した名前を消す
    def delete_name(self):
        selected = self.name_listbox.curselection()  # リストボックスで選択されたアイテムのインデックスを取得
        if selected:  # 選択されたアイテムがある場合
            name = self.name_listbox.get(selected[0])  # 選択された名前を取得
            if messagebox.askyesno("確認", f"{name} を削除しますか？"):  # 削除の確認
                try:
                    conn = sqlite3.connect(self.db_file)  # データベースに接続
                    cursor = conn.cursor()  # カーソルオブジェクトを作成
                    cursor.execute("DELETE FROM names WHERE name = ?", (name,))  # namesテーブルから名前を削除
                    cursor.execute("DELETE FROM picked_names WHERE name = ?", (name,))  # picked_namesテーブルから名前を削除
                    conn.commit()  # 変更をコミット
                    conn.close()  # データベース接続を閉じる
                    self.names.remove(name)  # namesリストから名前を削除
                    if name in self.picked_names:
                        self.picked_names.remove(name)  # picked_namesリストから名前を削除（存在する場合）
                    self.update_name_list()  # 名前リストを更新
                    self.status_label.config(text=f"{name} を削除しました")  # ステータスを更新
                except sqlite3.Error as e:
                    messagebox.showerror("データベースエラー", f"名前の削除中にエラーが発生しました: {e}")
        else:
            messagebox.showwarning("警告", "削除する名前を選択してください")

# 前に習ったmainloop()のやつで実行
if __name__ == "__main__":
    root = tk.Tk()  # メインウィンドウを作成
    app = RandomNameSelector(root)  # アプリケーションのインスタンスを作成
    root.mainloop()  # イベントループを開始