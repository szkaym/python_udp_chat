# PythonでUDPソケット通信を行い簡単なチャットツールを作る

* 土曜日の13~15時 の2時間で作成

> *  第1回 Python勉強会@仙台
>     * https://www.facebook.com/events/156896251599013/

* UDPで接続
* グループチャットが可能
* 発言者がわかるようにしたい
* チャットのログと発言ツールは分ける
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
    * `:quit display`
        * `display.py`の終了命令を出す。
        * 次の入力でdisplay.pyを起動したときに設定したパスワードを入力することで終了させる。
    * `:quit`
        * `client.py`を終了させる。
    * `:help`
        * コマンドヘルプを表示する。
* display.py
    * 起動時に`:quit display`コマンドを打った時に入力する終了パスワードを設定する