import ftplib
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("Jopei","senhase", r"C:\Users\JoaoP\Documents\PythonFTP", "elradrmw")##Login 
handler = FTPHandler
handler.authorizer = authorizer
with FTPServer(("192.168.1.9", 21), handler) as server:
    server.max_cons = 3 ##Numero maximo de usuarios 
    server.max_cons_per_ip = 2 ##Numero de IPs constantes 
    server.serve_forever()
import ftplib
ftp = ftplib.FTP("192.168.1.9")

