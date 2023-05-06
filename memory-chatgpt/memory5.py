import argparse
import json
from datetime import datetime, timedelta

# Define the name of the JSON file to store events
JSON_FILE = "events.json"

def add_event(name, start_date, end_date=None, tags=None, memories=None):
    """
    Add a new event to the JSON file.
    """
    # Load the existing events from the JSON file
    with open(JSON_FILE) as f:
        events = json.load(f)

    # Create a new event
    new_event = {
        "name": name,
        "start_date": start_date,
        "end_date": end_date,
        "tags": tags or [],
        "memories": memories or []
    }

    # Add the new event to the list of events
    events.append(new_event)

    # Save the updated events to the JSON file
    with open(JSON_FILE, "w") as f:
        json.dump(events, f, indent=2)

    print(f"Event '{name}' added.")

def update_event(name, start_date, end_date=None, tags=None, memories=None):
    """
    Update an existing event in the JSON file by name and start date.
    """
    # Load the existing events from the JSON file
    with open(JSON_FILE) as f:
        events = json.load(f)

    # Find the event to update
    event_index = None
    for i, event in enumerate(events):
        if event["name"] == name and event["start_date"] == start_date:
            event_index = i
            break

    if event_index is None:
        print(f"No event found with name '{name}' and start date '{start_date}'.")
        return

    # Update the event
    updated_event = events[event_index]
    if end_date is not None:
        updated_event["end_date"] = end_date
    if tags is not None:
        updated_event["tags"] = tags
    if memories is not None:
        updated_event["memories"] = memories

    # Save the updated events to the JSON file
    with open(JSON_FILE, "w") as f:
        json.dump(events, f, indent=2)

    print(f"Event '{name}' updated.")

def delete_event(name, start_date):
    """
    Delete an event from the JSON file by name and start date.
    """
    # Load the existing events from the JSON file
    with open(JSON_FILE) as f:
        events = json.load(f)

    # Find the event to delete
    event_index = None
    for i, event in enumerate(events):
        if event["name"] == name and event["start_date"] == start_date:
            event_index = i
            break

    if event_index is None:
        print(f"No event found with name '{name}' and start date '{start_date}'.")
        return

    # Remove the event from the list of events
    events.pop(event_index)

    # Save the updated events to the JSON file
    with open(JSON_FILE, "w") as f:
        json.dump(events, f, indent=2)

    print(f"Event '{name}' deleted.")

def print_timeline():
    """
    Print an ASCII timeline of the events in the JSON file.
    """
    # Load the existing events from the JSON file
    with open(JSON_FILE) as f:
        events = json.load(f)

    # Create a list of all dates that any event occurs on
    all_dates = []
    for
    
    # NOT FINISHED ...
