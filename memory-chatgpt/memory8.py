import json
import argparse
from datetime import datetime, timedelta

# Load data from JSON file
with open("events.json", "r") as f:
    events = json.load(f)

# Create argument parser
parser = argparse.ArgumentParser(description="CLI app for managing events")

# Add subparsers for different commands
subparsers = parser.add_subparsers(dest="command", required=True)

# Subparser for adding new event
add_parser = subparsers.add_parser("add", help="Add a new event")
add_parser.add_argument("name", type=str, help="Name of the event")
add_parser.add_argument("start_date", type=str, help="Start date of the event (format: d.m.yyyy)")
add_parser.add_argument("--end_date", type=str, help="End date of the event (format: d.m.yyyy)")
add_parser.add_argument("--tags", nargs="+", help="Tags for the event")
add_parser.add_argument("--memories", nargs="+", help="Memories for the event")

# Subparser for updating existing event
update_parser = subparsers.add_parser("update", help="Update an existing event")
update_parser.add_argument("name", type=str, help="Name of the event")
update_parser.add_argument("date", type=str, help="Date of the event to update (format: d.m.yyyy)")
update_parser.add_argument("--new_name", type=str, help="New name for the event")
update_parser.add_argument("--new_start_date", type=str, help="New start date for the event (format: d.m.yyyy)")
update_parser.add_argument("--new_end_date", type=str, help="New end date for the event (format: d.m.yyyy)")
update_parser.add_argument("--new_tags", nargs="+", help="New tags for the event")
update_parser.add_argument("--new_memories", nargs="+", help="New memories for the event")

# Subparser for deleting event
delete_parser = subparsers.add_parser("delete", help="Delete an existing event")
delete_parser.add_argument("name", type=str, help="Name of the event")
delete_parser.add_argument("date", type=str, help="Date of the event to delete (format: d.m.yyyy)")

# Parse arguments
args = parser.parse_args()

# Convert date strings to datetime objects
def str_to_date(date_str):
    return datetime.strptime(date_str, "%d.%m.%Y")

# Add new event
if args.command == "add":
    # Set end date if provided, else set it to start date
    end_date = args.end_date if args.end_date else args.start_date
    end_date = str_to_date(end_date)

    # Create event dict
    event = {
        "name": args.name,
        "start_date": str_to_date(args.start_date),
        "end_date": end_date,
        "tags": args.tags if args.tags else [],
        "memories": args.memories if args.memories else []
    }

    # Add event to events list
    events.append(event)

    # Save data to JSON file
    with open("events.json", "w") as f:
        json.dump(events, f)

    print(f"Event '{args.name}' added successfully.")

# Update existing event
elif args.command == "update":
    # Find event to update
    event_to_update = None
    for event in events:
        if event["name"] == args.name and event["start_date"] == str_to_date(args.date):
            event_to_update = event
            break
    
    if event_to_update is None:
        print(f"Event '{args.name}' on {args.date

    # NOT FINISHED ...
