import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640',
             'lenta': 'https://lenta.ru/rss',
             'yandex': 'https://news.yandex.ru/index.rss',
             'sputnik': 'https://sputniknews.com/export/rss2/archive/index.xml',
             'tass': 'http://tass.ru/rss/v2.xml',
             }



@app.route("/")
@app.route("/<publication>")
def get_news(publication="lenta"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])

if __name__ == '__main__':
    app.run()
