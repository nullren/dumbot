#!/usr/bin/python2

import re
import bitlyapi
import urllib2
import yaml
from bs4 import BeautifulSoup

def privmsg(dumbot, user, channel, msg):
    # TODO more thorough admin checking than just nick - maybe hostmask?
    usernick = getUsernick(user)
    if usernick in dumbot.config['admins']:
        commandmode = True
        if channel == dumbot.config['nick']:               ### query
            replylocation = usernick
            command       = msg
        elif msg.startswith(dumbot.config['nick'] + ': '): ### hilight in channel
            replylocation = channel
            command       = msg[len(dumbot.config['nick'] + ': '):]
        else:
            commandmode = False

        if commandmode:
            if command.startswith('join ') and command.count(' ') == 1:
                joinChannel(dumbot, command[len('join '):])

            elif command.startswith('part ') and command.count(' ') == 1:
                partChannel(dumbot, command[len('part '):])

            elif command == "list admins":
                listAdmins(dumbot, replylocation)

            elif command.startswith('add admin ') and command.count(' ') == 2:
                addAdmin(dumbot, command[len('add admin '):], replylocation)

            elif command.startswith('remove admin ') and command.count(' ') == 2:
                removeAdmin(dumbot, command[len('remove admin '):], usernick, replylocation)

    b = bitlyapi.BitLy(dumbot.config['bitly_user'], dumbot.config['bitly_key'])
    urls = getURLs(msg)
    if urls:
        print(urls)
        for url in urls:
            res = b.shorten(longUrl=url)
            soup = BeautifulSoup(urllib2.urlopen(url))
            dumbot.msg(channel, soup.title.string.encode() + ' - ' + res['url'].encode())
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
    # TODO hacked in, use actual config here
    print("Signed on as %s." % dumbot.config['nick'])
    dumbot.msg('nickserv', 'identify baumy 629784531')
    dumbot.msg('nickserv', 'release dumbot')
    dumbot.setNick(dumbot.config['nick'])
    for channel in dumbot.config['channels']:
        dumbot.join(channel)
        print("Joined %s" % channel)
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
    usernick = getUsernick(user)
    print('action')
    dumbot.say(channel, 'what kind of idiot would ' + data + ', what a stupid thing to do')
def topicUpdated(dumbot, user, channel, newTopic):
    print('topicUpdated')
def userRename(dumbot, oldname, newname):
    print('userRename')
def receivedMOTD(dumbot, motd):
    print('receivedMOTD')

#### utility functions
def getUsernick(user):
    return user[:user.index('!')]
def getURLs(msg):
    return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', msg)
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
def addAdmin(dumbot, admin, replylocation):
    if validName(admin) and admin not in dumbot.config['admins']:
        dumbot.config['admins'].append(admin)
        # print('added admin ' + admin)
        # print('current list: %s' % dumbot.config['admins'])
        dumbot.msg(replylocation, 'added admin ' + admin)
        # with open(dumbot.factory.adminsfile, 'w') as f:
            # for admin in dumbot.admins:
                # f.write(admin + '\n')
def removeAdmin(dumbot, admin, remover, replylocation):
    if (validName(admin)) and (admin in dumbot.config['admins']):
        if admin == dumbot.config['admins'][0]:
            dumbot.msg(replylocation, 'you mutinous bitch')
            admin = getUsernick(remover)
            if admin == dumbot.config['admins'][0] or admin not in dumbot.config['admins']:
                return
        dumbot.config['admins'].remove(admin)
        dumbot.msg(replylocation, 'removed admin ' + admin)
        # TODO dump config nicely
        with open('config.yml', 'w') as f:
            f.write(yaml.dump(dumbot.config))
def listAdmins(dumbot, replylocation):
    adminstring = ""
    for admin in dumbot.config['admins']:
        adminstring += admin + ', '
    adminstring = adminstring[:-2]
    dumbot.msg(replylocation, adminstring)
