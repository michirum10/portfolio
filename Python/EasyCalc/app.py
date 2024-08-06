# 簡易電卓

# 1. 値は２入力して加算処理を行ってください。
# 2. ポート番号8081
# 3. ルートで値２つを入力し
# 4. /resultで答えを出力してください。


from flask import Flask, render_template, request, redirect, url_for

# インスタンス生成
app = Flask(__name__)

@app.route("/" ,methods=["GET"])
# GET : データの取得やページの表示
# POST: データの送信や処理
def index():
    err = request.args.get("errid")
    # レンダーテンプレート
    return render_template( "index.html",title="簡易電卓",e1='', e2='', errid=err)
# e1='', e2=''の初期値指定しておくと良いらしい


# 計算する関数
def calc(e1, e2, op):
    try:
    # 計算分岐
        if op == 'add':
            return e1 + e2
        elif op == 'sub':
            return e1 - e2
        elif op == 'mul':
            return e1 * e2
        elif op == 'div':
            if e2 == 0:
                return "ゼロでは割れません！"
            return e1 / e2
        else:
            return "無効な操作です"
    except Exception as e:
        return str(e)



# 結果を表示する関数
@app.route("/result", methods=["GET"])
# methods=["GET"]は省略できる
def result():
    e1 = request.args.get("e1")
    e2 = request.args.get("e2")
    op = request.args.get("op")
    try:
        e1 = int(e1)
        e2 = int(e2)
    except ValueError:
        return redirect(url_for("index", errid="E001"))  # indexに表示させる

    # 計算結果
    result = calc(e1, e2, op)
    
    if result == "ゼロでは割れません！":
        return redirect(url_for("index", errid="E002"))
    elif result == "無効な操作です":
        return redirect(url_for("index", errid="E003"))
    
    # 結果ページのレンダリング
    return render_template("result.html", title="計算結果", e1=e1, e2=e2, result=result, op=op)

if __name__ == "__main__":
    # デバッグモード
    app.debug = True
    # ホストとポートの指定
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=8081)
