# app.py

from flask import Flask,render_template
from LoginSystem import login_bp, init_db
from config import DevelopmentConfig

# インスタンス生成(appを初期化)
app = Flask(__name__)

# configの設定をロード(SQL,secret_key)
app.config.from_object(DevelopmentConfig)

# Blueprintの登録
app.register_blueprint(login_bp, url_prefix='/LoginSystem')

# データベース初期化したやつを呼び出し
init_db(app)

# indexの表示
@app.route("/") 
def index():
    return render_template("pages/index.html", msg="WELCOME！")

if __name__ == "__main__":
    # デバッグモード
    app.debug = True
    # ホストとポートの指定
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=8080)