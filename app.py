import flask
from flask import request
import requests
from bs4 import BeautifulSoup
from wiktionaryparser import WiktionaryParser

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/wikipedia', methods=['GET', 'POST'])
def wikipedia_scraper():
    term = request.args.get('term')
    response = requests.get(url=f"https://en.wikipedia.org/wiki/{term}",)
    soup = BeautifulSoup(response.content, 'html.parser')
    allp = soup.find(id="bodyContent").find_all("p")
    paragraph = allp[1].text
    return "<h1>%s<h1>" % paragraph

@app.route('/wiktionary', methods=['GET', 'POST'])
def wiktionary_scraper():
    term = request.args.get('term')
    parser = WiktionaryParser()
    word = parser.fetch(term)
    definition = word[0]['definitions']
    definition2 = definition[0]['text']
    definition3 = definition2[1:]
    return "<h1>%s</h1>" % definition3


app.run()