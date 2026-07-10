# Manufacturing Analytics Platform

A modular analytics platform for transforming manufacturing test data into actionable production insights through SQL, Python, KPI engineering, and automated reporting.

---

## Overview

Manufacturing Analytics Platform is a Python-based analytics framework designed to process manufacturing test data and generate production KPIs, yield metrics, failure analysis, and executive reports.

The platform integrates SQL-based data extraction with automated KPI calculations, visualization, and reporting workflows to support manufacturing engineering and production decision-making.

Rather than focusing on a single product line, the platform provides a reusable architecture applicable across multiple manufacturing environments.

---

## Key Features

- SQL data extraction
- Manufacturing KPI calculation
- First Pass Yield (FPY)
- Second Test Yield (STY)
- Failure Rate (FR%) monitoring
- Station performance analysis
- Product performance comparison
- Trend analysis
- Automated report generation
- Dashboard data preparation
- CSV / Excel export
- Modular analytics architecture

---

## Technology Stack

- Python
- SQL
- MySQL
- Pandas
- NumPy
- Matplotlib
- SQLAlchemy
- ETL
- Manufacturing Analytics
- Business Intelligence

---

## Project Architecture

SQL Database
        │
        ▼
SQL Loader
        │
        ▼
Data Cleaning
        │
        ▼
Product & Station Mapping
        │
        ▼
KPI Engine
        │
        ▼
Analytics Modules
        │
        ▼
Visualization
        │
        ▼
Automated Reports
        │
        ▼
Dashboard Export

---

## Current Capabilities

- SQL-based production data extraction
- Manufacturing KPI calculation
- Yield analytics
- Failure rate monitoring
- Product comparison
- Station performance analysis
- Automated reporting pipeline
- Dashboard-ready outputs
- Modular analytics workflow

---

## Repository Structure

src/
    calculators/
        yield_metrics.py
        failure_rate.py
        station_metrics.py

    utils/
        product_mapper.py
        station_mapper.py
        date_utils.py

    pipeline.py
    sql_loader.py
    kpi_engine.py
    report_builder.py
    visualization.py
    dashboard_export.py

docs/
sample_data/
sample_output/

---

## Future Improvements

- Statistical Process Control (SPC)
- Predictive quality analytics
- Interactive dashboards
- REST API
- Machine learning anomaly detection
- Manufacturing trend forecasting
- Docker deployment

---

## Author

**Eugen Rovner**

Data Analyst | Manufacturing Analytics | Python | SQL | Business Intelligence
