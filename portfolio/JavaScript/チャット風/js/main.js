const Asan = 'Asan'
const Bsan = 'Bsan'

const input = document.getElementById('input')
const output = document.getElementById('output')

function sendMessage(name){
    // 入力されたメッセージが空の時
    if(input.value == ''){
        // 処理を中断する
        return
    }

    let className = `${name} msg`
    // 表示名の準備
    let dispName = ''
    switch(name){
        case Asan:
            dispName = 'Aさん'
            break
        case Bsan:
            dispName = 'Bさん'
            break
    }

    // 現在の時刻の取得
    let now = new Date()
    // 日本の形式の時刻表示に変換
    let nowf = now.toLocaleString('ja-JP');
    // タグ生成
    let inputStr = 
`<dt class='${className}'>
    ${now} : ${dispName}
</dt>
<dd class='${className}'>
    ${input.value}
</dd>`

    output.innerHTML += inputStr
    input.value = ''
}

function reset(){
    output.innerHTML = ''
    input.value = ''
}
