import requests
from collections import defaultdict

def get_uk_holidays(year): 
    url = "https://www.gov.uk/bank-holidays.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        regions = ["england-and-wales"] 
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
holidays = get_uk_holidays(2026)
        
for holiday in holidays:
    first_event = holiday["events"][0]
    print(f"Date: {holiday['date']} Event: {first_event['title']}")