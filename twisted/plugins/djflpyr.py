import time

from zope import interface

from twisted.python import usage, reflect, threadpool, filepath
from twisted import plugin
from twisted.application import service, strports, internet
from twisted.web import wsgi, server, static
from twisted.internet import reactor


class Options(usage.Options):
    pass # We hard-code for simplicity

port_assignments = {
    'dj_sayhello.wsgi.application': 'tcp:8081',
    'fl_sayhello.app': 'tcp:8082',
    'pyr_sayhello.app': 'tcp:8083',
}

def update(fle, reactor):
    fle.setContent(time.ctime(reactor.seconds()))

@interface.implementer(service.IServiceMaker, plugin.IPlugin)
class ServiceMaker(object):
    tapname = "djflpyr"
    description = "Actually, Frankenstein is the doctor"
    options = Options

    def makeService(self, options):
        s = service.MultiService()
        for name, port in port_assignments.items():
            application = reflect.namedAny(name)
            pool = threadpool.ThreadPool()
            reactor.callWhenRunning(pool.start)
            reactor.addSystemEventTrigger('after', 'shutdown', pool.stop)
            root = wsgi.WSGIResource(reactor, pool, application)
            site = server.Site(root)
            strports.service(port, site).setServiceParent(s)
        root = static.File('data')
        site = server.Site(root)
        strports.service('tcp:8084', site).setServiceParent(s)
        fle = filepath.FilePath('data/time.txt')
        ts = internet.TimerService(1, update, fle, reactor)
        ts.setServiceParent(s)
        return s

serviceMaker = ServiceMaker()
