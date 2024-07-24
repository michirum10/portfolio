import Cart from "../js/Cart.js"
const output = document.getElementById('itemList')
if (window.sessionStorage.getItem('cartItems')) {
    // 出力先の要素の取得

    // カートのインスタンス化
    const cart = new Cart(JSON.parse(window.sessionStorage.getItem('cartItems')))
    cart.itemList.forEach(function (item) {

        let outhtml = `
  <div class="item-card">
    <h2>${item.name}</h2>
    <p>¥${item.price}</p>
  </div>
`
        // 出力先の要素へ追加要素の出力
        output.innerHTML += outhtml
    });
} else {
    let outhtml = `
  <div class="item-card">
    <p>カートの中は空っぽです。</p>
  </div>
`
    // 出力先の要素へ追加要素の出力
    output.innerHTML += outhtml
    document.getElementById('complete').remove()
}