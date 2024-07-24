// 06 main.js 従業員一覧

// ウィンドウが完全に読み込まれたらfunctionの中身が実行される
// この中に全部書く
window.onload = function () {

    // 出力準備
    // HTMLのID=empListをJSの変数outputに格納
    let output = document.getElementById('output');

    // JSONデータを取得し、それを元にHTML要素を構築して表示する関数を宣言
    // 実行する関数を宣言
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

                // ここからforEachループ
                // 変数membersHTMLを宣言して初期化
                let membersHTML = '';
                // jsonのmembers(member)をそれぞれ取り出す(ループ処理)
                // 教科書実践編のp114
                // members情報のindex番目を参照
                json.members.forEach(function (member, index) {
                    // 説明リストで見た目を整える
                    // 画像データのパスは "../data/${変数.img}" にする(相対パス)
                    // 各変数はjsonを参照
                    // テンプレートリテラル`${}`で囲む

                    // onclick="window.location.href = 'URL(相対パス)'"クリックすると詳細画面(index.html)に遷移
                    // onclickでメンバーのindex番目に画面遷移
                    membersHTML += `
                        <dl onclick="window.location.href = '../html/detail.html?index=${index}'">
                            <dt>名前</dt>
                            <dd>${member.name}</dd>
                            <dt>写真</dt>
                            <dd><img src="../data/${member.img}"></dd>
                        </dl>
                    `;

                // "json.members.forEach"　の　"}" と ")"
                });

                // membersHTMLをoutput.innerHTMLに代入
                output.innerHTML = membersHTML;

            //".then(json　"　の　"}" と ")"
            });

    // "function empList"　の　"}"
    }

    // function empListなのでempList関数を実行する
    // これがないと表示されない
    empList();

// "window.onload = function"　の　"}"
}

// 順番
// window.onload: ページが完全に読み込まれた後に実行される
// function empList: empListを実行する関数
// fetch: JSONデータを取得する
// forEach: JSONデータを一つずつ取り出すループ

// JSONデータの中身は配列の配列
// .は～の～という意味