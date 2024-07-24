# 課題７：ネットショップもどき

## ファイル構成
- html(フォルダ)
  - index.html
  - detail.html
  - confirm.html
  - complete.html
- css(フォルダ)
  - index.css
  - detail.css
  - confirm.css
  - complete.css
- js(フォルダ)
  - Cart.js
  - index.js
  - detail.js
  - confirm.js
  - complete.js
- img(フォルダ)
  - 好きなもの
- data(フォルダ)
  - data.json

## クラス
カート(買い物カゴ)クラスを作成
プロパティ:商品リスト(配列)
メソッド:商品追加
メソッド:商品一覧取得
メソッド:商品購入

## 画面には
画面間のデータの受け渡しは、sessionStorageを利用するとします。
※localStorageでも良いです。

### 商品一覧画面 index.html
商品名と値段、画像を表示(ローカルのdata.jsonからデータを取得する)
それらをクリックすると商品詳細画面へ遷移(新しくウィンドウを開く)
購入ボタン⇛購入確認画面へ遷移

### 商品詳細画面 detail.html
一つのクリックした商品の情報を表示する
（商品名と値段、画像、説明を大きく表示する。）
カートに入れるボタン⇛カートにデータを追加

### 購入確認画面 confirm.html
カートの中をリストで表示
購入のボタン⇛カートの中身を削除し購入完了画面へ遷移

### 購入完了画面 complete.html
商品一覧へ画面遷移
