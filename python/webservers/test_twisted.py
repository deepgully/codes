from twisted.web import server, resource
from twisted.internet import reactor

class HelloResource(resource.Resource):
    isLeaf = True
    
    def render_GET(self, request):
        return "Hello, world"

reactor.listenTCP(7000, server.Site(HelloResource()))
reactor.run()