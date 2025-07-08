import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def setupSock(ip: str, port: int):
    sock.bind((ip, port))
    sock.listen(5)

def extractPckNr(payload: str):
    split = payload.split(';', 1)
    return int(split[0])

def checkOrder(new: int, prev: int):
    if(new - 1 != prev):
        print(f"{bcolors.FAIL} Wrong order: {new} after {prev}. {bcolors.ENDC}")
    return new

def listener():

    conn, addr = sock.accept()
    data = b""
    new = 10000
    old = 10000
    while(True):
        chunk = conn.recv(1518)
        data += chunk
        if(b"####" in data):
            split = data.split(b"####")
            new = extractPckNr(split[0].decode())
            data = split[1]
            #print(new)
            old = checkOrder(new, old)

if __name__ == "__main__":
    setupSock(sys.argv[1], int(sys.argv[2]))
    print("Begin listening")
    listener()
