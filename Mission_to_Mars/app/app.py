from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
import scrape_mars
import pymongo
import mongo

app = Flask(__name__)

client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_facts


@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update(
        {},
        mars_data,
        upsert=True
    )
    return "Scraping Successful!"


if __name__ == "__main__":
    app.run()
