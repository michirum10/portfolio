/**
 * サイコロを振る
 * 
 * Math.random() を使用してランダムな数字を生成し、
 * 0 以上 6 以下の整数に変換します。
 * その数値を HTML 要素の innerHTML に設定します。
 */
function altRan() {
    // 0 以上 6 以下の整数を生成
    // Math.random() は 0 以上 1 未満の乱数を生成する
    // Math.floor() は引数の小数部分を切り捨てる
    // Math.random() * 6 は 0 以上 6 未満の乱数を生成する
    // +1 は 1 以上 6 以下の数値を生成する
    var r = Math.floor(Math.random() * 6) + 1;

    // 生成した数字を HTML 要素の innerHTML に設定
    // getElementById() は id 属性の値を指定して要素を取得する
    // innerHTML は HTML 要素の中身を取得・設定する
    document.getElementById("ran").innerHTML = r;
}
