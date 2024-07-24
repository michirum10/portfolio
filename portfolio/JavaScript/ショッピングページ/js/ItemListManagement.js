export default class ItemListManagement{
    // 商品リストの配列
    static #itemList = []

    // JSONからデータの取得
    static getJsonData(callback){
        fetch('../data/data.json')
        .then(response => response.json())
        .then(data => {
            console.log('JSONファイルの内容:')
            console.log(data)
            this.#itemList = Object.values(data.items)
            // callback処理の実行
            callback()
        }).catch(error => {
            console.error('エラー:', error);
        });
    }

    // 商品リスト取得
    static get itemList(){
        return this.#itemList
    }

    // 単品取得
    static getItem(index){
        return this.#itemList[index]
    }
}