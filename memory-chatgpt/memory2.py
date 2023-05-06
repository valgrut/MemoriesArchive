import argparse
from datetime import datetime, timedelta
from collections import defaultdict

# Sample data
activities = [
    {
        "name": "Slovakia vacation",
        "date": "10 July 2022-17 July 2022",
        "tags": ["slovakia", "family", "summer"],
        "memories": [
            "Dad slept on the floor because they forgot to give us one more bed, as we requested.",
            "There was a wasp that could not leave us alone while we were drinking beer.",
            "Mom started to sing while hiking in the mountains, and the deer nearby got scared."
        ]
    },
    {
        "name": "Concert",
        "date": "15 July 2022",
        "tags": ["music", "friends", "summer"],
        "memories": [
            "We had a blast dancing and singing along with the band.",
            "I met a new friend who shares my taste in music."
        ]
    },
    {
        "name": "Hiking",
        "date": "18 July 2022",
        "tags": ["outdoors", "exercise", "summer"],
        "memories": [
            "The view from the top of the mountain was breathtaking.",
            "I saw a rare bird species that I've been wanting to see for years."
        ]
    }
]

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--start', type=str, help='Start date in format dd/mm/yyyy')
parser.add_argument('--end', type=str, help='End date in format dd/mm/yyyy')
args = parser.parse_args()

# Convert command line arguments to datetime objects
if args.start:
    start_date = datetime.strptime(args.start, '%d/%m/%Y')
else:
    start_date = datetime.now() - timedelta(days=7)
if args.end:
    end_date = datetime.strptime(args.end, '%d/%m/%Y')
else:
    end_date = datetime.now()

# Create a dictionary to store activities by date
activity_dict = defaultdict(list)
for activity in activities:
    name = activity['name']
    tags = activity['tags']
    memories = activity['memories']
    date_range = activity['date'].split('-')

    # Convert date range to datetime objects
    start = datetime.strptime(date_range[0].strip(), '%d %B %Y')
    if len(date_range) > 1:
        end = datetime.strptime(date_range[1].strip(), '%d %B %Y')
    else:
        end = start

    # Check if activity falls within specified date range
    if start <= end_date and end >= start_date:
        # Add activity to activity_dict for each date in the date range
        for date in (start + timedelta(n) for n in range((end - start).days + 1)):
            activity_dict[date].append((name, tags, memories))

# Print timeline
for date in sorted(activity_dict):
    print(date.strftime('%d %B %Y'))
    for activity in activity_dict[date]:
        print(f"  {activity[0]}")
        print(f"    Tags: {' '.join(activity[1])}")
        print("    Memories:")
        for memory in activity[2]:
            print(f"      - {memory}")
