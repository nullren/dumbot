#!/usr/bin/python2

import dumbot
import signal
import sys
from twisted.internet import reactor, protocol

class DumBotFactory(protocol.ClientFactory):
    protocol   = dumbot.DumBot
    ownersfile = 'owners.txt'

    def __init__(self, channel, nickname='dumbot'):
        self.channel  = channel
        self.nickname = nickname
        self.owners        = []
        with open(self.ownersfile, 'r') as f:
            for line in f:
                self.owners.extend([line.rstrip('\n')])

    def clientConnectionLost(self, connector, reason):
        print("Lost connection (%s), reconnecting..." % (reason,))
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print("Could not connect: %s" % (reason,))

def SIGHUP_handler(num, frame):
    print("received SIGHUP")
    reload(dumbot)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit('usage: ./bot.py <nick> <channel>')
    nick = sys.argv[1]
    chan = sys.argv[2]
    reactor.connectTCP('irc.freenode.net', 6667, DumBotFactory('#' + chan, nick))
    signal.signal(signal.SIGHUP, SIGHUP_handler)
    reactor.run()
