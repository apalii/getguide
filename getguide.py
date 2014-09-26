#!/usr/bin/env python

import re
import urllib2 as u
import sys

'''
*Not complete.
This simple program is designed to find all available links on guides:
 
http://portaone.com/resources/docs/PortaSIP/m-r-32/PortaSIP_Switching_Server_MR32.pdf
http://portaone.com/resources/docs/PortaSIP/m-r-32/PortaSIP_Media_Server_MR32.pdf
 
For single release or even for needed range.
'''
links = []
urls = ['http://portaone.com/support/documentation/old/', 'http://portaone.com/support/documentation/']
 
def url_grep() :  
    '''This function will fill the list "links" with direct links on guides. '''
    for page in urls :
        html = u.urlopen(page)
        for i in html:
            if re.search('^\s+<a\s+href=',i):
                i = i.strip()
                x = re.findall('(\/resources\/docs\S+pdf)', i)
                links.append(''.join(x))
 
def link_grep_range(first,last):  
    url_grep()
    gen = ['MR' + str(i) for i in xrange(int(first[2:]), int(last[2:]) + 1)]
    for pattern in gen:
        for i in links :
            if re.search(pattern,i):
                print 'http://portaone.com' + i
 
def url_grep_single(mr) :
    url_grep()
    for i in links :
        if re.search(mr.upper(),i):
            print 'http://portaone.com' + i
 
if __name__ == "__main__":
    if sys.argv.__len__() == 1 or sys.argv.__len__() > 3:
        print "\nExamples :\n$ python guide.py mr35\n$ python guide.py mr35 mr40\n\nTry again!"
        exit()
    elif sys.argv.__len__() == 2:
        url_grep_single(sys.argv[1])
    elif sys.argv.__len__() == 3:
        link_grep_range(sys.argv[1], sys.argv[2])
