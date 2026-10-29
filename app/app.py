"""Flask web app that embeds the Tableau dashboard + story and serves KPI JSON."""
import os
import sqlite3
from pathlib import Path
from flask import Flask, render_template, jsonify

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "ev_market.db"

app = Flask(__name__)
# Paste your Tableau Public URLs here or set them as environment variables.
app.config["DASHBOARD_URL"] = os.getenv(
    "TABLEAU_DASHBOARD_URL", "https://public.tableau.com/views/YOUR_WORKBOOK/EVMarketDashboard")
app.config["STORY_URL"] = os.getenv(
    "TABLEAU_STORY_URL", "https://public.tableau.com/views/YOUR_WORKBOOK/EVMarketStory")


def query(sql, args=()):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    rows = [dict(r) for r in con.execute(sql, args)]
    con.close()
    return rows


def kpis():
    r = query("""SELECT SUM(annual_sales) AS units, ROUND(AVG(driving_range_km)) AS rng,
                        ROUND(AVG(customer_rating),2) AS rating,
                        COUNT(DISTINCT manufacturer) AS makers
                 FROM ev_sales WHERE sales_year = 2024""")[0]
    top = query("""SELECT manufacturer FROM ev_sales WHERE sales_year=2024
                   GROUP BY manufacturer ORDER BY SUM(annual_sales) DESC LIMIT 1""")[0]["manufacturer"]
    return {**r, "top_maker": top}


@app.route("/")
def home():
    return render_template("index.html", k=kpis(), page="home")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", url=app.config["DASHBOARD_URL"], page="dashboard")


@app.route("/story")
def story():
    return render_template("story.html", url=app.config["STORY_URL"], page="story")


@app.route("/personas")
def personas():
    return render_template("personas.html", page="personas")


@app.route("/api/kpis")
def api_kpis():
    return jsonify(kpis())


@app.route("/api/category-sales")
def api_category_sales():
    return jsonify(query("""SELECT category, SUM(annual_sales) AS units FROM ev_sales
                            WHERE sales_year=2024 GROUP BY category ORDER BY units DESC"""))


if __name__ == "__main__":
    app.run(debug=True)
