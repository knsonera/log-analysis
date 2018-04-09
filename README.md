# Logs Analysis Project

The program you write in this project will run from the command line.
It won't take any input from the user.
Instead, it will connect to that database, use SQL queries to analyze the log data,
and print out the answers to these questions:

1. What are the most popular three articles of all time?
(Which articles have been accessed the most?)
**Example:**
```
  - "Princess Shellfish Marries Prince Handsome" — 1201 views
  - "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
  - "Political Scandal Ends In Political Scandal" — 553 views
```

2. Who are the most popular article authors of all time?
(That is, when you sum up all of the articles each author has written,
which authors get the most page views?)
**Example:**
```
  - Ursula La Multa — 2304 views
  - Rudolf von Treppenwitz — 1985 views
  - Anonymous Contributor — 1023 views
```

3. On which days did more than 1% of requests lead to errors?
**Example:**
```
  - July 29, 2016 — 2.5% errors
```
## What's inside:
- Database parser - newsdata.py
- Report Generator - report_generator.py

## What's under the hood
###newsdata.py###
This module provides methods for generating reports.
Methods:
- **get_articles()**
Connects to the database and creates view of log table.
View contains TOP-3 paths and number of views (successful requests for path).
Then it matches path with article title in articles table.
Then it drops the view.
Returns list of tuples. Every tuple contains title and number of views.
Example:
```
>>> print(get_articles())
[("First Article", 730),("Second Article", 543), ("Third Article", 173)]
```

- **get_authors()**
Connects to the database and creates two views.
First view cointains data from 'log' table.
It contains TOP-3 paths and number of views (successful requests for path).
Second view contains data from articles and log tables
It matches author ids with articles and number of views.
Then it matches author ids with author names from authors table.
Then it drops all the views.
Returns list of tuples.
Every tuple contains author name and sum of views of author's articles.
Example:
```
>>> print(get_authors())
[("John Smith", 932),("Anna Reed", 765), ("Jack Brown", 456)...]
```

- **get_error_days()**
Returns list of tuples.
Every tuple contains date, number of requests and number of errors.
Number of requests is a number of all requests during the day.
Number of errors is a number of all request lead to errors (not '200 OK')
List contains all days. List is sorted by date.
Example:
```
>>> print(get_error_days())
[(2016-07-01, 932, 1),(2016-07-02, 1225, 56),(2016-07-03, 342, 12)...]
```

###report_generator.py###
This module generates reports using data from news database.



## Try me!
To generate report run report_generator.py from the command line
```
python3 report_generator.py
```
