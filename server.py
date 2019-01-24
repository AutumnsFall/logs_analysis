from flask import Flask
from logsdb import get_three_popular_articles, get_most_popular_article_author, get_error_leads
from index import *

app = Flask(__name__)

@app.route('/', methods=['GET'])

def main():
	articleResults = get_three_popular_articles()
	if not articleResults:
		articles = EMPTY_RETURN
	else:
		articles = "".join(ARTICLES_ROW % ( title, views) for title, views in articleResults)

	authorResults = get_most_popular_article_author()
	if not authorResults:
		authors = EMPTY_RETURN	
	else:
		authors = "".join(AUTHORS_ROW % (author, views) for author, views in authorResults)

	dateWithError = get_error_leads()
	if not dateWithError:
		dateError = EMPTY_RETURN
	else:
		dateError = "".join(ERRORS_ROW % (date, percentage) for date, percentage in dateWithError)

	html = HTML_WRAP % (articles, authors, dateError)
	
	return html

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8000)	
	
