#!/usr/bin/env python
import sys
import urllib2
import os


URL_TRACKER = "http://www.goear.com/tracker758.php?f="


def downlaod_mp3(url_mp3, name_song):
    print "Downloading song..."
    file = urllib2.urlopen(url_mp3)
    # Open our local file for writing
    with open(os.path.basename(name_song + ".mp3"), "wb") as local_file:
        local_file.write(file.read())


def parser(code, parameter):
    vector = code.split("/")
    return vector[parameter]


def get_url_mp3(id_song):
    url_source_mp3 = URL_TRACKER + id_song
    source = urllib2.urlopen(url_source_mp3).read()
    s = source.find('http://', 0)
    e = source.find('.mp3')
    return source[s:e] + ".mp3"


def get_url_song():
    if sys.argv[1] == "-d":
        print "Get url of song..."
        url_song = sys.argv[2]
        ind = 4
        return parser(url_song, ind)

    else:
        print 'Usage: python godown.py -d "name_song" | -h (show help)'


#Show help
def help():
    if sys.argv[1] == "-h":
        print 'Help: python godown.py -d "name_song"'

    else:
        print 'Usage: python godown.py -d "name_song" | -h (show help)'


#Get paramaters of cmd
if len(sys.argv) == 3:
    id_song = get_url_song()
    url_mp3 = get_url_mp3(id_song)
    name_song = raw_input("Insert name of song: ")
    downlaod_mp3(url_mp3, name_song)
    print "Download succesful !!!"

elif len(sys.argv) == 2:
    help()

else:
    print "Usage error"
