import argparse
import json
from datetime import datetime, timedelta

# Load data from json file
with open("events.json", "r") as f:
    events = json.load(f)

# CLI arguments
parser = argparse.ArgumentParser(description="Event Timeline")
subparsers = parser.add_subparsers(dest="command")

# Add new event
add_parser = subparsers.add_parser("add", help="Add a new event")
add_parser.add_argument("name", type=str, help="Name of the event")
add_parser.add_argument("date", type=str, help="Date of the event (d.m.yyyy format)")
add_parser.add_argument("--tag", type=str, nargs="+", help="Tag(s) for the event")
add_parser.add_argument("--memory", type=str, nargs="+", help="Memory(ies) of the event")

# Delete event
delete_parser = subparsers.add_parser("delete", help="Delete an event")
delete_parser.add_argument("name", type=str, help="Name of the event")
delete_parser.add_argument("date", type=str, help="Date of the event (d.m.yyyy format)")

# Update event
update_parser = subparsers.add_parser("update", help="Update an existing event")
update_parser.add_argument("name", type=str, help="Name of the event")
update_parser.add_argument("date", type=str, help="Date of the event (d.m.yyyy format)")
update_parser.add_argument("--newname", type=str, help="New name of the event")
update_parser.add_argument("--newdate", type=str, help="New date of the event (d.m.yyyy format)")
update_parser.add_argument("--tag", type=str, nargs="+", help="New tag(s) for the event")
update_parser.add_argument("--memory", type=str, nargs="+", help="New memory(ies) of the event")

# Print timeline
timeline_parser = subparsers.add_parser("timeline", help="Print event timeline")
timeline_parser.add_argument("--start", type=str, help="Start date of the timeline (d.m.yyyy format)")
timeline_parser.add_argument("--end", type=str, help="End date of the timeline (d.m.yyyy format)")

# Parse arguments
args = parser.parse_args()


def add_event(event_data):
    with open('events.json', 'r+') as f:
        events = json.load(f)
        date_str = event_data['date']
        if date_str not in events:
            events[date_str] = []
        events[date_str].append(event_data)
        f.seek(0)
        json.dump(events, f, indent=2)
        print(f"Event added: {event_data['name']} ({event_data['date']})")

def update_event(name, date, new_data):
    with open('events.json', 'r+') as f:
        events = json.load(f)
        date_str = date.strftime('%d.%m.%Y')
        if date_str not in events:
            print(f"No events found for {date_str}")
            return
        updated = False
        for event in events[date_str]:
            if event['name'] == name:
                event.update(new_data)
                updated = True
                break
        if updated:
            f.seek(0)
            json.dump(events, f, indent=2)
            print(f"Event updated: {name} ({date_str})")
        else:
            print(f"No events found for {name} on {date_str}")

def delete_event(name, date):
    with open('events.json', 'r+') as f:
        events = json.load(f)
        date_str = date.strftime('%d.%m.%Y')
        if date_str not in events:
            print(f"No events found for {date_str}")
            return
        deleted = False
        for event in events[date_str]:
            if event['name'] == name:
                events[date_str].remove(event)
                deleted = True
                break
        if deleted:
            f.seek(0)
            json.dump(events, f, indent=2)
            print(f"Event deleted: {name} ({date_str})")
        else:
            print(f"No events found for {name} on {date_str}")

def print_timeline(start_date, end_date):
    with open('events.json', 'r') as f:
        events = json.load(f)
    curr_date = start_date
    while curr_date <= end_date:
        date_str = curr_date.strftime('%d.%m.%Y')
        if date_str in events:
            events_on_date = events[date_str]
            print(date_str + "  ", end='')
            for i, event in enumerate(events_on_date):
                if i != 0:
                    print("   |   ", end='')
                print(event['name'], end='')
            print()
        curr_date += timedelta(days=1)

