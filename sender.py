import socket
import sys
import time

udp_ip = "127.0.0.1"
udp_port = 5005
TEST_MSG  = 'A'*1465

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def setupReciever(ip = "127.0.0.1", port = 5005):
    print("Set up reciever")
    global udp_ip
    global udp_port
    udp_ip = ip
    udp_port = port

def streamData(frequency: int, duration: int, msg: str) -> int:
    '''
    Stream data to reciever.
    
    :param int frequency: The number of times per second to send data
    :param int duration: The duration over which to send data
    :param string str: The message to be sent
    :return int: Response code
    '''
    before = time.time()
    sleepTime = 1 / (frequency + 2)
    pckCount = 0

    print(f"Begin sending packages to {udp_ip}...")

    noOfPck = duration * frequency

    for i in range(noOfPck):
        pckCount  = pckCount + 1
        payload = str(10000 + pckCount) + ';' + msg + "####"
        sock.sendto(payload.encode(), (udp_ip, udp_port))
        time.sleep(sleepTime)

    timeTaken = round(time.time() - before, 2)
    print(f"Sent {noOfPck} packages in {timeTaken} seconds")
    return 0

if __name__ == "__main__":
    print(sys.argv)
    if(len(sys.argv) > 4):
        setupReciever(sys.argv[3], int(sys.argv[4]))

    streamData(int(sys.argv[1]), int(sys.argv[2]), TEST_MSG)