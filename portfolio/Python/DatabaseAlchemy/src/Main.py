# Main.py
# =============
# 自作ライブラリの利用とCUIアプリケーション
# =============
import Logic
from DatabaseManager import db,ses

print("DBシステムを開始しました。")

# 課題：
# 更新機能と削除機能を追加してください。
# 更新機能の仕様：
# IDを入力して、そのレコードを更新
# 変更したいカラムに文字を入力
# 空白にした場合は変更なし
# 削除機能は物理削除で実装してください。

# 無限ループ
while True:
    cmd = input("[1]追加[2]確認[3]更新[4]削除[q]終了\n>")
    if cmd == "1":# データの追加3
        print("データを追加します。")
        Logic.add(ses)
    elif cmd == "2":# データの確認
        print("データを確認します。")
        Logic.getAll(ses)
    elif cmd == "3":# データの更新
        print("データを更新します。")
        Logic.update(ses)
    elif cmd == "4":# データの削除
        print("データを削除します。")
        Logic.delete(ses)
    elif cmd == "q" or cmd == "Q":# システムの終了
        
        break

# DBの終了処理
db.dispose()
print("システムが終了しました。")
