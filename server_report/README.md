# Server Infrastructure Report

## Overview

A Python script that reads server inventory data from a CSV file and generates a simple infrastructure report.

The project was created to practise working with operational data, CSV imports, dictionaries, date handling, configuration files, and reusable reporting functions.

The script simulates a common infrastructure task: taking server inventory data and producing useful operational summaries.

## Features

The report includes:

* Total number of servers
* Server count grouped by environment
* Server count grouped by operating system
* Servers requiring patching based on a configurable age threshold
* Average memory allocation across servers

## Example Output

```
Infrastructure Report
=====================

Total servers: 3

By environment:
prod: 2
test: 1

By operating system:
Windows Server 2022: 1
Ubuntu 24.04: 1
Windows Server 2019: 1

Servers requiring patching:
server02: patch date: 2026-06-10 Last Patched 46 days ago
server03: patch date: 2025-12-01 Last Patched 237 days ago

Average memory:
21.33GB
```

## Project Structure

```
server_report/
│
├── report.py
├── config.py
└── servers_example.csv
```

## Configuration

Settings such as the CSV file location and patching threshold are stored separately in `config.py`.

Example:

```python
PATCH_DAYS = 30
CSV_PATH = "servers_example.csv"
```

This allows operational settings to be changed without modifying the reporting logic.

## Running the Script

Install Python 3.x, then run:

```
python report.py
```

The script will load the server inventory CSV and generate the infrastructure report.

## Skills Practised

* Reading CSV files using Python's `csv` module
* Working with lists and dictionaries
* Aggregating data by category
* Date calculations using `datetime` and `timedelta`
* Exception handling
* Separating configuration from application logic
* Writing reusable functions
* Structuring a small Python automation project

## Future Improvements

Possible enhancements:

* Export reports to CSV or HTML
* Add logging instead of console output
* Add command-line parameters for configurable reports
* Validate CSV data before processing
* Connect to a live inventory source instead of using a static CSV file

## Purpose

This project is part of a Python learning portfolio, focusing on practical automation and reporting tasks commonly found in infrastructure and operations environments.
