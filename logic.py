#!/usr/bin/python2

import re

def privmsg(dumbot, user, channel, msg):
    # TODO more thorough owner checking than just nick - maybe hostmask?
    username = getUsername(user)
    if username in dumbot.owners:
        if channel == dumbot.nickname:               ### query
            replylocation = username
            command       = msg
        elif msg.startswith(dumbot.nickname + ': '): ### hilight in channel
            replylocation = channel
            command       = msg[len(dumbot.nickname + ': '):]
        else:
            return

        if command.startswith('join ') and command.count(' ') == 1:
            joinChannel(dumbot, command[len('join '):])

        elif command.startswith('part ') and command.count(' ') == 1:
            partChannel(dumbot, command[len('part '):])

        elif command == "list owners":
            listOwners(dumbot, replylocation)

        elif command.startswith('add owner ') and command.count(' ') == 2:
            addOwner(dumbot, command[len('add owner '):], replylocation)

        elif command.startswith('remove owner ') and command.count(' ') == 2:
            removeOwner(dumbot, command[len('remove owner '):], username, replylocation)

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
    dumbot.say(channel, 'what kind of idiot would ' + data + ', what a stupid thing to do')

def topicUpdated(dumbot, user, channel, newTopic):
    print('topicUpdated')

def userRename(dumbot, oldname, newname):
    print('userRename')

def receivedMOTD(dumbot, motd):
    print('receivedMOTD')


#### utility functions
def getUsername(user):
    return user[:user.index('!')]

def validName(name, search=re.compile(r'[^-_`~|@#%^&*+a-z0-9]').search):
    return not bool(search(name))

def joinChannel(dumbot, channel):
    if validName(channel):
        dumbot.join(channel)
        print('joined #' + channel)

def partChannel(dumbot, channel):
    if validName(channel):
        dumbot.leave(channel)
        print('left #' + channel)

def addOwner(dumbot, owner, replylocation):
    if validName(owner) and owner not in dumbot.owners:
        dumbot.owners.append(owner)
        print('added owner ' + owner)
        print('current list: %s' % dumbot.owners)
        with open(dumbot.factory.ownersfile, 'w') as f:
            for owner in dumbot.owners:
                f.write(owner + '\n')

def removeOwner(dumbot, owner, remover, replylocation):
    if (validName(owner)) and (owner in dumbot.owners):
        if owner == dumbot.owners[0]:
            dumbot.msg(replylocation, 'you mutinous bitch')
            owner = getUsername(remover)
            if owner == dumbot.owners[0] or owner not in dumbot.owners:
                return
        dumbot.owners.remove(owner)
        dumbot.msg(replylocation, 'removed owner ' + owner)
        with open(dumbot.factory.ownersfile, 'w') as f:
            for owner in dumbot.owners:
                f.write(owner + '\n')

def listOwners(dumbot, replylocation):
    ownerstring = ""
    for owner in dumbot.owners:
        ownerstring += owner + ', '
    ownerstring = ownerstring[:-2]
    dumbot.msg(replylocation, ownerstring)
