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

# Add new event
if args.command == "add":
    # Parse date
    date = datetime.strptime(args.date, "%d.%m.%Y")
    date_str = date.strftime("%d.%m.%Y")

    # Create event object
    event = {"name": args.name, "date": date_str}
    if args.tag:
        event["tags"] = args.tag
    if args.memory:
        event["memories"] = args.memory

    # Check if event already exists on this date
    if date_str in events:
        events[date_str].append(event)
    else:
        events[date_str] = [event]

    # Save data to json file
    with open("events.json", "w") as f:
        json.dump(events, f, indent=4)

    print(f"{args.name} event on {date_str} added successfully!")

# Delete event
elif args.command == "delete":
    # Parse date
    date = datetime.strptime(args.date, "%d.%m.%Y")
    date_str = date.strftime("%d.%m.%Y")

    # Check if event exists on this date
    if date_str in events:
        event_found = False
        for i, event in enumerate(events[date_str]):
            if event["name"] == args.name:
                event_found = True
                events[date_str].pop



