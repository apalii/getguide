#!/usr/bin/env python

import re
import urllib2 as u
import sys

'''
*Not complete.
version = 3
 
This simple program is designed to find all available links on guides:
 
http://portaone.com/resources/docs/PortaSIP/m-r-32/PortaSIP_Switching_Server_MR32.pdf
http://portaone.com/resources/docs/PortaSIP/m-r-32/PortaSIP_Media_Server_MR32.pdf
 
For one release or even for needed range.
"grep -i <pattern>" - included since v3 !
'''
 
links = []
links2 = []
urls = ['http://portaone.com/support/documentation/old/', 'http://portaone.com/support/documentation/']
 
def url_grep() :  
    '''This function will fill the list "links" with direct links on guides. '''
    global links
    for page in urls :
        html = u.urlopen(page)
        for i in html:
            if re.search('^\s+<a\s+href=',i):
                i = i.strip()
                x = re.findall('(\/resources\/docs\S+pdf)', i)
                links.append(''.join(x))
 
def grep_i(guide):
    ''' this is an analog of the grep -i'''
    global links
    for i in links :
        if re.search(guide, i, re.IGNORECASE):
            links2.append(i)
 
def find_one(mr,list=links) :
    for i in list :
        if re.search(mr.upper(),i):
            print 'http://portaone.com' + i
 
def find_range(first,last,list=links):  
    gen = ['MR' + str(i) for i in xrange(int(first), int(last) + 1)]
    for pattern in gen:
        for i in list :
            if re.search(pattern,i):
                print 'http://portaone.com' + i
 
if __name__ == "__main__":
    if sys.argv.__len__() == 1 or sys.argv.__len__() > 4:
        print "\nHow to use :\ngetguide.py  <int>   <  <int>      <str>"
        print "getguide.py <from MR> <to MR> <grep pattern>"
        print "\nExamples :\n~$ python getguide.py 35\t - all possible guides for one release."
        print "~$ python getguide.py 35 bill\t - the same as ~$ python getguide.py 35 bill | grep -i bill"
        print "~$ python getguide.py 35 40\t - all possible guides for range of releases(from 35 to 40)"
        print "~$ python getguide.py 35 40 int\t - equivalent to ~$ python getguide.py 35 40 | grep -i int\n\nTry again!"
        exit(0)
 
    elif sys.argv.__len__() == 2:
        url_grep()
        find_one(sys.argv[1])
               
    elif sys.argv.__len__() == 3:
        if sys.argv[2].isdigit() :
            if int(sys.argv[1]) > int(sys.argv[2]):
                print '\nFirst parameter should be less than second parameter !\n', sys.argv[1], '<', sys.argv[2], 'really ???\n'
                exit(0)
            else :
                url_grep()
                find_range(sys.argv[1], sys.argv[2])
        else :
            url_grep()
            grep_i(sys.argv[2])
            find_one(sys.argv[1],links2)
 
    elif sys.argv.__len__() == 4:
        if int(sys.argv[1]) > int(sys.argv[2]):
            print '\nFirst parameter should be less than second parameter !\n', sys.argv[1], '<', sys.argv[2], 'really ???\n'
            exit(0)
        else:
            url_grep()
            grep_i(sys.argv[3])
            find_range(sys.argv[1], sys.argv[2],links2)