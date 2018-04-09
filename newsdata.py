#!/usr/bin/python3

# Logs Analysis Project - newsdata.py
#
# This module provides methods for generating reports.
# Methods:
# - get_articles()
# - get_authors()
# - get_error_days()

import psycopg2


def get_articles():
    """
    TOP-3 of the most popular articles
    Returns list of tuples. Every tuple contains title and number of views.
    List is sorted by number of views.
    Example:
      >>> print(get_articles())
      [("First Article", 730),("Second Article", 543), ("Third Article", 173)]
    """
    pq = psycopg2.connect("dbname=news")
    c = pq.cursor()
    c.execute("create view viewTop as\
      select path, count(id) as num\
      from log\
      where path like '/article/%' and status like '200 OK'\
      group by path\
      order by num DESC limit 3;")
    c.execute("select articles.title, viewTop.num\
      from articles join viewTop\
      on viewTop.path like concat('%', articles.slug)\
      where viewTop.path like concat('%', articles.slug)\
      order by viewTop.num DESC;")
    results = c.fetchall()
    c.execute("drop view viewTop;")
    pq.close()
    return results


def get_authors():
    """
    Popular authors of all times
    Returns list of tuples. Every tuple contains author and number of views.
    Number of views is a sum of views of all author's articles.
    List contains all authors. List is sorted by number of views.
    Example:
      >>> print(get_authors())
      [("John Smith", 932),("Anna Reed", 765), ("Jack Brown", 456)...]
    """
    pq = psycopg2.connect("dbname=news")
    c = pq.cursor()
    c.execute("create view viewTop as\
      select path, count(id) as num\
      from log\
      where path like '/article/%' and status like '200 OK'\
      group by path;")
    c.execute("create view viewAuthors as\
      select articles.author, viewTop.num\
      from articles join viewTop\
      on viewTop.path like concat('%', articles.slug)\
      where viewTop.path like concat('%', articles.slug)\
      order by viewTop.num DESC;")
    c.execute("select authors.name, sum(viewAuthors.num) as views\
        from authors join viewAuthors\
        on authors.id = viewAuthors.author\
        group by authors.name\
        order by views DESC;")
    results = c.fetchall()
    c.execute("drop view viewAuthors;")
    c.execute("drop view viewTop;")
    pq.close()
    return results


def get_error_days():
    """
    Days when more that 1 percent of requests lead to errors
    Returns list of tuples.
    Every tuple contains date, number of requests and number of errors.
    Number of requests is a number of all requests during the day.
    Number of errors is a number of all request lead to errors (not '200 OK')
    List contains all days. List is sorted by date.
    Example:
      >>> print(get_error_days())
      [(2016-07-01, 932, 1),(2016-07-02, 1225, 56),(2016-07-03, 342, 12)...]
    """
    pq = psycopg2.connect("dbname=news")
    c = pq.cursor()
    c.execute("select time::date,\
            count(*) total,\
            sum(case when status!='200 OK' then 1 else 0 end) Errors\
        from log\
        group by time::date\
        order by time::date;")
    results = c.fetchall()
    pq.close()
    return results
