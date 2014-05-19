#!/usr/bin/python2

from twisted.words.protocols import irc
import logic

class DumBot(irc.IRCClient):
    def _get_nickname(self):
        return self.factory.nickname
    def _get_owners(self):
        return self.factory.owners

    reloadstring = 'im sorry i wasnt good enough =('
    owners       = property(_get_owners)
    nickname     = property(_get_nickname)

    def privmsg(self, user, channel, msg):
        if (msg.startswith(self.nickname + ': reload') or (self.nickname == channel and msg == 'reload')):
            username = logic.getUsername(user)
            if username in self.owners:
                if self.nickname == channel: # query
                    self.msg(username, self.reloadstring)
                else:
                    self.msg(channel, self.reloadstring)
                reload(logic)
                print('i reloaded!')
                return
        logic.privmsg(self, user, channel, msg)

    def created(self, when):
        logic.created(self, when)
    def yourHost(self, info):
        logic.yourHost(self, info)
    def myInfo(self, servername, version, umodes, cmodes):
        logic.myInfo(self, servername, version, umodes, cmodes)
    def luserClient(self, info):
        logic.luserClient(self, info)
    def bounce(self, info):
        logic.bounce(self, info)
    def isupport(self, options):
        logic.isupport(self, options)
    def luserChannels(self, channels):
        logic.luserChannels(self, channels)
    def luserOp(self, ops):
        logic.luserOp(self, ops)
    def luserMe(self, info):
        logic.luserMe(self, info)
    def joined(self, channel):
        logic.joined(self, channel)
    def left(self, channel):
        logic.left(self, channel)
    def noticed(self, user, channel, msg):
        logic.noticed(self, user, channel, msg)
    def modeChanged(self, user, channel, set, modes, args):
        logic.modeChanged(self, user, channel, set, modes, args)
    def pong(self, user, secs):
        logic.pong(self, user, secs)
    def signedOn(self):
        logic.signedOn(self)
    def kickedFrom(self, channel, kicker, message):
        logic.kickedFrom(self, channel, kicker, message)
    def nickChanged(self, nick):
        logic.nickChanged(self, nick)
    def userJoined(self, user, channel):
        logic.userJoined(self, user, channel)
    def userLeft(self, user, channel):
        logic.userLeft(self, user, channel)
    def userQuit(self, user, quitMessage):
        logic.userQuit(self, user, quitMessage)
    def userKicked(self, kickee, channel, kicker, message):
        logic.userKicked(self, kickee, channel, kicker, message)
    def action(self, user, channel, data):
        logic.action(self, user, channel, data)
    def topicUpdated(self, user, channel, newTopic):
        logic.topicUpdated(self, user, channel, newTopic)
    def userRename(self, oldname, newname):
        logic.userRename(self, oldname, newname)
    def receivedMOTD(self, motd):
        logic.receivedMOTD(self, motd)
