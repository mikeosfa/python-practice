import requests
from collections import defaultdict
import argparse
import csv

def get_uk_holidays(year,region): 
    url = "https://www.gov.uk/bank-holidays.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        regions = region 
        grouped = defaultdict(list)

        for region in regions: 
            for event in data[region]["events"]:
                if not event["date"].startswith((str(year),str(year + 1))):
                    continue    
                grouped[event["date"]].append({
                    "title": event["title"],
                      "region": region
                })
        return [
            {
                "date": date,
                "events": events
            }
            for date, events in grouped.items()
        ]  

def write_to_csv(holidays, year):
    csv_filename = f"bank-holidays-{year}.csv"
    fieldnames = ["Date","Event", "Region"]
    with open(csv_filename, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        for holiday in holidays:
            first_event = holiday["events"][0]

            writer.writerow({
                "Date": holiday["date"],
                "Event": first_event["title"],
                "Region" : first_event["region"]
            })

    print(f"csv saved down at: {csv_filename}")


def main(year, region):
    region_lookup = {
        "england": ["england-and-wales"],
        "scotland": ["scotland"],
        "northern-ireland": ["northern-ireland"]
    }
    api_region = region_lookup[region]
    holidays = get_uk_holidays(year, api_region)
    write_to_csv(holidays,year)
        
    for holiday in holidays:
        first_event = holiday["events"][0]
        print(f"Date: {holiday['date']} Event: {first_event['title']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Enter the year to run: "
    )

    parser.add_argument(
    "--year",
    type=int,
    required=True,
    help="Enter the year required"
)

    parser.add_argument(
        "--region",
        type=str,
        choices=["england", "scotland", "northern-ireland"],
        default="england",
        help="Region to retrieve holidays for"
    )

    args = parser.parse_args()

    main(args.year, args.region)