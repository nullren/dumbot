#!/usr/bin/python2

from twisted.words.protocols import irc
import logic

class DumBot(irc.IRCClient):
    reloadstring = 'im sorry i wasnt good enough =('

    def _get_nickname(self):
        return self.factory.nickname
    nickname = property(_get_nickname)

    def signedOn(self):
        logic.signedOn(self)

    def joined(self, channel):
        logic.joined(self, channel)

    def privmsg(self, user, channel, msg):
        print('PRIVMSG: ' + user + '::' + channel + '::' + msg)
        if (self.nickname in msg or self.nickname == channel) and 'reload' in msg:
            if self.nickname == channel: # query
                username = user[:user.index('!')]
                print('sending message to ' + username)
                self.msg(username, self.reloadstring)
            else:
                self.msg(channel, self.reloadstring)
            reload(logic)
            return
        logic.privmsg(self, user, channel, msg)

    def noticed(self, user, channel, msg):
        logic.noticed(self, user, channel, msg)

