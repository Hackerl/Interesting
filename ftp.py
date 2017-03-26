from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
authorizer = DummyAuthorizer()
authorizer.add_anonymous("/home", perm='elradfmwM')
handler = FTPHandler
handler.authorizer = authorizer

handler.banner = "Server Ready.."

address = ("",21)
server = FTPServer(address, handler)

server.max_cons = 10
server.serve_forever()
