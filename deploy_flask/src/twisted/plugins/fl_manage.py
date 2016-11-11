import pkg_resources

from zope import interface

from twisted.python import usage, reflect, threadpool, filepath
from twisted import plugin
from twisted.application import service, strports, internet
from twisted.web import wsgi, server, static
from twisted.internet import reactor


class Options(usage.Options):
    optParameters = [["port", "p", None, "strports description of the port to "
                      "start the server on."],
    

@interface.implementer(service.IServiceMaker, plugin.IPlugin)
class ServiceMaker(object):
    tapname = "greeter"
    description = "Greet people nicely"
    options = Options

    def makeService(self, options):
        application = sayhello.wsgi.app
        pool = threadpool.ThreadPool()
        reactor.callWhenRunning(pool.start)
        reactor.addSystemEventTrigger('after', 'shutdown', pool.stop)
        wsgiresource = wsgi.WSGIResource(reactor, pool, application)
        index_loc = pkg_resource.resource_filename('sayhello', 'index.html')
        index = static.File(index_loc)
        root = resource.Resource()
        root.putChild('', index)
        root.putChild('hello', wsgi_resource)
        site = server.Site(root)
        ret = strports.service(port, site)
        return ret

serviceMaker = ServiceMaker()
