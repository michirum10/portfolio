# app.py

from flask import Flask,render_template

from config import DevelopmentConfig

# インスタンス生成(appを初期化)
app = Flask(__name__)
print("Before importing config")
app.config.from_object(DevelopmentConfig)
print("After importing config")

# Blueprintの登録
from app2 import app2
app.register_blueprint(app2)

# indexの表示
@app.route("/")
def index():
    return render_template("pages/index.html", msg="WELCOME！")

if __name__ == "__main__":
    # デバッグモード
    app.debug = True
    # ホストとポートの指定
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=5002)
