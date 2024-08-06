// 06 detail.js　従業員詳細

// ウィンドウが完全に読み込まれたらfunctionの中身が実行される
// この中に全部書く
window.onload = function () {

    // 出力準備
    let output = document.getElementById('output')

    // GETパラメータの取得する処理
    // URLオブジェクトを生成して現在のURLを取得
    let url = new URL(window.location.href)
    // パラメーター。複数系。情報を受け取る
    // URLSearchParamsオブジェクトを取得
    let params = url.searchParams
    // 'index'パラメータの値を取得
    let index = params.get('index')

    // JSONデータを取得して表示するための関数
    function empList() {
        // fetchはデータの取得(非同期通信)
        // 引数にはデータのURL(相対パス)
        fetch("../data/data.json")
            // response(URLから受け取った情報)をjsonに変換
            .then(response => response.json())
            // JSONデータを受け取って処理
            .then(json => {
                // コンソールログに表示
                console.log(json);

                // ループ外す
                // 変数membersHTMLを宣言して初期化
                let membersHTML = '';

                // インデックスを使用して特定のメンバーのデータを表示
                // 変数はmembers
                // 各変数はjsonを参照
                // 説明リスト<dl>で見た目を整える
                // 画像データのパスは "../data/${members[index].img}" にする(相対パス)
                // テンプレートリテラル`${}`で囲む
                membersHTML += `
                    <dl>
                        <dt>名前</dt>
                        <dd>${json.members[index].name}</dd>
                        <dt>年齢</dt>
                        <dd>${json.members[index].age}</dd>
                        <dt>写真</dt>
                        <dd><img src="../data/${json.members[index].img}"></dd>
                        <dt>詳細</dt>
                        <dd>${json.members[index].detail}</dd>
                    </dl>
                `;
                // membersHTMLをoutput.innerHTMLに代入
                output.innerHTML = membersHTML;

            //".then(json　"　の　"}" と ")"
            });

    // "function empList"　の　"}"
    }

    // function empListなのでempList関数を実行してデータを表示
    // これがないと表示されない
    empList();

}
