import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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

def extractPckNr(payload: str):
    return int(payload.split(';', 1)[0])

def checkOrder(new: int, prev: int):
    if(new - 1 != prev):
        print(f"{bcolors.FAIL} Wrong order: {new} after {prev}, expected {prev + 1}. {bcolors.ENDC}")
    return new

def listener():
    new = 10000
    old = 10000
    while(True):
        data, addr = sock.recvfrom(1518)
        data.decode()
        new = extractPckNr(data)
        print(new)
        old = checkOrder(new, old)

if __name__ == "__main__":
    setupSock(sys.argv[1], int(sys.argv[2]))
    listener()
