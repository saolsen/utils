#!/usr/bin/python
# Logs Mtgox and Tradehill Ticker Data in couchdb for later.
# Quick and Dirty Hack! Just need to start getting this
# ticker data for later.

import time
import gevent
from gevent import monkey
import cryptotrade
import couchdb

monkey.patch_all()

def logMG(broker, db):
    ticker = broker.ticker()
    doc = {'MtGox': ticker}
    db[str(time.time())] = doc
    print "MtGox Ticker:\n"
    print doc

def logTH(broker, db):
    ticker = broker.ticker()
    doc = {'TradeHill': ticker}
    db[str(time.time())] = doc
    print "TradeHill Ticker:\n"
    print doc
    
def main():
    tradehill = cryptotrade.TradeHill()
    mtgox     = cryptotrade.MtGox()

    couch = couchdb.Server()
    db    = couch['tickers']
    
    while True:
        print "Logging Tickers"
        tickers = [ gevent.spawn(logTH, tradehill, db),
                    gevent.spawn(logMG, mtgox, db) ]
        gevent.joinall(tickers)
        time.sleep(30)

if __name__ == '__main__':
    main()
