#!/usr/bin/env python
"""Produce reports from web server."""

#
# log_analysis.py -- implementation of Logs Analysis Project
#

import psycopg2
import sys

DBNAME = "news"


def connect(query, func):
    """Connect to database, handle errors and if none, return results."""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        posts = c.fetchall()
        if func == 'one_percent_error_loads':
            for p in posts:
                print '%s - %d errors' % (p[0], p[1])
        else:
            for p in posts:
                print '%s - %d views' % (p[0], p[1])
    except psycopg2.DatabaseError, exception:
        print exception
        sys.exit(1)
    finally:
        if db:
            db.close()


def most_popular_articles():
    """Select the 3 most popular articles of all time."""
    print '1. The most popular articles are...'
    return ("""SELECT articles.title, COUNT(*) as num FROM articles, log"""
            """ WHERE SUBSTRING (log.path FROM 10) = articles.slug and"""
            """ log.path != '/' Group By articles.title ORDER By num"""
            """ DESC LIMIT 3;""")


def most_popular_authors():
    """Select the most popular authors of all time."""
    print '2. The most popular authors are...'
    return ("""SELECT authors.name, count(*) as num from"""
            """ authors, articles, log WHERE SUBSTRING (log.path FROM 10)"""
            """ = articles.slug and articles.author = authors.id and"""
            """ log.path != '/' Group By authors.name ORDER by num"""
            """ DESC LIMIT 20;""")


def one_percent_error_loads():
    """Select the days where there are >= 1% error load."""
    print '3. The days where there are more than  1% load error are'
    return ("""SELECT gday, ((err::decimal / allc::decimal) * 100) as perc"""
            """ FROM (select date(time) as gday, count(status) as allc, """
            """ count(CASE WHEN status = '200 OK' THEN 1 END) AS ok,"""
            """ count(CASE WHEN status = '404 NOT FOUND' THEN 1 END) AS err """
            """ FROM log GROUP BY gday) as errreq;""")


if __name__ == '__main__':
    connect(most_popular_articles(), most_popular_articles.__name__)
    connect(most_popular_authors(), most_popular_authors.__name__)
    connect(one_percent_error_loads(), one_percent_error_loads.__name__)
