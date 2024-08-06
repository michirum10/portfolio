import Fan from "./Fan.js"

// チェイニング
// 新規ボタン
document.getElementById('new').addEventListener('click',() => new Fan())

// 全ての扇風機の電源をOFFにするボタン
document.getElementById('allOff').addEventListener('click', () => Fan.allOff())

// 全ての扇風機の電源をONにするボタン
document.getElementById('allOn').addEventListener('click', () => Fan.allOn())

