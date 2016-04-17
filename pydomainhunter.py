import urllib2
import sys
import re
import time
import httplib
import random


HEADERS = [
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android4.2.2; zh-tw;WIZ T-218) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30;',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0'

]


def curldom(domain):
    foundsubdomains = []
    num = 1

    while True:
        try:
                request = urllib2.Request("http://www.bing.com/search?q=site%3A" + domain + "&first=" + str(num))
                request.add_header('User-Agent', HEADERS[ random.randint( 1 , len( HEADERS ) ) - 1  ] )
                opener = urllib2.build_opener()
                feeddata = opener.open(request).read()
                links =  feeddata.split("<a href=")
                for i in links:
                    if "."+domain in i:
                        pagematches = i.split('"')
                        possiblesubdomain = pagematches[1:2:][0].split("." + domain+ "/")[0]
                        if possiblesubdomain not in foundsubdomains:
                            print possiblesubdomain
                            foundsubdomains.append(possiblesubdomain)

                
                time.sleep(2)
                num+=10
        except httplib.IncompleteRead:
                print "Incomplete Read. Let me Try again"
                num-=10


if __name__ == '__main__':
    
    try:
        print "*"*80
        print "\n TinMyoWin's subdomain scanner is working"
        print "*"*80
        domain = sys.argv[1]
        curldom(domain)
        
    except IndexError:
        print "Usage:"
        print "\tpython pydomainhunter.py <domain>"
        print "Example:"
        print "\tpython subdomainer.py google.com"
        print "\tpython subdomainer.py bing.com"
