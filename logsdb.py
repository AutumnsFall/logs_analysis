#!/usr/bin/env python3
import psycopg2
from config import *


def connect(database_name=DBNAME):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except psycopg2.DatabaseError as e:
        print(e)


def get_three_popular_articles():
    db, c = connect()
    c.execute("select title, total from articles, " +
              "(select path, count(*) as total from log group by path) " +
              "as paths where path LIKE '%' || slug order by total desc " +
              "limit 3;")
    articles = c.fetchall()
    db.close()
    return articles


def get_most_popular_article_author():
    db, c = connect()
    c.execute("select authors.name, sum(total) as views from articles," +
              " authors, (select path, count(*) as total " +
              " from log group by path) as paths where " +
              "path LIKE '%' || slug and articles.author=authors.id " +
              " group by authors.name order by views desc;")
    authors = c.fetchall()
    db.close()
    return authors


def get_error_leads():
    db, c = connect()
    c.execute(
        "select date1, (perDayError*1.0/totalError*1.0)*100.00" +
        " as percentage from (select TO_CHAR(time, 'dd-Mon-YYYY')" +
        " as date1, count(*) as perDayError from log where status" +
        " LIKE '404%' group by date1) as X, (select TO_CHAR(time," +
        " 'dd-Mon-YYYY') as date2, count(*) as totalError from" +
        " log group by date2) as Y where date1 = date2 and " +
        "(perDayError*1.0/totalError*1.0)*100.00 > 1.00 order by percentage; ")
    dateWithError = c.fetchall()
    db.close()
    return dateWithError
