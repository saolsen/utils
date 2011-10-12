#!/usr/bin/env python
# hulu_movies.py
"""
Scrapes hulu for it's list of movies and then gets it's rating on imdb
"""

__author__="Stephen Olsen"

import urllib2
import urllib
import simplejson
from BeautifulSoup import BeautifulSoup

# Hulu's movie list
base_url = 'http://www.hulu.com/browse/movies'

def get_rating(title):
    """
    Gets the rating of a movie with the IMDB api
    """
    # If the movie isn't found through the API or
    # it can't be converted to ASCII just return -1
    imdb_api = 'http://www.imdbapi.com/'
    try:
        ascii_title = title.encode('ASCII')
        request  = imdb_api + '?' + urllib.urlencode(dict(t=ascii_title))
        movie  = urllib2.urlopen(request).read()
        rating = simplejson.loads(movie)['Rating']
    except:
        rating = '-1'
    return rating

# Used for sorting later
def _key(tple):
    try:
        key = float(tple[1])
    except:
        key = -1
    return key

def main():
    # Get a list of all the movies on hulu
    page   = urllib2.urlopen(base_url).read()
    tree   = BeautifulSoup(page)
    div    = tree.find(id='show_list_hiden')
    links  = div.findChildren()
    titles = map(lambda x: x.text, links)

    # Get their rating and sort by it
    movies = map(lambda x: (x,get_rating(x)), titles)
    ranked = sorted(movies, key=_key, reverse=True)

    # Print them out nicely
    f = open('./hulu_movies', 'w')
    for movie in ranked:
        f.write(movie[1] + '\t' + movie[0] + '\n')
    f.close()

if __name__ == '__main__':
    main()
