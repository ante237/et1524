import socket
import time
import sys

tcp_ip = "127.0.0.1"
tcp_port = 5005
TEST_MSG  = 'A'*1465
TIMER_OFFSET = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def setupReciever(ip = "127.0.0.1", port = 5005):
    print("Set up reciever")
    global tcp_ip
    global tcp_port
    tcp_ip = ip
    tcp_port = port

def streamData(frequency: int, duration: int, msg: str) -> int:
    '''
    Stream data to reciever.
    
    :param int frequency: The number of times per second to send data
    :param int duration: The duration over which to send data
    :param string str: The message to be sent
    :return int: Response code
    '''
    before = time.time()
    sock.connect((tcp_ip, tcp_port))
    sleepTime = 1 / (frequency + TIMER_OFFSET)
    pckCount = 0

    print(f"Begin sending packages to {tcp_ip}...")

    noOfPck = duration * frequency

    for i in range(noOfPck):
        pckCount  = pckCount + 1
        payload = str(10000 + pckCount) + ';' + msg + "####"
        sock.send(payload.encode())
        time.sleep(sleepTime)

    sock.close()
    timeTaken = round(time.time() - before, 2)
    print(f"Sent {noOfPck} packages in {timeTaken} seconds")
    return 0

def streamDataCont(duration: int, msg: str) -> int:
    '''
    Stream data to reciever.
    
    :param int duration: The duration over which to send data
    :param string str: The message to be sent
    :return int: Response code
    '''
    before = time.time()
    sock.connect((tcp_ip, tcp_port))
    pckCount = 0

    print(f"Begin sending packages to {tcp_ip}...")

    noOfPck = 0

    while(round(time.time() - before, 2) < duration):
        pckCount  = pckCount + 1
        payload = str(10000 + pckCount) + ';' + msg + "####"
        sock.send(payload.encode())
        # time.sleep(0)
        noOfPck = noOfPck + 1

    timeTaken = round(time.time() - before, 2)
    print(f"Sent {noOfPck} packages in {timeTaken} seconds")
    return 0

if __name__ == "__main__":
    print(sys.argv)
    if(len(sys.argv) > 4):
        setupReciever(sys.argv[3], int(sys.argv[4]))

    if(int(sys.argv[1]) == 0):
        streamDataCont(int(sys.argv[2]), TEST_MSG)
    else:
        streamData(int(sys.argv[1]), int(sys.argv[2]), TEST_MSG)