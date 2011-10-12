#!/usr/bin/env python
# nutritionalData.py
"""
Takes ashley w's json dump of the The U.S. Department of Agriculture's
food nutrition data database and dumps it into a couchDB database.
http://ashleyw.co.uk/project/food-nutrient-database

To run the script as is, download the dump, drop it in the same folder
and fill in the couchdb info.
"""

__author__= "Stephen Olsen"

import simplejson
import couchdbkit

# CouchDB Info
couch_server = "server address"
couch_db     = "nutrition"
filename     = "foods-2011-10-03.json"

def main():
    srv = couchdbkit.Server(couch_server)
    db  = srv[couch_db]
    
    f = open(filename, 'r')

    json = simplejson.loads(f.readline())
    amount = len(json)
    x = 1

    for item in json:
        print item['description'] + '\t\t' + str(x) + '/' + str(amount)
        x += 1
        db[str(item['id'])] = item
        

if __name__ == '__main__':
    main()
