#!/usr/bin/python3

# Logs Analysis Project - Report Generator
#
# The program you write in this project will run from the command line.
# It won't take any input from the user.
# Instead, it will connect to that database,
# use SQL queries to analyze the log data,
# and print out the answers to some questions:
#
# 1. What are the most popular three articles of all time?
# (Which articles have been accessed the most?)
# Example:
#    "Princess Shellfish Marries Prince Handsome" — 1201 views
#    "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
#    "Political Scandal Ends In Political Scandal" — 553 views
#
# 2. Who are the most popular article authors of all time?
# (That is, when you sum up all of the articles each author has written,
# which authors get the most page views?)
# Example:
#    Ursula La Multa — 2304 views
#    Rudolf von Treppenwitz — 1985 views
#    Anonymous Contributor — 1023 views
#
# 3. On which days did more than 1% of requests lead to errors?
# Example:
#    July 29, 2016 — 2.5% errors

import newsdata


# prints list of top-3 articles
def print_articles():

    top_list = newsdata.get_articles()
    for (title, views) in top_list:
        print("\t- \"" + title + "\" - " + str(views))


# prints list of authors, sorted by popularity
def print_authors():

    author_list = newsdata.get_authors()
    for (name, views) in author_list:
        print("\t- \"" + name + "\" - " + str(views))


# prints day, when more than 1% of requests lead to errors
def print_error_days():

    error_list = newsdata.get_error_days()
    for (date, all, errors) in error_list:
        if errors > (all*0.01):
            print("\t- " + convert_to_date(date) + " - " +
                  convert_to_percent(errors/all) + "% errors")


# converts errors/all ratio to decimal with precision set to 1.
def convert_to_percent(n):

    return format(n*100, '.1f')


# converts date object to readable string
def convert_to_date(date):

    result = date.strftime("%B %d, %Y")
    return result


# prints report in plain text
def generator():

    print("Report:")
    print("")
    print("What are the most popular three articles of all time?")
    print_articles()
    print("Who are the most popular article authors of all time?")
    print_authors()
    print("On which days did more than 1% of requests lead to errors?")
    print_error_days()


generator()
