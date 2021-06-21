import os
print(os.uname())

import platform 
print (platform.platform())
print (platform.system())
print (platform.processor())
print (platform.architecture())
print (platform.node())
print (platform.release())
print (platform.version())
print (platform.machine())


import socket
hostname=socket.gethostname()
print(hostname)
ip=socket.gethostbyname(hostname)
print (ip)

import uuid
mac=(hex(uuid.getnode()))
print (mac)