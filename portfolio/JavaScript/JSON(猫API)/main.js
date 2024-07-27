// main.js
// 猫は配列に格納されている

// 出力準備
let output = document.getElementById('output');
let fetchButton = document.getElementById('fetchButton');
let loadingIndicator = document.querySelector('.loading');

// 実行する関数(capture)を宣言
function capture() {
    // 画像取得前に表示するメッセージを設定
    output.alt = "画像取得中";
    
    // 画像のsrcを空にして、前の画像をクリア
    output.src = ""; 
    
    // 画像を非表示にする
    output.style.display = "none"; 
    
    // ローディングインジケータを表示
    loadingIndicator.style.display = "block"; 

    // APIから猫の画像を取得するためのfetchリクエストを送信
    fetch('https://api.thecatapi.com/v1/images/search')
        .then(response => {
            // レスポンスが正常でない場合、エラーを投げる
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            // レスポンスをJSON形式に変換して返す
            return response.json();
        })
        .then(json => {
            // 取得したJSONデータをコンソールに表示
            console.log(json);
            
            // 画像の読み込みが完了したときの処理
            output.onload = function() {
                // 画像を表示
                this.style.display = "block";
                // ローディングインジケータを非表示にする
                loadingIndicator.style.display = "none";
            };
            
            // 画像の読み込みに失敗したときの処理
            output.onerror = function() {
                // エラーメッセージをコンソールに表示
                console.error('画像の読み込みに失敗しました');
                // 代替テキストを設定
                this.alt = "画像の読み込みに失敗しました";
                // ローディングインジケータを非表示にする
                loadingIndicator.style.display = "none";
            };
            
            // 取得した猫の画像のURLをsrcに設定
            output.src = json[0].url; 
            // 画像取得完了のメッセージを設定
            output.alt = "猫の画像取得完了";
        })
        .catch(error => {
            // エラーが発生した場合の処理
            console.error('エラーが発生しました:', error);
            // エラーメッセージを設定
            output.alt = "画像の取得に失敗しました";
            // 画像を非表示にする
            output.style.display = "none";
            // ローディングインジケータを非表示にする
            loadingIndicator.style.display = "none";
        });
}

// ボタンクリック時に猫画像を取得
fetchButton.addEventListener('click', capture);