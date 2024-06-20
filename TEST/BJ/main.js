// ブラックジャック

/*******************************************
グローバル変数
********************************************/
// 変数の初期化

// カードの山(配列)
let cards = [];
// 自分のカード(配列)
let myCards = [];
// 相手のカード(配列)
let comCards = [];
// 勝敗決定フラグ(論理型)
let isGameOver = false;  // 初期値: false(旗が下がってる状態)

/*******************************************
  イベントハンドラの割り当て
********************************************/
// メソッドチェーン
// 関数名().メソッドA().メソッドB()

// ページの読み込みが完了したとき実行する関数を登録
// loadHandler関数を実行
window.addEventListener('load', loadHandler);

// 「カードを引く」ボタンを押したとき実行する関数を登録
// querySelector: HTMLの選択した要素を取得
// #pickボタンが押されたら、clickPickHandler関数を実行
document.querySelector('#pick').addEventListener('click', clickPickHandler);

// 「勝負する！」ボタンを押したとき実行する関数を登録
document.querySelector('#judge').addEventListener('click', clickJudgeHandler);

// 「もう一回遊ぶ」ボタンを押したとき実行する関数を登録
document.querySelector('#reset').addEventListener('click', clickResetHandler);

/*******************************************
 イベントハンドラ
********************************************/

// ページの読み込みが完了したとき実行する関数を設定
function loadHandler() {
    // シャッフル
    shuffle();
    // 自分がカードを引く
    pickMyCard();
    // 相手がカードを引く
    picComCard();
    // 画面更新する
    updateView();
}

// 「カードを引く」ボタンを押したとき実行する関数
function clickPickHandler() {
    // 勝敗が未決定の時だけカードを引く
    if (isGameOver == false) {    // ゲームが終了していなければ(falseなら)条件が成立  // もし旗が降りてたら(勝敗が未決定なら)
        // 初期表示の関数を再利用
        // 自分がカードを引く関数
        pickMyCard();
        // 相手がカードを引く関数
        picComCard();
        // 画面更新する関数
        updateView();
    }
}

// 「勝負する！」ボタンを押したとき実行する関数
// judge(勝敗を判定)とshowResult(勝敗を表示)で分ける
function clickJudgeHandler() {
    // 勝敗をあらわす関数
    let result = "";    //初期化
    // 勝敗が未決定の時だけ勝負するボタン押せるようにする(勝敗が決まっていなければ何もしない)
    if (isGameOver == false) {   // もし旗が降りてたら(勝敗が未決定なら)
        // 勝敗を判定する
        result = judge();
        // 勝敗を画面に表示する
        showResult(result);
        // 勝敗決定フラグを「決定」に変更  // もし旗が降りてたら(勝敗が未決定なら)旗を上げる
        isGameOver = true;
    }
}

// 「もう一回遊ぶ」ボタンを押したとき実行する関数
function もう一回遊ぶ() {
    // 画面を初期表示にもどす
    // location.reloadメソッドでページを再読み込みする
}

/***********************************************
  ゲーム関数
************************************************/

// カードの山をシャッフルする関数
function shuffle() {
    // カードの初期化
    // カードの中に52個の配列要素を追加
    for (let i = 1; i <= 52; i++) {
        // カードに初期値を入れる
        cards.push = (i);    // push: 配列の末尾に要素を追加する
    }

    // 十分に混ぜるため100回繰り返す
    for (let i = 1; i <= 100; i++) {
        // カードの山からランダムに選んだ2枚を入れ替える
        // 0~51までのランダムな値を取得し「j」「k」に代入
        let j = Math.floor(Math.random() * 52);
        let k = Math.floor(Math.random() * 52);
        // cardds[j]とcards[k]を入れ替える
        let temp = cards[j];    // tempはtemporary(一時的)の略
        cards[j] = cards[k];
        cards[k] = temp;
    }
}

//自分がカードを引く関数
function pickMyCard() {
    // 自分のカードが４枚以下の場合
    if (myCards.length <= 4) {
        // カードの山(配列)から1枚取り出す
        let cards = cards.pop();    // pop: 配列の末尾から要素を取り出す
        // 取り出した(pop)カードを自分のカード(配列)に追加(push)する
        myCards.push(cards);
    }
}

//相手がカードを引く関数
function picComCard() {
    // カードは5枚までなので
    if (comCards.length <= 4) {
        // カードを引くかどうか考える
        // 考える(pickAI)関数を呼び出す
        if (pickAI(comCards)) {
            // カードの山(配列)から1枚取り出す
            let cards = cards.pop();
            // 取り出したカードを自分のカード(配列)に追加する
            comCards.push(cards);
        }
    }
}
// カードを引くかどうか考える関数
function pickAI(handCards) {
    // 現在のカードの合計を計算する
    let total = getTotal(handCards);
    // カードを引くかどうか
    let isPick = false;    // 引くならtrue、引かないならfalse

    // 合計が11以下なら「引く」
    if (total <= 11) {
        isPick = true;
    }
    // 合計が12~14なら80%の確立で「引く」
    else if (total >= 12 && total <= 14) {
        // randamメソッドを使って確率で引く
        if (Math.random() < 0.8) {
            isPick = true;
        }
    }
    // 合計が15~17なら35%の確立で「引く」
    else if (total >= 15 && total <= 17) {
        if (Math.random() < 0.35) {
            isPick = true;
        }
    }
    // 合計が18以上なら「引かない」
    else if (total >= 18) {
        isPick = false;
    }
    // 引くかひかないかを戻り値で返す
    return isPick;    // 引く(true)、引かない(false)を返す
}

// カードの合計を計算する関数
function getTotal(handCards) {
    let total = 0;    // 計算した合計を入れる変数
    let number = 0;    // カードの数字を入れる変数
    for (let i = 0; i < handCards.length; i++) {
        // カードの数字は余りで判断
        // 13で割った余りを求める
        number = handCards[i] % 13;
        // J,Q,K(余りが11,12,0)のカードは10とする
        if (number == 11 || number == 12 || number == 0) {
            total += 10;
        } else {
            total += number;
        }
    }
    // 「A」のカードを含んでいる場合
    // 配列に含まれている場合1,14,27,40のいずれかが入っている
    if (handCards.includes(1) || handCards.includes(14)
        || handCards.includes(27) || handCards.includes(40)) {    //includesメソッド: 配列に要素が含まれているか調べる
        // 「A」を11と数えても合計が21を越えなければ11と数える
        if (total + 10 <= 21) {
            total += 10;    //もし仮に合計に10を足しても21を超えないなら合計にさらに10を足す
        }
    }
    // 合計を返す
    return total;
}

// 画面を更新する関数
// カード引く度毎回行う
// 相手、自分のカードを引く関数の中に書かない
function updateView() {
    // 自分のカードを表示
    let myFields = document.querySelectorAll(".myCard");    //ノードが5つ入ったNodeListオブジェクトを返す
    for (let i = 0; i < myFields.length; i++) {    // 5つのノードを繰り返す
        // 自分のカードの枚数が1より大きい場合
        if (myCards.length > i) {
            // 表面の画像を表示する
            myFields[i].setAttribute('src', getCardPath(myCards[i]));    //src:属性を変更する//getCardPath:カードの画像パスを取得する関数を呼び出す
        } else {
            // 表面の画像を表示する
            myFields[i].setAttribute('src', 'blue.png');    //src属性を変更する
        }
    }
    // 相手のカードを表示
    let comFields = document.querySelectorAll(".comCard");    //ノードが5つ入ったNodeListオブジェクトを返す
    for (let i = 0; i < comCardsFields.length; i++) {    // 5つのノードを繰り返す
        // 相手のカードの枚数が1より大きい場合
        if (comCardsCards.length > i) {
            // 表面の画像を表示する
            comCardsFields[i].setAttribute('src', getCardPath(comCardsCards[i]));    //src:属性を変更する//getCardPath:カードの画像パスを取得する関数を呼び出す
        } else {
            // 表面の画像を表示する
            comCardsFields[i].setAttribute('src', 'red.png');    //src属性を変更する
        }
    }
    // カードの合計を再計算する
    // function getTotal
    document.querySelector('#myTotal').innerText = getTotal(mycards);
    document.querySelector('#comTotal').innerText = getTotal(comCardsCards);
}

// カードの画像パスを求める関数
function getCardPath(card) {
    // カードのパスを入れる変数
    let path = '';
    // カードの数字が１桁(9以下)なら先頭にゼロをつける
    if (card < 9) {
        path = '0' + card + '.png';
    } else {
        path = card + '.png';
    }
    return path;
}

// 自分のカードを表示する
for (iを5回繰り返す) {
    if (自分のカードの枚数がiより大きい) {
        // 表面の画像を表示する
    } else {
        // 表面の画像を表示する
    }
}

// 相手のカードを表示する  
for (iを5回繰り返す) {
    if (相手のカードの枚数がiより大きい) {
        // 表面の画像を表示する
    } else {
        // 表面の画像を表示する
    }
}

// 勝敗を判定する関数
function judge() {
    // 勝敗をあらわす関数
    let result = '';    //初期化
    // 自分のカードの合計を求める
    let myTotal = getTotal(myCards);
    // 相手のカードの合計を求める
    let comTotal = getTotal(comCards);
    // 勝敗のパターン表に当てはめて勝敗を決める
    if (myTotal > 21 && comTotal <= 21) {  // 自分21超え、相手が21以下
        result = 'lose';                   //負け
    } else if (comTotal <= 21 && myTotal > 21) {// 自分21以下、相手が21超え
        result = 'win';                   //勝ち
    } else if (comTotal > 21 && myTotal > 21) {// 自分21超え、相手が21超え
        result = 'draw';                   //引き分け
    }
    else {
        if (myTotal > comTotal) {    //自分も相手も21以下
            result = 'win';
        } else if (myTotal < comTotal) {
            result = 'lose';
        } else {
            result = 'draw';
        }
    }
    // 勝敗を呼び出し元に戻す
}

/***********************************************
  デバッグ関数
************************************************/

// デバッグ用の関数
function debug() {
    console.log('カードの山', カードの山);
    console.log('自分のカード', 自分のカード);
    console.log('相手のカード', 相手のカード);
    console.log('勝敗決定フラグ', 勝敗決定フラグ);
}