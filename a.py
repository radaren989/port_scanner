import socket
import threading

def main():
    ip = input("Target IP: ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))

    constant = (end_port - start_port) // 20

    threads = []

    for i in range(19):
        threads.append(threading.Thread(target=check_port_series, args=(ip, start_port, start_port + i*constant + (i+1)*constant)))

    threads.append(threading.Thread(target=check_port_series, args=(ip, start_port + 3 * constant, end_port)))
    
    for th in threads:
        th.start()

    for th in threads:
        th.join()

def check_port_series(ip, start_port, end_port):
    for port in range(start_port, end_port):
        check_port(ip, port)

def check_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"Error checking port {port}: {e}")

if __name__ == "__main__":
    main()
