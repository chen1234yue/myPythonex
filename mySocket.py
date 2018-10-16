import socket


try:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    print("create socket succ!")

    sock.bind(('localhost',8001))
    print('bind socket succ!')

    sock.listen(5)
    print('listen succ!')

except:
    print("init socket error!")

while True:
    print("listen for client...")
    conn,addr = sock.accept()
    print("get client")
    print(addr)

    conn.settimeout(30)
    szBuf=conn.recv(1024)
    print("recv:"+str(szBuf))

    if "0" == szBuf or "1"==szBuf or "2"==szBuf or "3"==szBuf or "4"==szBuf:
        conn.send(b"<http://dbpedia.org/resource/3WAY_FM>,<http://dbpedia.org/ontology/slogan>,\"Great Ocean Radio\"@en")
    else:
        conn.send(b"<http://dbpedia.org/resource/Adrian_Griffin>, <http://dbpedia.org/ontology/termPeriod>, <http://dbpedia.org/resource/Adrian_Griffin__5>,"
                  b"<http://dbpedia.org/resource/Adrian_Griffin>, <http://dbpedia.org/ontology/termPeriod>, <http://dbpedia.org/resource/Adrian_Griffin__5>,"
                  b"<http://dbpedia.org/resource/Adrian_Griffin>, <http://dbpedia.org/ontology/termPeriod>, <http://dbpedia.org/resource/Adrian_Griffin__5>,"
                  b"<http://dbpedia.org/resource/Adrian_Griffin>, <http://dbpedia.org/ontology/termPeriod>, <http://dbpedia.org/resource/Adrian_Griffin__5>,"
                  b"<http://dbpedia.org/resource/Adrian_Griffin>, <http://dbpedia.org/ontology/termPeriod>, <http://dbpedia.org/resource/Adrian_Griffin__5>")

    conn.close()
    print("end of servive")