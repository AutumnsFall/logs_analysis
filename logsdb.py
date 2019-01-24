import psycopg2
from config import *

def get_three_popular_articles():
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	c.execute("select title, total from articles, (select path, count(*) as total from log group by path) as paths where path LIKE '%' || slug order by total desc limit 3;")
	articles = c.fetchall()
	db.close()
	return articles	

def get_most_popular_article_author():
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	c.execute("select authors.name, sum(total) as views from articles, authors, (select path, count(*) as total from log group by path) as paths where path LIKE '%' || slug and articles.author=authors.id group by authors.name order by views desc;")
	authors = c.fetchall()
	db.close()
	return authors	

def get_error_leads():
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	c.execute("select date, (error*1.0/total*1.0)*100.00 as percentage from (select TO_CHAR(time, 'dd-Mon-YYYY') as date, count(*) as error from log where status LIKE '404%' group by date) as X, (select count(*) as total from log) as Y where (error*1.0/total*1.0)*100.00 >1.00 order by percentage desc; ")
	dateWithError = c.fetchall()
	db.close()
	return dateWithError
	

