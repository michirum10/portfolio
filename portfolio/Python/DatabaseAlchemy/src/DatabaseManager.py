# DatabaseManager.py

# =============
# SQLAlchemy(ORMの利用)
# =============

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session


# モデルを作成
# プログラムでいうとClassの事
# DBでいうとテーブルの事

# モデルのベースクラスを取得
Base = declarative_base()

# モデルの定義
class Person(Base):

    # テーブル名
    __tablename__ = "person"

    # カラムの定義
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    gender = Column(Integer)
    age = Column(Integer)

    # データを辞書型で取得する
    def getData(self):
        if self.id is not None:
            return {
                "id":int(self.id),
                "name":str(self.name),
                "gender":int(self.gender),
                "age":int(self.age),
            } 
        else:
            return {
                "id":"新規",
                "name":str(self.name),
                "gender":int(self.gender),
                "age":int(self.age),
            } 

# ORMエンジンの使用準備と接続
db = create_engine("sqlite:///../db/Person.db")

# テーブルを自動生成する準備
Base.metadata.create_all(bind=db,checkfirst=True)

# セッション
ses = scoped_session(sessionmaker(bind=db))

# テストコード
if __name__ == "__main__":
    # ORMエンジンの使用準備と接続
    db = create_engine("sqlite:///../db/TestPerson.db")

    # テーブルを自動生成する準備
    Base.metadata.create_all(bind=db,checkfirst=True)

    # セッション
    Session = sessionmaker(bind=db)
    ses = Session()

    # データベース操作
    # データの挿入
    p1 = Person(name="木内",gender=1,age=32)
    ses.add(p1)
    ses.commit()

    # 出力メソッドの定義
    def dispRecord(record:Person):
        dicRecord = record.getData()
        print(f"id:{dicRecord["id"]}")
        print(f"name:{dicRecord["name"]}")
        print(f"gender:{dicRecord["gender"]}")
        print(f"age:{dicRecord["age"]}")

    # 全データ取得
    print("全データ取得")
    res1 =  ses.query(Person).all()
    for record in res1:
        dispRecord(record)

    print("１件データ取得(id=2)")
    # １件データ取得
    # ID(プライマリキー)が2番のレコードを取得
    p2 = ses.get(Person,2)
    dispRecord(p2)

    # 1件データ取得(検索)
    print("１件データ取得(id=3)")
    p3 = ses.query(Person).filter(Person.id == 3).first()
    dispRecord(p3)

    # データ検索
    print("データ取得(age=37)")
    p4 = ses.query(Person).filter(Person.age == 37)
    for record in p4:
        dispRecord(record)

    # データ検索(あいまい検索)
    print("データ検索(name=『木』が付くもの)")
    p5 = ses.query(Person).filter(Person.name.like("%木%"))
    for record in p5:
        dispRecord(record)
    
    # データの更新
    print("データの更新")
    print("idを指定して内容を書き換える")

    inputNo = input("IDを指定してください。")
    # １件データ取得
    p6 = ses.get(Person,inputNo)
    print("データの更新前")
    dispRecord(p6)
    # データを書き換える(更新の重要ポイント)
    p6.name = "木之内"
    # コミット(更新)
    ses.commit()
    print("データの更新後")
    dispRecord(p6)

    # データの削除
    ses.query(Person).filter(Person.name == "木之内").delete()
    ses.commit()