## About CHaserOnlineWeb
> Note: このリポジトリは大学で、暇なときに作っているので更新が遅いかもです。許してね☻

CHaserOnlineWebは、[CHaserOnline](http://www.zenjouken.com/?page_id=62)をWeb版および、[Ruby](https://ja.wikipedia.org/wiki/Ruby)や[Python](https://ja.wikipedia.org/wiki/Python)などの他言語を[API](https://ja.wikipedia.org/wiki/API)で対応させるためのアプリケーションです。
CHaserOnlineWebは、次のような、ほとんどのクライアント作成過程で使用される一般的なタスクを簡素化することで、開発の負担を軽減しようとしています。
- 異なる[OS](https://ja.wikipedia.org/wiki/OS)上でクライアントの実行(WindowsからLinuxを操作するなど)
- 複数のユーザ管理(coolやcool2などの切替など)
- 固定されたプログラミング言語の移行([C言語](https://ja.wikipedia.org/wiki/C%E8%A8%80%E8%AA%9E)のみなど)
- CHaserOnlineの監視([端末](https://ja.wikipedia.org/wiki/%E7%AB%AF%E6%9C%AB%E3%82%A8%E3%83%9F%E3%83%A5%E3%83%AC%E3%83%BC%E3%82%BF)とブラウザを後者に統合して監視するなど)
- テキストエディタの統合([エディタ](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%87%E3%82%A3%E3%82%BF)をブラウザに統合するなど)

このように、CHaserOnlineWebは簡単に始めやすく、タスク管理とクライアント作成で必要なツールを提供します。
また、実行環境を各自で整える必要はなく、ブラウザさえあれば動作するポータブルソフトウェアになっています。

## Supported Operating Systems
CHaserOnline Webは、次のオペレーティングシステムに対応しています。

- **Windows:** Version 10 and above

## Installation
Gitの場合
```bash
git clone https://github.com/CHACCHAN/CHaserOnlineWeb.git
```

zipの場合
- [Download](https://github.com/CHACCHAN/CHaserOnlineWeb/archive/refs/heads/main.zip)

## Usage
> APIのみ使用したい方はこちらから
1. リポジトリをダウンロードしよう  
   `Installation`から、Gitコマンドか、直接ダウンロードします。
   > zipの場合は解凍してください。
   
   ![usage-1](https://raw.githubusercontent.com/CHACCHAN/CHaserOnlineWeb/main/docs/img/usage-1.png)

2. ファイル構成を確認しよう  
   `CHaserOnlineWeb/`の中身の説明  
   <pre>
   ├── CHaserOnline
   │   ├── Action.js
   │   ├── GetReady.js
   │   └── setting.json
   ├── python-3.12.3-embed-amd64
   │   └── // Python本体のため省略
   ├── server
   │   ├── db
   │   │   └── user.db
   │   ├── model
   │   │   └── user.py
   │   ├── apis.py
   │   ├── app.py
   │   ├── CHaserOnlineClient.py
   │   ├── config.py
   │   ├── routes.py
   │   └── module.py
   ├── web
   │   ├── dist
   │   │   └── // Web画面
   │   ├── public
   │   │   └── // 公開コンテンツ
   │   ├── src
   │   │   └── // ソースコード
   │   ︙
   ├── docs //ドキュメント
   ├── README.md
   └── run.bat
   </pre>

   - 其々のファイル/フォルダの解説
      - CHaserOnlineフォルダは[JavaScript](https://ja.wikipedia.org/wiki/JavaScript)でGetReady、Actionなどを記述できる場所です。
      - python-3.12.3-embed-amd64フォルダはPython Embeded版本体が入ってます。
      - serverフォルダはpython(flask)を用いたWebのサーバー側の処理を担うアプリケーションが付属しています。
      - webフォルダはブラウザで実際に表示されるHTMLやJavaScriptやCSSが含まれています。
      - docsフォルダはドキュメントが含まれています。
      - run.batは実行ファイルです。
   
   例 `CHaserOnline/GetReady.js`の中身
   
   ``` javascript
   function GetReady(returnNumber, ActionReturnNumber) {
       var GetReadyMode = 4;
       var param;
   
       if(ActionReturnNumber[1] >= 70 && ActionReturnNumber[1] <= 79) {
           GetReadyMode = 1;
       } else if(ActionReturnNumber[3] >= 70 && ActionReturnNumber[3] <= 79) {
           GetReadyMode = 3;
       } else if(ActionReturnNumber[5] >= 70 && ActionReturnNumber[5] <= 79) {
           GetReadyMode = 5;
       } else if(ActionReturnNumber[7] >= 70 && ActionReturnNumber[7] <= 79) {
           GetReadyMode = 7;
       } else {
           GetReadyMode = 4;
       }
   
       switch(GetReadyMode) {
           case 1:
               param = 'gru';
               break;
           case 3:
               param = 'grl';
               break;
           case 5:
               param = 'grr';
               break;
           case 7:
               param = 'grd';
               break;
           default:
               param = 'gr';
       }
   
       return param;
   }
   
   window.GetReady = GetReady;
   ```

3. サーバーを実行してみよう  
   `run.bat`をダブルクリックでサーバーとブラウザが起動します。

4. ブラウザから操作してみよう

5. JavaScriptでクライアントのプログラミングをしてみよう

## Technology used

## Notes

## Author
- 作成者 中山裕哉
- 所属 千葉工業大学
- E-mail chacchan.info@gmail.com

## License
The CHaserOnlineWeb is open-sourced software licensed under the [MIT license](https://github.com/laravel/framework/blob/11.x/LICENSE.md).
