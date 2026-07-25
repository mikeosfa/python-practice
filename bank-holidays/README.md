# UK Bank Holiday Lookup

A Python script that retrieves UK bank holiday information from the Government API and filters results by year.

## Overview

This project uses the UK Government Bank Holiday API to retrieve public holiday information.

The program requests holiday data, processes the JSON response, and returns bank holidays for a specified year.

## Features

- Retrieves data from an external REST API.
- Processes JSON responses.
- Filters holidays by year.
- Groups events by date.
- Handles structured data using dictionaries and lists.

## Example Output
Date: 2026-01-01 Event: New Year's Day
Date: 2026-04-03 Event: Good Friday
Date: 2026-04-06 Event: Easter Monday
Date: 2026-05-04 Event: Early May bank holiday
Date: 2026-05-25 Event: Spring bank holiday
Date: 2026-08-31 Event: Summer bank holiday
Date: 2026-12-25 Event: Christmas Day
Date: 2026-12-28 Event: Boxing Day (substitute day)

## Technologies Used

- Python 3
- Requests library
- UK Government Bank Holiday API
- JSON data processing

## Concepts Demonstrated

- API integration
- HTTP requests
- JSON parsing
- Dictionary and list manipulation
- Data filtering
- Data grouping with `defaultdict`

## Installation

Install dependencies:
pip install requests

## Running the Program

## Example Usage

The year can be changed by modifying:

```python
holidays = get_uk_holidays(2026)

Future Improvements

Possible enhancements:

Allow year input from the command line.
Support Scotland and Northern Ireland regions.
Add date sorting.
Export results to CSV.
Add error handling for API failures.