#!/usr/bin/python2

def signedOn(dumbot):
    dumbot.join(dumbot.factory.channel)
    print("Signed on as %s." % (dumbot.nickname))

def joined(dumbot, channel):
    print("Joined %s." % (channel))

def privmsg(dumbot, user, channel, msg):
    if channel == dumbot.nickname:
        print('I was queried!')
    if channel:
        if dumbot.nickname in msg:
            dumbot.say(channel, 'suck me')

def noticed(dumbot, user, channel, msg):
    print('NOTICED ' + channel + ' | ' + user + ' ' + msg)

#### utility functions
def getUsername(user):
    return user[:user.index('!')]

