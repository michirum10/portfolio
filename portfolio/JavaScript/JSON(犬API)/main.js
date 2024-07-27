// main.js

// 出力準備
let output = document.getElementById('output');
let fetchButton = document.getElementById('fetchButton');
let loadingIndicator = document.querySelector('.loading');

// 実行する関数(capture)を宣言
function capture() {
    // 画像取得前に表示
    output.alt = "画像取得中";
    output.src = ""; // 画像をクリア
    output.style.display = "none"; // 画像を非表示
    loadingIndicator.style.display = "block"; // ローディングインジケータを表示

    // fetchはデータの取得(非同期通信)
    fetch('https://dog.ceo/api/breeds/image/random')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(json => {
            console.log(json);
            output.src = json.message;
            output.alt = "犬の画像取得完了";
            
            // 画像の読み込みイベントを追加
            output.onload = function() {
                this.style.display = "block";
                loadingIndicator.style.display = "none";
            };
            output.onerror = function() {
                console.error('画像の読み込みに失敗しました');
                this.alt = "画像の読み込みに失敗しました";
                loadingIndicator.style.display = "none";
            };
        })
        .catch(error => {
            console.error('エラーが発生しました:', error);
            output.alt = "画像の取得に失敗しました";
            output.style.display = "none";
            loadingIndicator.style.display = "none";
        });
}

// ボタンクリック時に犬画像を取得
fetchButton.addEventListener('click', capture);