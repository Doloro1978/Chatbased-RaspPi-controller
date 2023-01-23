import socket
import json

linux_hostnames = []

def connect(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((hostname, port))
    sock.close()
    return result == 0

for i in range(0,255):
    res = connect("192.168.0."+str(i), 22)
    print("Port " + str(i))
    if res:
        temp_hostname = False
        print("Device found at: ", "192.168.0."+str(i) + ":"+str(22))
        try:
            temp_hostname = socket.gethostbyaddr(str("192.168.0."+str(i)))
        except:
            print("Cant find hostname")
        if temp_hostname:
            print("Device hostname :" + str(temp_hostname))
            linux_hostnames.append(str(temp_hostname[0]+".local | " + "192.168.0."+str(i)))
        else:
            linux_hostnames.append(str("unavailable | " + "192.168.0."+str(i)))
    print(linux_hostnames)
xc = {
    "Setup" : True,
    "pis" : {
        0 : {   
        },
        1 : {   
        },
        2 : {   
        },
        3 : {   
        },
        4 : {   
        },
        5 : {   
        },
        6 : {   
        },
        7 : {   
        },
        8 : {   
        },
        9 : {   
        },
        10 : {   
        }
    }
}
spliced_ips = []
spliced_hostnames = []
for x in linux_hostnames:
    print(x)
    split_off = x.find("|")
    split_off = split_off + 1
    lenn = len(x)
    ip = x[split_off:lenn]
    hostname = x[0:(split_off-1)]
    ip = ip.strip()
    hostname = hostname.strip()
    spliced_ips.append(ip)
    spliced_hostnames.append(hostname)
for x in range(len(spliced_ips)):
    ip = spliced_ips[x]
    host = spliced_hostnames[x]
    xc["pis"][x]["ip"] = ip
    xc["pis"][x]["hostname"] = host

print(json.dumps(xc))
temp = json.dumps(xc)
f = open("ip_config.txt", "w")
f.write(temp)
f.close
        