from __future__ import absolute_import

import os

import pkg_resources

from zope import interface

from twisted.python import usage, reflect, threadpool, filepath
from twisted import plugin
from twisted.application import service, strports, internet
from twisted.web import wsgi, server, static, resource
from twisted.internet import reactor

import sayhello.wsgi

class Options(usage.Options):
    optParameters = [["port", None, None, "strports description of the port to "
                      "start the server on."],
                     ["empty-file", None, None, "create empty file with this name"],
                    ]

class EmptyFileMaker(service.Service):

    def __init__(self, fname):
        self.fname = fname

    def startService(self):
        if os.path.exists(self.fname):
            return
        with open(self.fname, 'a') as fp:
            pass
        service.Service.startService(self)

@interface.implementer(service.IServiceMaker, plugin.IPlugin)
class ServiceMaker(object):
    tapname = "sayhello"
    description = "Greet people nicely"
    options = Options

    def makeService(self, options):
        ret = service.MultiService()
        application = sayhello.wsgi.app
        pool = threadpool.ThreadPool()
        reactor.callWhenRunning(pool.start)
        reactor.addSystemEventTrigger('after', 'shutdown', pool.stop)
        wsgiresource = wsgi.WSGIResource(reactor, pool, application)
        index_loc = pkg_resources.resource_filename('sayhello', 'data/index.html')
        index = static.File(index_loc)
        root = resource.Resource()
        root.putChild('', index)
        root.putChild('hello', wsgiresource)
        site = server.Site(root)
        strports.service(options['port'], site).setServiceParent(ret)
        if options['empty-file'] != None:
            ef = EmptyFileMaker(options['empty-file'])
            ef.setServiceParent(ret)
        return ret

serviceMaker = ServiceMaker()
