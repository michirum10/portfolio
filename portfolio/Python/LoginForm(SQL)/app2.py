# app2.py

from flask import Blueprint, redirect, render_template, request, session
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
import bcrypt

# Blueprintの名称：APP2
# モジュール名：app2
# URL：/APP2
app2 = Blueprint("APP2", __name__, url_prefix="/APP2")

# データベースの設定
db = SQLAlchemy()

# ユーザーのIDとパスワードを管理
class User(db.Model):
    
    # ユーザーのID。最大80文字の文字列型。主キー
    id = db.Column(db.String(80), primary_key=True)
    # ユーザーのパスワード。最大120文字の文字列型。NULL値を許可しない
    password = db.Column(db.String(120), nullable=False)

    # パスワードをハッシュ化して文字列として保存
    def set_password(self, password):
        # パスワードをUTF-8でエンコード、ハッシュ化し、再度デコードして保存
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # 入力されたパスワードが正しいかチェックするメソッド
    def check_password(self, password):
        # 入力パスワードをハッシュ化し、保存されているハッシュと比較
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

# loginとsuccessの設定
class LoginSystem(MethodView):
    # getでのアクセス時
    def get(self):
        return render_template("pages/login.html")
    
    # postでのアクセス時
    def post(self):
        id = request.form.get("id")
        pw = request.form.get("pw")
        
        # 入力が空の場合のエラーチェック
        if not id or not pw:
            msg = 'エラー：IDとパスワードを入力してください。'
            return render_template('pages/login.html', msg=msg)
        
        # データベースからユーザーを検索
        user = User.query.get(id)
        
        #idとpasswordが一致するかどうかの確認
        if user:
            if user.check_password(pw): #一致した場合
                session['flag'] = True #ログイン可能な状態にする
                session['id'] = id
                msg = 'ログインに成功しました！'
                # successページに遷移
                return render_template("pages/success.html",id=id,pw="••••••••",msg=msg)
            else: #一致しなかった場合
                session['flag'] = False
                msg = 'エラー：パスワードが間違っています！'
        else:  # 新規登録
            new_user = User(id=id)
            # set_passwordでパスワードをハッシュ化
            new_user.set_password(pw)
            # データベースセッションに新しいユーザーを追加
            db.session.add(new_user)
            # 変更をデータベースにコミット
            db.session.commit()
            session['flag'] = True
            session['id'] = id
            msg = '新規ユーザーとして登録しました！'
            return render_template("pages/success.html", id=id, pw="••••••••", msg=msg)
        
        return render_template('pages/login.html', msg=msg)

# LoginSystemをBlueprintに登録
app2.add_url_rule("/",view_func=LoginSystem.as_view("login"))

# Blueprintのインデックスページ
@app2.route("/")
def index():
    return render_template("pages/index.html", msg="APP2のホーム")

# データベース初期化関数
def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()