import ItemListManagement from "../js/ItemListManagement.js"
import Cart from "../js/Cart.js"

// カート(モジュールスコープ)
let cart

// セッションストレージからcartItems(文字列)を取得する。
if(window.sessionStorage.getItem('cartItems')){
  // cartItemsの中が存在する時
  // カートのインスタンス化(cartItems(文字列)を取得し、これをオブジェクトに変換してCartクラスのコンストラクタの引数に渡している。)
  cart = new Cart(JSON.parse(window.sessionStorage.getItem('cartItems')))
}else{
  // cartItemsの中が存在しない時
  // カートのインスタンス化
  cart = new Cart()
}

// JSONデータの取得処理
window.onload = function(){
  // callback関数の設定
  ItemListManagement.getJsonData(getDataAfter)
}

// JSONデータ取得後の処理
function getDataAfter(){
  // 出力先の要素の取得
  const output = document.getElementById('itemList')
  // 商品リストの取得
  const itemList = ItemListManagement.itemList
  itemList.forEach(function(item,index){
    // HTMLへ出力する追加要素の生成
    const card = document.createElement('div')
    // クリックイベントのバインディング
    card.addEventListener('click',() => screenTransitionDetail(index))

    let outhtml = `
  <div class="item-card">
    <h2>${item.name}</h2>
    <img src="../img/${item.img}" alt="item ${index}">
    <p>¥${item.price}</p>
  </div>
`
      // 出力先の要素へ追加要素の出力
      card.innerHTML += outhtml
      output.appendChild(card)
    });
}


// 画面遷移を行う関数
function screenTransitionDetail(index){
  // 通常の画面遷移
  // location.href = 'detail.html?index=' + index
  // 新しいウィンドウを生成する。
  // ウィンドウのサイズを指定(新しいウィンドウを生成する条件でもある)
  let option = 'width=400,height=600'
  // 組み込みオブジェクトの関数open()を呼び出している。
  // サブウィンドウ(ポップアップ)と連携用に引数と取得
  const newwin = open('./detail.html','detail' , option);
  // 商品一つを取得
  const item = ItemListManagement.getItem(index)
  // ポップアップの表示が完了したときにmessageイベントを発生させる。
  // その時に、商品情報を送信
  newwin.onload = () => newwin.postMessage({item,index}, window.location.origin)
}

// 子ウィンドウ(詳細ウィンドウ)からカートに入れるボタンが押下された時の関数
function cartIn(itemIndex){
  // カートに追加処理
  cart.addItem(ItemListManagement.getItem(itemIndex))
  // セッションに追加処理 オブジェクト⇛JSON⇛セッションに追加
  const data = JSON.stringify(cart.itemList)
  window.sessionStorage.setItem('cartItems',data)
  // console.log(JSON.parse(window.sessionStorage.getItem('cartItems')))
}

// moduleの関数をwindowに追加(グローバルスコープ)
window.cartIn = cartIn