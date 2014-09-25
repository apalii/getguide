#!/usr/bin/env python

import re
import urllib2 as u
import sys
 
'''
Please specify 'MR' version as a first parameter"
For example :
 
$ python guide.py mr35
'''
def url_grep(mr) :
    urls = {'http://portaone.com/support/documentation/old/', 'http://portaone.com/support/documentation/'}
    links = []
    for page in urls :
        html = u.urlopen(page)
        for i in html:
            if re.search('^\s+<a\s+href=',i):
                i = i.strip()
                x = re.findall('(\/resources\/docs\S+pdf)', i)
                links.append(''.join(x))
        root = 'http://portaone.com'
        for i in links :
            if re.search(mr.upper(),i):
                print 'http://portaone.com' + i
 
if __name__ == "__main__": url_grep(sys.argv[1])
