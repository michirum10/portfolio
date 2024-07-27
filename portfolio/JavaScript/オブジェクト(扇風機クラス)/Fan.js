// # 課題６：扇風機クラスの追加機能

// - 新規ボタンの右にボタンを二つ追加してください。
//   - １つ目のボタンはすべての扇風機の電源をOFFにする機能を持ちます。
//   - ２つ目のボタンはすべての扇風機の電源をONにする機能を持ちます。
//     - 電源を一度も入れたことがない扇風機は風力を弱に設定
//     - 電源を一度でも入れたことがある扇風機は風力を前回の設定に再設定

// 扇風機クラス
// ボタンの関数化

// exportで外から呼び出せる
// デフォルトモジュール出力
export default class Fan {

    // プロパティ

    // クラスプロパティ(状態)
    // 台数
    static #number = 0

    // 全体の状態出力先
    static #output

    // 扇風機のコレクションオブジェクト{}
    static #fanList = {}

    // クラス定数
    // windPowerの日本語名称の統一用定数
    static #POWER_STATUS = { OFF: '切', P1: '弱', P2: '中', P3: '強' }

    // プライベートプロパティ(状態)
    // シリアルナンバー
    #serialNumber
    // 羽根の枚数
    #blades
    // 風力
    #windPower
    // 電源
    #power
    // 首振り
    #swing
    // 個々の状態の出力先
    #deviceOutput
    // 直前の風力
    #previousWindPower

    // 全デバイスのオブジェクトリスト取得
    static get fanlist() {
        return Fan.#fanList
    }


    // クラスメソッド(動詞-名詞)
    // 扇風機の統計情報の表示
    static infoFans() {

        // もしundefined(エラー)の時に出力先を設定
        if (Fan.#output == undefined) {
            // 代入する
            Fan.#output = document.getElementById('output')
        }
        // コンソールにFanと入力して確認
        // console.log()
        Fan.#output.innerHTML += `扇風機の台数は全部で${Fan.#number}台です。`
    }

    // 全ての扇風機をOFFにする


    // コンストラクタ(メソッド)の宣言
    constructor(blades = 5) {
        // 扇風機の台数に一台追加        
        Fan.#number++
        this.#serialNumber = Fan.#number

        // 各値を初期化
        // オブジェクト化されてるときはthisをつける
        this.#blades = blades
        this.#windPower = Fan.#POWER_STATUS.OFF
        this.#power = false
        this.#swing = false
        this.#previousWindPower = Fan.#POWER_STATUS.OFF    // 直前の風力
        // this.#deviceOutput = null

        // #outputが設定されていない時、初期設定を行う処理
        if (Fan.#output === undefined) {
            // 代入する
            Fan.#output = document.getElementById('output')
        }

        // ブロック生成(divタグの生成)
        let block = document.createElement('div')

        // 各扇風機ブロックにIDを付与(シリアルナンバー)
        block.id = this.#serialNumber

        // 各扇風機ブロックの出力部分のdivタグを生成
        // #deviceOutputはinfoView(情報を表示)
        this.#deviceOutput = document.createElement('div')

        // blockの子要素に各扇風機ブロックの出力部分を追加
        // Child青教科書DOMツリーの子要素
        block.appendChild(this.#deviceOutput)

        // 全体の状態出力先の子要素に各扇風機ブロックを追加
        Fan.#output.appendChild(block)

        // 切ボタン生成
        createFanBtn(Fan.#POWER_STATUS.OFF, () => this.pressPowerButton(Fan.#POWER_STATUS.OFF), block)

        // 弱ボタン生成
        createFanBtn(Fan.#POWER_STATUS.P1, () => this.pressPowerButton(Fan.#POWER_STATUS.P1), block)

        // 中ボタン生成
        createFanBtn(Fan.#POWER_STATUS.P2, () => this.pressPowerButton(Fan.#POWER_STATUS.P2), block)

        // 強ボタン生成
        createFanBtn(Fan.#POWER_STATUS.P3, () => this.pressPowerButton(Fan.#POWER_STATUS.P3), block)

        // 首振りボタン生成
        createFanBtn('首振り', () => this.pressSwingButton(), block)

        // 削除ボタン生成
        createFanBtn('削除', () => {    // 無名アロー関数
            // コンソールに、削除する扇風機のシリアルナンバーを出力
            console.log(`扇風機${this.#serialNumber}を削除します。`)
            
            // block変数には現在の扇風機のブロック要素が格納
            // removeChild:引数に指定したノードを子ノードから削除

            // #outputの子要素である『block』を削除
            // 見かけの表示(divタグ)を削除
            Fan.#output.removeChild(block)  // 親はHTMLのoutput
            // データの中身を削除
            delete Fan.#fanList[this.#serialNumber]
        }, block)

        // 情報表示
        this.infoView()

        // データの管理
        // 連想配列
        Fan.#fanList[this.#serialNumber] = this    // 扇風機リストに追加
    }

    // メソッド(関数)

    // パワーボタングループ押下
    // pressPowerButtonメソッド
    pressPowerButton(btnName) {
        console.log(`パワーボタン『${btnName}』が押されました。`)
        switch (btnName) {
            case Fan.#POWER_STATUS.OFF:
                // 順番が大事

                // １．電源を切る前の風力を記録
                this.#previousWindPower = this.#windPower
                // ２．風力0
                this.#windPower = Fan.#POWER_STATUS.OFF
                // ３，電源OFF
                this.#power = false
                break;

            case Fan.#POWER_STATUS.P1:
                // 風力1
                this.#windPower = Fan.#POWER_STATUS.P1
                // 電源ON
                this.#power = true
                break;

            case Fan.#POWER_STATUS.P2:
                // 風力2
                this.#windPower = Fan.#POWER_STATUS.P2
                // 電源ON
                this.#power = true
                break;

            case Fan.#POWER_STATUS.P3:
                // 風力3
                this.#windPower = Fan.#POWER_STATUS.P3
                // 電源ON
                this.#power = true
                break;

            default:
                break;
        }
        this.infoView()
    }

    // メソッド(関数)
    // 首振りボタン押下
    pressSwingButton() {
        // コンソール出力に処理の切り替え
        console.log('首振りボタンが押されました。' + '<br>')
        // 現在の状態を反転させる処理
        this.#swing = !this.#swing
        this.infoView()
    }

    // 状態確認
    infoView() {
        // console.logで状態確認
        console.log(Fan.fanlist)
        // outputは状態の出力先から
        this.#deviceOutput.innerHTML = `
        シリアルナンバー：${this.#serialNumber}<br>
        羽根の枚数：${this.#blades}<br>
        風力：${this.#windPower}<br>
        電源：${this.#power}<br>
        首振り：${this.#swing}<br>
        TimeStamp：${new Date()}<br>`
    }

    // 「全オフ」「全オン」ボタンの追加

    // 全ての扇風機をOFFにする
    // 全デバイスのオブジェクトリストを使う
    // forループで全ての扇風機をオフに
    // 配列[key]を使って全てのオブジェクト(#fanListから)を取得
    static allOff() {
        // Object.values:オブジェクト(Fan.#fanList)に存在する値(values)を配列に変換
        // ループ(forEach)させる
        Object.values(Fan.#fanList).forEach(fan => {
            // 電源オフに
            fan.pressPowerButton(Fan.#POWER_STATUS.OFF)
        });
        console.log(Fan.#fanList)
        // for-in文オブジェクトに使用できる繰り返し処理
        // for(key（変数名） in obj)という形
        // for (let key in Fan.#fanList) {
        //     Fan.#fanList[key].pressPowerButton(Fan.#POWER_STATUS.OFF);
        // }
    }

    // 全ての扇風機をONにする
    //  電源がOFFの場合、前回の風力設定に基づいて風力を設定
    //  前回の風力設定がOFFの場合、風力を弱に設定
    static allOn() {
        // Object.valuesで配列の値を取得してforEachループ
        Object.values(Fan.#fanList).forEach(fan => {

            // もし電源がオフの場合
            if (fan.#windPower == Fan.#POWER_STATUS.OFF) {    // == 等価演算子:比較する際に「値」をチェックする
                if (fan.#previousWindPower == Fan.#POWER_STATUS.OFF) {    // 前回が電源オフの場合
                    fan.pressPowerButton(Fan.#POWER_STATUS.P1)      // 風力を弱に設定
                } else {                                           // 前回オフじゃなければ
                    fan.pressPowerButton(fan.#previousWindPower)   // 前回の風力を設定
                }
            }
        })
        console.log(Fan.#fanList)
        // for-in文
        //     for (let key in Fan.#fanList) {
        //         let fan = Fan.#fanList[key]    // 現在の扇風機を取得
    }
}

// グローバル関数(外に準備)
// 扇風機のボタン生成関数
function createFanBtn(value, handler, parent) {   //引数には変わる値(value:切,handler:() => this.pressPowerButton(Fan.#POWER_STATUS.P3),parent:block)を入れる
    // inputタグを生成
    let btn = document.createElement('input')
    // ボタンの各設定
    // タイプの指定
    // inputなのでtype属性を指定できる
    btn.type = 'button'
    // valueの指定
    btn.value = value  //変わる
    // イベント指定
    btn.addEventListener('click', handler)  //変わる
    // ボタンをparentの子要素に追加
    parent.appendChild(btn)
}
