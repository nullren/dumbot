#!/usr/bin/python2

import re

def privmsg(dumbot, user, channel, msg):
    if channel == dumbot.nickname: # query
        if getUsername(user) == dumbot.owner: # query from owner
            if msg.startswith('join ') and msg.count(' ') == 1:
                newchannel = msg.lstrip('join ')
                if validName(newchannel):
                    dumbot.join(newchannel)
            if msg.startswith('part ') and msg.count(' ') == 1:
                oldchannel = msg.lstrip('part ')
                if validName(oldchannel):
                    dumbot.leave(oldchannel)

    if channel:
        if dumbot.nickname in msg:
            dumbot.say(channel, 'LolLeRbEArS')

def created(dumbot, when):
    print('created')

def yourHost(dumbot, info):
    print('yourHost')

def myInfo(dumbot, servername, version, umodes, cmodes):
    print('myInfo')

def luserClient(dumbot, info):
    print('luserClient')

def bounce(dumbot, info):
    print('bounce')

def isupport(self, options):
    print('isupport')

def luserChannels(dumbot, channels):
    print('luserChannels')

def luserOp(dumbot, ops):
    print('luserOp')

def luserMe(self, info):
    print('luserMe')

def joined(dumbot, channel):
    print("Joined %s." % (channel))

def left(dumbot, channel):
    print('left')

def noticed(dumbot, user, channel, msg):
    print('NOTICED ' + channel + ' | ' + user + ' ' + msg)

def modeChanged(dumbot, user, channel, set, modes, args):
    print('modeChanged')

def pong(self, user, secs):
    print('pong')

def signedOn(dumbot):
    dumbot.join(dumbot.factory.channel)
    print("Signed on as %s." % (dumbot.nickname))

def kickedFrom(dumbot, channel, kicker, message):
    print('kickedFrom')

def nickChanged(dumbot, nick):
    print('nickChanged')

def userJoined(dumbot, user, channel):
    print('userJoined')

def userLeft(dumbot, user, channel):
    print('userLeft')

def userQuit(dumbot, user, quitMessage):
    print('userQuit')

def userKicked(dumbot, kickee, channel, kicker, message):
    print('userKicked')

def action(dumbot, user, channel, data):
    username = getUsername(user)
    print('action')
    # dumbot.msg(username, 'why the fuck would you "' + data + '" you faggot')
    dumbot.say(channel, 'why the fuck would you "' + data + '" you faggot')

def topicUpdated(dumbot, user, channel, newTopic):
    print('topicUpdated')

def userRename(dumbot, oldname, newname):
    print('userRename')

def receivedMOTD(dumbot, motd):
    print('receivedMOTD')


#### utility functions
def getUsername(user):
    return user[:user.index('!')]

def validName(name, search=re.compile(r'[^a-z0-9]').search):
    return not bool(search(name))
