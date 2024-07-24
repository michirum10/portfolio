// 簡易電卓

// 出力準備(値が変化する取得する要素を予め変数に格納しておく)
let num2 = document.getElementById("num2")
let result = document.getElementById("result")

// 定数
// 記号でも良い。。
// 数字に置き換えると容量少なく済む
const PLUS = '+'
const MINUS = '-'
const MULTIPLY = '*'
const DIVIDE = '/'
const MODULO = '%'

/// 出力文字列の生成(テンプレートリテラル)
// output = `計算結果：${counter}`
function calculate(mode) {
    // 前処理
    // num1n上のnum1と被らないように
    // タグの値の取得は.valueを利用する
   let num1n = Number(num1.value)
   let num2n = Number(num2.value)
   //  一応初期化
   let resultNum = 0


    // メイン処理
   switch (mode) {
      case PLUS:
      resultNum = num1n + num2n
         break;
      case MINUS:
         resultNum = num1n - num2n
         break;
      case MULTIPLY:
          resultNum = num1n * num2n
         break;
      case DIVIDE:
         resultNum = num1n / num2n
         break;
      case MODULO:
         resultNum = num1n % num2n
         break;
   
      default:
            break;
   }

    // 表示処理
    // ${mode}が記号
   let msg = `${num1n} ${mode} ${num2n} = ${resultNum}`
   result.textContent = msg
}
// 処理」を分けると可読性が上がる