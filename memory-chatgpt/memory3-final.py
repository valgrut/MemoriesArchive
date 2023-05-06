import argparse
from datetime import datetime, timedelta
from collections import defaultdict

#
# Example input:
#   python timeline.py "Slovakia vacation" --start "10/07/2022" --end "17/07/2022" --memories "Dad slept on the floor because they forgot to give us one more bed, as we requested." "There was a wasp that could not leave us alone while we were drinking beer." "Mom started to sing while hiking in the mountains, and the deer nearby got scared." --tags "slovakia" "family" "summer"

# Sample data
activities = []

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('name', type=str, help='Name of the activity')
parser.add_argument('--start', type=str, help='Start date in format dd/mm/yyyy')
parser.add_argument('--end', type=str, help='End date in format dd/mm/yyyy')
parser.add_argument('--memories', nargs='*', help='Memories from the activity')
parser.add_argument('--tags', nargs='*', help='Tags for the activity')
args = parser.parse_args()

# Convert command line arguments to appropriate data types
name = args.name
if args.start:
    start_date = datetime.strptime(args.start, '%d/%m/%Y')
else:
    start_date = datetime.now()
if args.end:
    end_date = datetime.strptime(args.end, '%d/%m/%Y')
else:
    end_date = start_date
if args.memories:
    memories = args.memories
else:
    memories = []
if args.tags:
    tags = args.tags
else:
    tags = []

# Add new activity to activities list
activities.append({
    "name": name,
    "date": f"{start_date.strftime('%d %B %Y')}-{end_date.strftime('%d %B %Y')}",
    "tags": tags,
    "memories": memories
})

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
        print(f"    Memories:")
        for memory in activity[2]:
            print(f"      - {memory}")
