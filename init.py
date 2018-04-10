#!/usr/bin/python3

# Logs Analysis Project - init.py
# This module creates views for newsdata methods.

import psycopg2


def create_views():
    pq = psycopg2.connect("dbname=news")
    c = pq.cursor()
    # create view for get_articles() method - top-3 most popular paths
    # (popularity is determined by the number of requests)
    c.execute("create view viewTop as\
              select path, count(id) as num\
              from log\
              where path like '/article/%' and status like '200 OK'\
              group by path\
              order by num DESC limit 3;")
    # create views for get_authors() method
    # viewArticles contains article paths and views (successful requests)
    c.execute("create view viewArticles as\
              select path, count(id) as num\
              from log\
              where path like '/article/%' and status like '200 OK'\
              group by path;")
    # viewAuthors contains article's author ids
    # and number of requests for article
    c.execute("create view viewAuthors as\
              select articles.author, viewArticles.num\
              from articles join viewArticles\
              on viewArticles.path like concat('%', articles.slug)\
              where viewArticles.path like concat('%', articles.slug)\
              order by viewArticles.num DESC;")
    pq.commit()
    pq.close()

create_views()
