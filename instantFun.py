# Downloads all the buttons from instantsfun as mp3 files

import httplib2
import re
import os
from sets import Set

url_prefix = 'http://www.instantsfun.es/'
get_all = 'instants/all'

# Get page source
h = httplib2.Http()
resp, content = h.request(url_prefix + get_all)

# Parse out url's for buttons
pattern = '("/)([[/A-z0-9%]*)(.swf)(")'
results = re.findall(pattern, content)
urls = map ((lambda x: x[1] + x[2]), results)
urls = list(Set(urls))

for url in urls:
    print url
    #os.system("wget " + url_prefix + url)

f = os.popen("ls")
for i in f.readlines():
    i = i.strip()
    if ".swf" in i:
        name = i[:-4]
        flasm = ("flasm -x " + i)
        #print flasm
        os.system(flasm)
        mplayer = ("mplayer -dumpaudio " + i + " -dumpfile " + name + ".mp3")
        #print mplayer
        os.system(mplayer)
