import select
import socket


# 未使用
def socket_connet():
    # ソケットを発行する
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # サーバーと接続する
    soc.connect(('server', 8000))
    return soc


# 未使用
def send_request(soc, path):
    request_msg = f'''GET {path} HTTP/1.1
Host: server
Connection: close

'''.encode('ascii')
    # リクエスト送信
    total_sent = 0
    while total_sent < len(request_msg):
        sent = soc.send(request_msg[total_sent:])
        if sent == 0:
            raise RuntimeError("send error")
        total_sent += sent


def epoll_fetch(paths, poller):
    connections = {}
    request = {}
    reponses = {}
    for path in paths:
        # ソケット接続
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect(('server', 8000))
        # ソケットのファイルNoを監視する
        fileno = soc.fileno()
        # まずはEPOLLOUT監視して出力を見張る
        poller.register(fileno, select.EPOLLOUT)
        # それぞれのソケットのリクエストとレスポンスを持つ
        connections[fileno] = soc
        reponses[fileno] = b''
        request[fileno] = f'''GET {path} HTTP/1.1
Host: server
Connection: close

'''.encode('ascii')

    while connections:
        events = poller.poll()
        for fd, event in events:
            if event & select.EPOLLIN:
                # レスポンス受信側
                recv = connections[fd].recv(1024)
                # 何も受信しなかったらソケットクローズして接続を削除
                if not recv:
                    connections[fd].shutdown(socket.SHUT_RDWR)
                    connections[fd].close()
                    del connections[fd]
                reponses[fd] += recv
            elif event & select.EPOLLOUT:
                # リクエスト送信側
                sent = connections[fd].send(request[fd])
                if sent == 0:
                    raise RuntimeError("send error")
                request[fd] = request[fd][sent:]
                if not request[fd]:
                    # 全部送信し切ったら、次は受信側を監視する
                    poller.modify(fd, select.EPOLLIN)

    return reponses


# 未使用
def recv_response(soc):
    chunks = b''
    total_received = 0
    while True:
        chunk = soc.recv(1024)
        if not chunk:
            break
        chunks += chunk
        total_received += len(chunk)

    soc.shutdown(socket.SHUT_RDWR)
    soc.close()

    return chunks.decode('ascii')


def main():
    # こいつでファイルを監視
    poller = select.epoll()
    responses = epoll_fetch(['/','/','/','/','/'], poller)
    for fd, response in responses.items():
        print(f"fileno:{fd}")
        print(response.decode('ascii'))


if __name__ == '__main__':
    main()
