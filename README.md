<div align="center">

# ⚡ EV Market Analytics

### Electric Vehicle Market Intelligence · Tableau · SQL · Flask

An end-to-end analytics project for exploring electric vehicle sales, market segments, battery technologies, manufacturing regions, and customer ratings.

[Project Overview](#project-overview) · [Features](#key-questions) · [Getting Started](#getting-started) · [Dataset](#dataset) · [Tableau](#tableau-workbook)

</div>

---

## Project Overview

**EV Market Analytics** brings together a sample electric-vehicle dataset, a SQL data workflow, Tableau visual analytics, and a Flask web application. The project demonstrates how raw market data can be transformed into structured analysis and presented through interactive dashboards.

### Business Problem

Market strategy teams, business intelligence analysts, and sustainable-mobility researchers need a clearer view of:

- Which vehicle categories contribute most to sales?
- Which manufacturers lead the market?
- How do battery technologies compare?
- Where are vehicles manufactured?
- How do technical specifications and customer ratings vary across segments?

### Intended Audiences

| Audience | Example questions |
| --- | --- |
| **EV Market Strategy Director** | Which categories lead sales? Which segments may be growing? How does satisfaction vary by segment? |
| **Automotive BI Manager** | How are sales distributed by manufacturer, battery type, and manufacturing country? |
| **Sustainable Mobility Researcher** | How do battery types, driving range, and production regions compare? |

## Key Questions

The analysis is designed to explore the following dimensions:

- **Sales performance:** annual sales by year, region, manufacturer, and vehicle category
- **Competitive landscape:** manufacturer comparisons and market distribution
- **Battery technology:** battery-type mix and technical specifications
- **Vehicle specifications:** battery capacity, driving range, charging time, and price
- **Customer experience:** ratings across manufacturers and vehicle categories
- **Manufacturing footprint:** production countries represented in the dataset

## Technology Stack

| Area | Tools |
| --- | --- |
| Data preparation | Python, pandas |
| Data storage | SQLite |
| Data analysis | SQL |
| Visualization | Tableau Desktop / Tableau Public |
| Web application | Flask, HTML, CSS |

The database layer is intended to be adaptable to MySQL or PostgreSQL with the appropriate connection and schema changes.

## Repository Structure

```text
├── app/
│   ├── app.py                   # Flask application
│   ├── templates/               # HTML templates
│   └── static/                  # Static assets (CSS, etc.)
├── data/
│   ├── ev_market_data.csv       # Sample dataset
│   └── ev_market.db             # Generated SQLite database
├── scripts/
│   ├── generate_dataset.py      # Generate sample data
│   ├── load_to_db.py             # Load data into the database
│   └── run_queries.py            # Run analysis queries
├── sql/
│   ├── schema.sql
│   ├── views.sql
│   └── analysis_queries.sql
├── tableau/
│   ├── Nitya Pandya.twbx         # Packaged Tableau workbook
│   ├── dashboard_design.md
│   ├── calculated_fields.md
│   └── story_scenes.md
├── docs/
│   ├── project_documentation.md
│   ├── performance_testing.md
│   └── demo_video_script.md
└── requirements.txt
```

> The tree above describes the intended project layout. File names may vary slightly depending on what is included in your repository.

## Getting Started

### Prerequisites

- Python 3.9 or later (use the version supported by your dependencies)
- Git
- A Tableau account for publishing to Tableau Public
- Tableau Desktop is needed to open and publish the packaged `.twbx` workbook using the workflow described below

### 1. Clone the repository

Replace `<your-username>` with your GitHub username and update the repository URL if yours differs.

```bash
git clone https://github.com/<your-username>/ev-market-analytics-tableau.git
cd ev-market-analytics-tableau
```

### 2. Create a virtual environment

**Windows (PowerShell)**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the dataset and database

Run these commands from the repository root:

```bash
python scripts/generate_dataset.py
python scripts/load_to_db.py
```

The dataset-generation step is optional if you already have the intended CSV file and do not want to regenerate it. The database-loading script creates or refreshes the SQLite database, depending on how the script is implemented.

### 5. Run the SQL analysis

```bash
python scripts/run_queries.py
```

The project documentation describes 11 analysis queries and 2 SQL views.

### 6. Start the Flask application

```bash
python app/app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Dataset

**File:** `data/ev_market_data.csv`  
**Size:** 1,488 rows  
**Period:** 2019–2024  
**Data type:** Synthetic sample data

The sample data is generated by `scripts/generate_dataset.py` and is intended for demonstrating the workflow. It is not a verified source of real-world EV market statistics. The generator uses modeled relationships between vehicle attributes, such as battery capacity and driving range.

### Data Dictionary

| Column | Description |
| --- | --- |
| `sales_year` | Year of sale |
| `sales_region` | Sales region |
| `manufacturer` | Vehicle manufacturer |
| `model` | Vehicle model |
| `category` | Vehicle category, such as hatchback, sedan, SUV, bus, truck, or two-wheeler |
| `battery_type` | Battery technology, such as LFP, NMC, NCA, sodium-ion, or solid-state |
| `battery_capacity_kwh` | Battery capacity in kilowatt-hours |
| `driving_range_km` | Driving range in kilometres |
| `fast_charge_minutes` | Fast-charging time in minutes |
| `price_usd` | Average price in US dollars |
| `manufacturing_country` | Country of manufacture represented in the dataset |
| `annual_sales` | Annual units sold |
| `customer_rating` | Customer rating on a 1–5 scale |

To use a real dataset, replace the sample CSV with a compatible source and verify that the column names and data types match the project’s scripts and SQL schema.

## Tableau Workbook

The repository documentation identifies the packaged workbook as:

`tableau/Nitya Pandya.twbx`

A `.twbx` file packages a Tableau workbook with supporting resources, which may include an embedded data extract. GitHub can store the file, but it does not render Tableau dashboards interactively in the repository preview.

### Connect and Publish

1. Open the packaged workbook in Tableau Desktop.
2. If you need to connect to the project database separately, use the CSV file or configure an appropriate SQLite connection. Connector and driver availability can vary by operating system and Tableau version.
3. Use the project guides to configure the intended visuals and story:
   - [`tableau/dashboard_design.md`](tableau/dashboard_design.md)
   - [`tableau/calculated_fields.md`](tableau/calculated_fields.md)
   - [`tableau/story_scenes.md`](tableau/story_scenes.md)
4. Publish the workbook to Tableau Public using your Tableau account.
5. Copy the published dashboard and story URLs if you want to embed them in the Flask application.

### Configure Tableau URLs for Flask

Set the environment variables to the URLs of your **published** Tableau views.

**macOS / Linux**

```bash
export TABLEAU_DASHBOARD_URL="https://public.tableau.com/views/<workbook>/<dashboard>"
export TABLEAU_STORY_URL="https://public.tableau.com/views/<workbook>/<story>"
python app/app.py
```

**Windows PowerShell**

```powershell
$env:TABLEAU_DASHBOARD_URL = "https://public.tableau.com/views/<workbook>/<dashboard>"
$env:TABLEAU_STORY_URL = "https://public.tableau.com/views/<workbook>/<story>"
python app/app.py
```

Replace the placeholders with your actual published URLs. The Flask app must be implemented to read these environment variables for the configuration to take effect.

## Project Status

The checklist below reflects the status recorded in the original project README. Update it as the implementation progresses.

- [x] Problem definition and audience personas
- [x] Data generation and database-loading workflow
- [x] SQL analysis (11 queries and 2 views)
- [ ] Tableau connection and data preparation
- [ ] 12+ visualizations, dashboard, and five-scene story
- [x] Performance testing plan — [`docs/performance_testing.md`](docs/performance_testing.md)
- [x] Flask web integration — [`docs/project_documentation.md`](docs/project_documentation.md)
- [ ] Demo video — [`docs/demo_video_script.md`](docs/demo_video_script.md)
- [x] Project documentation — [`docs/project_documentation.md`](docs/project_documentation.md)

## Documentation

- [Project documentation](docs/project_documentation.md)
- [Performance testing plan](docs/performance_testing.md)
- [Demo video script](docs/demo_video_script.md)
- [Dashboard design guide](tableau/dashboard_design.md)
- [Calculated fields guide](tableau/calculated_fields.md)
- [Tableau story scenes](tableau/story_scenes.md)

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for the full license text if included in the repository.

---

<div align="center">

**EV Market Analytics** · Turning sample EV data into structured insights

</div>
