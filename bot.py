#!/usr/bin/python2

import sys
from skeleton import *
from twisted.internet import reactor

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit('usage: ./bot.py <nick> <channel>')
    nick = sys.argv[1]
    chan = sys.argv[2]
    reactor.connectTCP('irc.freenode.net', 6667, DumbBotFactory('#' + chan, nick))
    reactor.run()
