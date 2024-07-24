# Pythonの課題です。
# 登録した人をランダムで当てるアプリケーションを作成してください。
# こちらはtkinterまたはコンソールアプリケーションで、作成してください。
# tkinterで作成する場合はの結果出力先はアプリケーション上（ラベル）でも、ターミナルでも良いです。
# コンソールアプリケーションの作成例は追って送ります。
# 課題の段階ですが、
# 1段回目、任意の人を登録できるようにしてください。
# 2段階目、登録した人からランダムに1人を出力してください。
# 3段階目、偏らない様に、全員が平等に出力されるようにしてください。
# 4段階目、アプリケーションを終了しても、データを維持できるようにしてください。（データの読み込みと保存）

# インポート
import tkinter as tk
import random
import csv

# csvファイルを変数に代入
data_file = "names_data.csv"  # 名前を保存するCSVファイル
picked_file = "picked_names_data.csv"  # 選ばれた名前データを保存するCSVファイル

# 名前を格納するリスト(2つ用意)
names = []  # 登録された名前を格納するリスト
picked_names = []  # ランダムに選ばれた名前を格納するリスト

# 選択された名前(picked_names)リストをCSVファイルに保存する関数
def save_picked_data():
    # picked_namesリストのデータをCSVファイルに保存
    # open()関数でpicked_fileファイルを書き込みモード(mode='w')で開く
    with open(picked_file, mode='w', newline='', encoding='utf-8-sig') as f:  #encoding='utf-8-sig':文字化けなおす
        writer = csv.writer(f)  # csv.writer()関数でデータを書き込むためのwriterオブジェクトを作る
        # ループ
        for name in picked_names:
            writer.writerow([name])  # 一行ずつ書き込む
    print(f"データを {picked_file} に保存しました。")

# csvデータを読み込む関数(data_file,picked_file両方読み込む)
def load_data():
    global names, picked_names  # グローバル変数として宣言、変更が関数外にも反映
    names = []  # 初期化
    picked_names = []  # 初期化
    
    try:
        # namesリストのデータをCSVファイルから読み込む
        with open(data_file, mode='r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)  # 読み込み
            # ループ
            for row in reader:
                names.append(row[0])  # 最初の要素を行に追加(rowは行)
        print(f"データを {data_file} から読み込みました。")
    except FileNotFoundError:
        # ファイルが見つからない場合、新しいファイルを作成する
        with open(data_file, mode='w', newline='', encoding='utf-8-sig') as f:
            pass
        print(f"{data_file} が見つかりませんでした。新しいファイルを作成します。")
    try:
        # picked_namesリストのデータをCSVファイルから読み込む
        with open(picked_file, mode='r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)  # 読み込み
            # ループ
            for row in reader:
                picked_names.append(row[0])  # 最初の要素を行に追加
        print(f"データを {picked_file} から読み込みました。")
    except FileNotFoundError:
        # ファイルが見つからない場合、新しいファイルを作成する
        with open(picked_file, mode='w', newline='', encoding='utf-8-sig') as f:
            pass
        print(f"{picked_file} が見つかりませんでした。新しいファイルを作成します。")

# ランダムに1人選ぶ関数
# ウィンドウを閉じて再度実行しても一度選ばれた名前は選ばれないように
def pick_random_name():
    # 選ばれていない名前のリストを作成
    # names[]リストに含まれる名前のうち、picked_names[]リストに含まれていない名前のリストを作成？？？
    remaining_names = [name for name in names if name not in picked_names]
    # ないとき
    if not remaining_names:
        return "まだ誰も登録されていないか、全員選ばれました"
    picked_name = random.choice(remaining_names)  # ランダムに1人選ぶ
    picked_names.append(picked_name)  # 選ばれた名前をpicked_namesリストに追加
    save_picked_data()  # データを保存
    return picked_name  # 選ばれた名前を出力

# ランダム選択ボタンが押されたときの処理
def choose_random_name():
    result = pick_random_name()  # ランダムに1人選ぶ
    status_label.config(text=result)  # ステータスラベルを更新

# 登録ボタンが押されたときの処理
def register_name(event=None):# event=Noneを追加してEnterキーでも呼び出せるように(.bind("<Return>")をエントリボタンに書き込む)
    name = entry.get()  # get(入力フォーム)の中身を取得
    if name and name not in names:  # 名前が入力されていて、かつ重複していない場合？？
        names.append(name)  # 名前をnamesリストに追加
        # データを保存する（namesリストに書き込み）
        with open(data_file, mode='w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)  # 書き込み
            # ループ
            for n in names:
                writer.writerow([n])  # 一行ずつ書き込む
        entry.delete(0, tk.END)  # 入力フォームのクリア
        status_label.config(text=f"{name} を登録しました")  # ステータスラベルを更新
    else:  # 重複で分岐
        status_label.config(text="名前が入力されていないか、既に登録されています")  # エラーメッセージ
    update_name_list()

# リセットボタンが押されたときの処理
def reset_picked_names():
    global picked_names  # グローバル変数
    picked_names = []  # 初期化
    save_picked_data()  # データを保存
    status_label.config(text="選択履歴をリセットしました")

# 登録された名前一覧を更新
def update_name_list():
    name_listbox.delete(0, tk.END)  # リストボックスの内容を全て削除
    # namesリストの全ての名前をリストボックスに挿入
    for name in names:
        name_listbox.insert(tk.END, name)

# 一個ずつ選んで消せるように
def delete_selected_name():
    selected = name_listbox.curselection()  # リストボックスで選択された項目を取得
    # 選択された項目がある場合
    if selected:
        name = name_listbox.get(selected[0])  # 選択された名前を取得
        names.remove(name)  # namesリストから名前を削除
        if name in picked_names: # さらにその名前がpicked_namesリストにある場合は削除
            picked_names.remove(name)
        # namesリストをCSVファイルに保存
        with open(data_file, mode='w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            for n in names:
                writer.writerow([n])
        save_picked_data()  # picked_namesリストを保存
        update_name_list()  # リストボックスを更新
        status_label.config(text=f"{name} を削除しました") # ステータスラベルを更新
    else:
        # 選択された項目がない場合、エラーメッセージを表示
        status_label.config(text="削除する名前を選択してください")
    update_name_list()  # リストボックスを更新

# Tkinterの設定

# tkitterのウィジェットの作成
root = tk.Tk()  # メインウィンドウの作成
root.title("ランダム名前選択アプリ")  # ウィンドウのタイトルを設定
root.geometry("400x400")  # ウィンドウのサイズを設定

# フレームの作成
input_frame = tk.Frame()  # 入力用フレーム
button_frame = tk.Frame()  # ボタン用フレーム
status_frame = tk.Frame()  # 結果表示用のフレーム
list_frame = tk.Frame()  # 名前リスト用のフレーム

# ラベルとフォームの作成
# 「名前を登録してください:」と表示するラベル
label = tk.Label(input_frame,text="名前を登録してください:")
entry = tk.Entry(input_frame)  # 名前入力フォーム
status_label = tk.Label(status_frame, text="")  # ランダム表示用ラベル
list_label = tk.Label(list_frame, text="登録済みの名前:")  # 名前リストボックスのラベル
name_listbox = tk.Listbox(list_frame, height=10, width=30)  # 名前リストボックス
scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL, command=name_listbox.yview)# スクロールバー
name_listbox.config(yscrollcommand=scrollbar.set)  # ボックスとスクロールバーを関連付ける

# ボタンの作成
choose_button = tk.Button(button_frame, text="ランダム選択", command=choose_random_name)  # ランダム選択ボタン
register_button = tk.Button(button_frame, text="登録", command=register_name)  # 登録ボタン
reset_button = tk.Button(button_frame, text="リセット", command=reset_picked_names)  # リセットボタン
delete_button = tk.Button(list_frame, text="削除", command=delete_selected_name)  # 削除ボタン

# 配置

# フレームの配置
input_frame.pack(pady=10)  # 入力フレームを配置、縦の余白を追加
button_frame.pack(pady=10)  # ボタンフレームを配置
status_frame.pack(pady=10)# 結果表示用のフレーム
list_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)  # リストフレームを配置
# ウィジェットの配置
label.pack()
entry.pack()  # 名前入力フォーム
entry.bind("<Return>", register_name)  # Enterキーで登録できるように
# ボタンの配置
choose_button.pack(side=tk.LEFT,padx=10)  # ランダムボタン(左寄せで配置、横の余白を追加)
register_button.pack(side=tk.LEFT,padx=10)  # 登録ボタン
reset_button.pack(side=tk.LEFT,padx=10)  # リセットボタン
delete_button.pack(side=tk.BOTTOM,pady=10 )  # 削除ボタンをリストの下に配置(上下の余白を追加)
# ランダム結果表示
status_label.pack()
# 名前一覧表示
list_label.pack()
name_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# データを読み込む
load_data()

# 表示開始
root.mainloop()

# コンソールアプリ(３段階目まで)
# # テストコード
# if __name__ == "__main__":
    # print("プログラムを開始します")
    # endFlag = False
    # # 名前を格納するリスト1
    # names = []
    # picked_names = []
    # while not endFlag:
    #     print("選択してください。")
    #     print("[1] 名前を登録する [2] ランダムに選ぶ [0] 終了\n>")
    #     cmd = input()
    #     # 名前の登録
    #     if cmd == "1":
    #         name = input("名前を入力してください: ")
    #         names.append(name)
    #         print(f"{name} を登録しました")
    #     # ランダムに選ぶ
    #     elif cmd == "2":
    #         # namelistが空かどうかを確認
    #         if not names:
    #             print("まだ誰も登録されていません")
    #         else:
    #             random_name = random.choice(names)
    #             names.remove(random_name)  # 選ばれた名前をリストから削除
    #             print(f"ランダムに選ばれた人: {random_name}")
    #     # 終了
    #     elif cmd == "0":
    #         print("終了が選択されました。")
    #         endFlag = True
    #     else:
    #         print("正しいコマンドを入力してください。")
# print("プログラムを終了します。")

# サンプルコード
# print("プログラムを開始します")
# endFlag = False
# while not endFlag:
#     print("選択してください。")
#     print("[1]挨拶[2]自己紹介[0]終了")
#     cmd = input()
#     if cmd == "1":
#         print("こんにちは")
#     elif cmd == "2":
#         print("どうも、コンソールアプリです。")
#     elif cmd == "0":
#         print("終了が選択されました。")
#         endFlag = True
#     else:
#         print("正しいコマンドを入力してください。")
# print("プログラムを終了します。")