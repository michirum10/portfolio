# =============
# ロジック
# =============

from sqlalchemy.orm  import scoped_session, Session
from DatabaseManager import Person

def add(scoped_ses:scoped_session):
    name = input("名前を入力してください。\n>")
    gender = numberRangeInput("性別を入力してください。\n[1]男[2]女[3]その他",1,3)
    age = numberRangeInput("年齢を入力してください。",0,150)
    p = Person(name=name,gender=gender,age=age)
    # 挿入予定のデータを出力
    dispRecord(p)
    if confirm("上記のデータで登録します。\nよろしいでしょうか？"):
        # セッション開始
        session = scoped_ses()
        # DB操作[データの挿入]
        session.add(p)
        # DB操作[コミット]
        session.commit()
        # DB操作セッションの終了
        session.close()
        print("登録が実行されました。")
    else:
        print("登録がキャンセルされました。")

# 全部表示するやつ
def getAll(scoped_ses:scoped_session):
    # セッション開始
    session = scoped_ses()
    # DB操作[全件取得処理]
    res = session.query(Person).all()
    for record in res:
        print("----------------")
        dispRecord(record)
    print("----------------")
    # DB操作セッションの終了
    session.close()

# 出力メソッドの定義
def dispRecord(record:Person):
    dicRecord = record.getData()
    print(f"id:{dicRecord["ID"]}")
    print(f"name:{dicRecord["name"]}")
    print(f"gender:{transGenderNumToStr(dicRecord["gender"])}")
    print(f"age:{dicRecord["age"]}")

# 性別選択の整数入力関数の定義
def numberInput(msg,empty=False):
    while True:
        cmd = input(msg + "\n>")
        if empty and cmd == "":
            return ""
        try:
            return int(cmd)
        except:
            print("ERROR:整数を入力してください。")

# 年齢の範囲指定、数値入力チェック関数の定義
def numberRangeInput(msg,min,max,empty=False):
    while True:
        cmd = numberInput(msg,empty)
        if cmd != "":
            num = int(cmd)
            if min <= num <= max:
                return num
            else:
                print(f"ERROR:{min}~{max}の範囲の整数を入力してください。")
        else:
            return ""        

# 承認チェック関数
def confirm(msg):
    while True:
        cmd = input(f"{msg}\n [y]YES[n]NO\n>")
        if cmd == "y":
            return True
        elif cmd == "n":
            return False
        else:
            print("ERROR:正しく入力してください。")

# 性別を番号から文字列に変換する関数
genderNumToStr = {1:"男",2:"女",3:"その他"}
def transGenderNumToStr(genderNum):
    try:
        genderStr = genderNumToStr[genderNum]
    except:
        genderStr = "ERROR:データが不正です。"
    return genderStr

# 更新機能
def update(scoped_ses: scoped_session):
    # 現在の全レコードを表示
    getAll(scoped_ses)
    
    # セッション開始
    session = scoped_ses()
    # id指定
    inputNo = input("更新したいIDを指定してください。\n>")
    # 指定したidデータを取得
    record = session.get(Person,inputNo)
    
    if record:
        # 変更前のデータを表示
        print("変更前のデータ:")
        dispRecord(record)
        
        name = input("名前を入力してください。\n>")
        if name != "":
            record.name = name
            
        gender = numberRangeInput("性別を入力してください。\n[1]男[2]女[3]その他",1,3,True)
        if gender != "":
            record.gender = gender
            
        age = numberRangeInput("年齢を入力してください。",0,150,True)
        if age != "":
            gender.age = age
        dispRecord(record)
        if confirm("上記のデータで更新します。\nよろしいですか？"):
            session.commit()
            print("更新が実行されました。")
        else:
            print("更新がキャンセルされました。")
            # 変更をキャンセルする場合は、ロールバックして元の状態に戻す
            # session.rollback()
    else:
        print(f"ID {id} のレコードが見つかりません。")
    # DB操作セッションの終了
    session.close()

# 削除機能(物理削除)
def delete(scoped_ses: scoped_session):
    
    # 現在の全レコードを表示
    getAll(scoped_ses)
    
    # セッション開始
    session = scoped_ses()
    inputNo = input("削除したいIDを入力してください\n>")
    person = session.get(Person,inputNo)
    
    if person:
        if confirm(f"本当にID {inputNo} を削除してもよろしいですか？"):
            session.delete(person)
            session.commit()
            print(f"ID {inputNo} が削除されました。")
        else:
            print("削除がキャンセルされました。")
    else:
        print(f"ID {inputNo}が見つかりません。")
    
    # 閉じる
    session.close()