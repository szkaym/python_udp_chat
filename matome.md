# PythonでUDPソケット通信を行い簡単なチャットツールを作る

* UDPで接続
* グループチャットが可能
* 発言者がわかるようにしたい
* チャットのログと発言ツールは分ける
* 設定は外部ファイルにする

## SOKET を作成する

* ポートは `61080`を使用する
* IP指定はしない

* socket モジュールについては公式ドキュメントを参考にする
    * https://docs.python.jp/3/library/socket.html

```python

import socket

ip = ''
port = 6080

soc = socket.socket(socket.AF_INET, socket.SOC_DGRAM)

```