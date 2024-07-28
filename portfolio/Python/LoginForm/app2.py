# app2.py

from flask import Blueprint, redirect, render_template, request, session
from flask.views import MethodView
import bcrypt

# Blueprintの名称：APP2
# モジュール名：app2
# URL：/APP2
app2 = Blueprint("APP2", __name__, url_prefix="/APP2")
# # セッションを使うための鍵
# app2.secret_key = b"hit"


# # flask-loginからLoginManagerをimport
# from flask_login import LoginManager
# LoginManagerの起動
# login = LoginManager(app) #extensionを起動させる際の標準的な記述

# 辞書型で取得
name_list = {}

# loginとsuccessの設定
class LoginSystem(MethodView):
    # getでのアクセス時
    def get(self):
        global name_list
        return render_template("pages/login.html")
    
    # postでのアクセス時
    def post(self):
        id = request.form.get("id")
        pw = request.form.get("pw").encode('utf-8')  # パスワードをバイト列にエンコード
        
        
        global name_list
        
        #idが既にあるかどうかを確認する
        if id in name_list:
            # パスワードのハッシュを取得
            hashed_pw = name_list[id]
            # IDとパスワードが一致しているかを確認する
            if bcrypt.checkpw(pw, hashed_pw):
                #ログイン可能な状態にする
                session['flag'] = True
            #IDとpasspwrdが一致しない場合は
            else:
                session['flag'] = False
        #idの新規登録の場合
        else:
            hashed_pw = bcrypt.hashpw(pw, bcrypt.gensalt())
            name_list[id] = hashed_pw
            session['flag'] = True #ログイン可能な状態にする
            
        session['id'] = id
        user_id = session.get("id")
        #idとpasseprdが一致するかどうかの確認
        if session['flag']: #一致した場合
            msg = 'ログインに成功しました！'
            return render_template("pages/success.html",id=id,pw=pw,msg=msg)
        else: #一致しなかった場合
            msg = 'エラー：パスワードが間違っています！'
            return render_template('pages/login.html',msg=msg)
        

# LoginSystemをBlueprintに登録
app2.add_url_rule("/",view_func=LoginSystem.as_view("login"))
# ("login")はただ名前付けただけらしい

# Blueprintのインデックスページ
@app2.route("/")
def index():
    return render_template("pages/index.html", msg="APP2のホーム")