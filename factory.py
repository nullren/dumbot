#!/usr/bin/python2

import dumbot
import signal
import sys
import yaml
from twisted.internet import reactor, protocol

class DumBotFactory(protocol.ClientFactory):
    protocol   = dumbot.DumBot

    def __init__(self, config):
        self.config = config

    def clientConnectionLost(self, connector, reason):
        print("Lost connection (%s), reconnecting..." % (reason,))
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print("Could not connect: %s" % (reason,))

def SIGHUP_handler(num, frame):
    print("received SIGHUP")

if __name__ == "__main__":
    with open('config.yml', 'r') as f:
        config = yaml.load(f.read())

    reactor.connectTCP(config['host'], config['port'], DumBotFactory(config))
    signal.signal(signal.SIGHUP, SIGHUP_handler)
    reactor.run()
