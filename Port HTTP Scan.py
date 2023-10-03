import socket
import requests

def get_host_by_name(host):
    try:
        ip = socket.gethostbyname(host)
        print(f"Host: {host} has IP: {ip}")
        return ip
    except:
        print(f"Could not resolve host: {host}")
        return None

def scan_host(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        con = s.connect((host, port))
        print(f"Port {port} is open on host {host}")
        con.close()
        return True
    except:
        print(f"Port {port} is closed on host {host}")
        return False

def get_http_info(host, port):
    url = f"http://{host}:{port}"
    try:
        response = requests.get(url)
        print(f"HTTP response status code: {response.status_code}")
        print(f"HTTP response headers: {response.headers}")
        print(f"HTTP response content: {response.text}")
    except:
        print(f"Could not get information from HTTP service on {url}")

def main():
    host = input("Enter the host name or IP address: ")
    ip = get_host_by_name(host)
    if ip:
        for port in range(1,1024):
            if scan_host(host, port):
                if port == 80:
                    get_http_info(host, port)

if __name__ == "__main__":
    main()
