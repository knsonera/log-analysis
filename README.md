# Logs Analysis Project

The program can be run from the command line.
It connects to that database, uses SQL queries to analyze the log data,
and prints out the answers to these questions:

1. What are the most popular three articles of all time?
(Which articles have been accessed the most?)
```
  - "Princess Shellfish Marries Prince Handsome" — 1201 views
  - "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
  - "Political Scandal Ends In Political Scandal" — 553 views
```

2. Who are the most popular article authors of all time?
(That is, when you sum up all of the articles each author has written,
which authors get the most page views?)
```
  - Ursula La Multa — 2304 views
  - Rudolf von Treppenwitz — 1985 views
  - Anonymous Contributor — 1023 views
```

3. On which days did more than 1% of requests lead to errors?
```
  - July 29, 2016 — 2.5% errors
```
## What's inside:
- View Initialization File - init.py
- Database parser - newsdata.py
- Report Generator - report_generator.py

## What's under the hood
### init.py
This module creates views for get_articles() and get_authors()
**WARNING: Run this module ONCE before generating report!**
### newsdata.py
This module provides methods for generating reports.
Methods:
- **get_articles()**
Returns list of tuples.
List contains only three tuples. Every tuple contains article's title and
number of views (a number of successful requests of the article's path).
Example:
```
>>> print(get_articles())
[("First Article", 730),("Second Article", 543), ("Third Article", 173)]
```

- **get_authors()**
Returns list of tuples.
Every tuple contains author name and sum of successful requests of
all author's articles.
List is sorted by views in descending order.
Example:
```
>>> print(get_authors())
[("John Smith", 932),("Anna Reed", 765), ("Jack Brown", 456)...]
```

- **get_error_days()**
Returns list of tuples.
Every tuple contains date, number of requests and number of errors.
Number of requests is a number of all requests during the day.
Number of errors is a number of all unsuccessful errors during the day.
List is sorted by date in ascending order.
Example:
```
>>> print(get_error_days())
[(2016-07-01, 932, 1),(2016-07-02, 1225, 56),(2016-07-03, 342, 12)...]
```

### report_generator.py
This module generates reports using data from news database.

## Before you start
To prepare for generating reports, please run init.py module **ONCE**:
```
python3 init.py
```
Once views are created, you don't need to create them again!

## Try me!
To generate report run report_generator.py from the command line
```
python3 report_generator.py
```
