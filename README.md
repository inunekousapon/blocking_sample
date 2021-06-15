Pythonによるノンブロッキング処理習作

## 概要

Pythonで並列・並行プログラミングをする際に必要な知識を身につける。

## やっていること

HTTPリクエストを同時実行できる。  
エラー処理は一切書いてない。

## 構成

- server.py 疑似APIサーバー
- client.py クライアントサーバー

## 起動

docker-compose up

実行結果
```
server_1  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
server_1  | INFO:     Started reloader process [12] using statreload
server_1  | INFO:     Started server process [14]
server_1  | INFO:     Waiting for application startup.
server_1  | INFO:     Application startup complete.
server_1  | INFO:     172.24.0.3:41146 - "GET / HTTP/1.1" 200 OK
server_1  | INFO:     172.24.0.3:41150 - "GET / HTTP/1.1" 200 OK
server_1  | INFO:     172.24.0.3:41152 - "GET / HTTP/1.1" 200 OK
server_1  | INFO:     172.24.0.3:41148 - "GET / HTTP/1.1" 200 OK
server_1  | INFO:     172.24.0.3:41154 - "GET / HTTP/1.1" 200 OK
client_1  | fileno:4
client_1  | HTTP/1.1 200 OK
client_1  | date: Tue, 15 Jun 2021 10:15:17 GMT
client_1  | server: uvicorn
client_1  | content-length: 19
client_1  | content-type: application/json
client_1  | Connection: close
client_1  | 
client_1  | ["wait time: 1sec"]
client_1  | fileno:5
client_1  | HTTP/1.1 200 OK
client_1  | date: Tue, 15 Jun 2021 10:15:17 GMT
client_1  | server: uvicorn
client_1  | content-length: 19
client_1  | content-type: application/json
client_1  | Connection: close
client_1  | 
client_1  | ["wait time: 3sec"]
client_1  | fileno:6
client_1  | HTTP/1.1 200 OK
client_1  | date: Tue, 15 Jun 2021 10:15:17 GMT
client_1  | server: uvicorn
client_1  | content-length: 19
client_1  | content-type: application/json
client_1  | Connection: close
client_1  | 
client_1  | ["wait time: 1sec"]
client_1  | fileno:7
client_1  | HTTP/1.1 200 OK
client_1  | date: Tue, 15 Jun 2021 10:15:17 GMT
client_1  | server: uvicorn
client_1  | content-length: 19
client_1  | content-type: application/json
client_1  | Connection: close
client_1  | 
client_1  | ["wait time: 3sec"]
client_1  | fileno:8
client_1  | HTTP/1.1 200 OK
client_1  | date: Tue, 15 Jun 2021 10:15:17 GMT
client_1  | server: uvicorn
client_1  | content-length: 19
client_1  | content-type: application/json
client_1  | Connection: close
client_1  | 
client_1  | ["wait time: 3sec"]
blocking_sample_client_1 exited with code 0
```

## 参考

https://nwpct1.hatenablog.com/entry/interprocess-communication