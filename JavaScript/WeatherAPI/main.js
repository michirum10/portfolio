// ウィンドウが完全に読み込まれた後に実行される処理
// この中に全部書く
window.onload = function () {

    // 出力準備
    // HTMLのID=weatherをJS内の変数outputに格納
    let output = document.getElementById('weather');

    // "forecasts"情報を取得して表示する準備
    // 実行する関数を宣言
    function weather() {
        // fetchはデータの取得(非同期通信)
        // 引数にはデータのURL（相対パス）
        fetch("https://weather.tsukumijima.net/api/forecast/city/270000")
            // response(URLから受け取った情報)をjsonに変換
            .then(response => response.json())
            // JSONデータを受け取って処理
            .then(json => {
                // コンソールログに表示
                console.log(json);

                // 変数forecastsHTMLを宣言して初期化
                let forecastsHTML = '';
                // jsonのforecastsをそれぞれ取り出す(ループ処理)
                json.forecasts.forEach(forecast => {
                    // 各変数はjsonを参照
                    // divで見やすく
                    // 三項演算子を使ってnullの時は'--'と表示
                    // テンプレートリテラル`${}`で囲む
                    forecastsHTML += `
                        <div class="forecast">
                            <div class="date">${forecast.date}</div>
                            <div class="label">${forecast.dateLabel}</div>
                            <div class="weather">
                                <span>${forecast.telop}</span>
                                <img src="${forecast.image.url}" alt="${forecast.image.title}" width="${forecast.image.width}" height="${forecast.image.height}">
                            </div>
                            <div class="temperature">
                                <div>最低気温: ${forecast.temperature.min.celsius !== null ? forecast.temperature.min.celsius + ' ℃' : '--'}</div>
                                <div>最高気温: ${forecast.temperature.max.celsius !== null ? forecast.temperature.max.celsius + ' ℃' : '--'}</div>
                            </div>
                            <div class="chanceOfRain">
                                <div>0-6時: ${forecast.chanceOfRain.T00_06 !== null ? forecast.chanceOfRain.T00_06 : '--'}</div>
                                <div>6-12時: ${forecast.chanceOfRain.T06_12 !== null ? forecast.chanceOfRain.T06_12 : '--'}</div>
                                <div>12-18時: ${forecast.chanceOfRain.T12_18 !== null ? forecast.chanceOfRain.T12_18 : '--'}</div>
                                <div>18-24時: ${forecast.chanceOfRain.T18_24 !== null ? forecast.chanceOfRain.T18_24 : '--'}</div>
                            </div>
                        </div>
                    `;
                });

                // forecastsHTMLをoutput.innerHTMLに代入
                output.innerHTML = forecastsHTML;
            });
    }

    // weather関数を実行する
    // これがないと表示されない
    weather();
}
