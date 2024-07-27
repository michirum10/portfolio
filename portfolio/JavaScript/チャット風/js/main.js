// 人物分岐用定数、CSSのクラス名と一緒
const ASAN = 'Asan';
const BSAN = 'Bsan';
const RESET = 'reset';

const input = document.getElementById('num1');
const output = document.getElementById('output');

function btn(action) {
    switch (action) {
        case ASAN:
        case BSAN:
            sendMessage(action);
            break;
        case RESET:
            reset();
            break;
    }
}

function sendMessage(name) {
    // 入力されたメッセージが空の時
    if (input.value === '') {
        // 処理を中断する
        return;
    }

    let className = `${name.toLowerCase()} msg`;
    // 表示名の準備
    let dispName = '';
    switch (name) {
        case ASAN:
            dispName = 'Aさん';
            break;
        case BSAN:
            dispName = 'Bさん';
            break;
    }

    // 現在の時刻の取得
    let now = new Date();
    // 日本の形式の時刻表示に変換
    let nowf = now.toLocaleString('ja-JP');
    // タグ生成
    let inputStr = 
`<dt class='${className}'>
    ${nowf} : ${dispName}
</dt>
<dd class='${className}'>
    ${input.value}
</dd>`;

    output.innerHTML += inputStr;
    input.value = '';
}

function reset() {
    output.innerHTML = '';
    input.value = '';
}
