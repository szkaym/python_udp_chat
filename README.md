# PythonでUDPソケット通信を行い簡単なチャットツールを作る

* 土曜日の13~14時 の1時間で前回のものを修正した

* UDPで接続
* グループチャットが可能
* 発言者がわかるようにしたい
* ~~チャットのログと発言ツールは分ける~~
    * おなじ画面にした
* ~~設定は外部ファイルにする~~
    * これは間に合わなかった。。

## SOKET を作成する

* ポートは `6080`を使用する
* IP指定
    * `client.py`でネットマスクを設定する
        * 例えば`192.168.11.255`

* socket モジュールについては公式ドキュメントを参考にする
    * https://docs.python.jp/3/library/socket.html

## 送信画面 受信画面は分けた

* threadを使用すれば1画面でできるが今回は2画面

### 送信画面
* `client.py`
    * gitbashだとなぜかうまく動かない ←
        * たぶん権限だと思う。
    * CMD、またはterminalで動かすこと。

### 受信画面
* `display.py`
    * gitbashだとなぜか(ry
    * CMD、またはterminalで動かすこと。

## コマンド
* client.py
    * `:quit`
        * 終了
    * `:help`
        * コマンドヘルプを表示する。
* display.py
    * 起動時に`:quit display`コマンドを打った時に入力する終了パスワードを設定する