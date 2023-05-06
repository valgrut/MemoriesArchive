import argparse
import json
from datetime import datetime, timedelta

def add_event(name, start_date, end_date, tags, memories):
    data = load_data()
    event = {
        'name': name,
        'start_date': start_date,
        'end_date': end_date,
        'tags': tags,
        'memories': memories
    }
    if start_date == end_date:
        key = start_date
    else:
        key = start_date + " - " + end_date
    if key in data:
        data[key].append(event)
    else:
        data[key] = [event]
    save_data(data)
    print(f"Event '{name}' added successfully.")

def update_event(name, start_date, end_date, tags, memories):
    data = load_data()
    if start_date == end_date:
        key = start_date
    else:
        key = start_date + " - " + end_date
    if key not in data:
        print(f"No event found for '{name}' on {key}.")
        return
    for event in data[key]:
        if event['name'] == name:
            event['tags'] = tags
            event['memories'] = memories
            save_data(data)
            print(f"Event '{name}' updated successfully.")
            return
    print(f"No event found for '{name}' on {key}.")

def delete_event(name, start_date, end_date):
    data = load_data()
    if start_date == end_date:
        key = start_date
    else:
        key = start_date + " - " + end_date
    if key not in data:
        print(f"No event found for '{name}' on {key}.")
        return
    for event in data[key]:
        if event['name'] == name:
            data[key].remove(event)
            save_data(data)
            print(f"Event '{name}' deleted successfully.")
            return
    print(f"No event found for '{name}' on {key}.")

def print_timeline():
    data = load_data()
    if not data:
        print("No events found.")
        return
    sorted_dates = sorted(data.keys(), key=lambda x: datetime.strptime(x, '%d.%m.%Y'))
    first_date = datetime.strptime(sorted_dates[0], '%d.%m.%Y')
    last_date = datetime.strptime(sorted_dates[-1], '%d.%m.%Y')
    num_days = (last_date - first_date).days + 1
    timeline = [[] for i in range(num_days)]
    for date in sorted_dates:
        start, end = date.split(' - ')
        start_date = datetime.strptime(start, '%d.%m.%Y')
        end_date = datetime.strptime(end, '%d.%m.%Y')
        days = (end_date - start_date).days + 1
        events = data[date]
        for i in range(days):
            day_index = (start_date - first_date).days + i
            timeline[day_index].append(events)
    for i, events in enumerate(timeline):
        date = (first_date + timedelta(days=i)).strftime('%d.%m.%Y')
        print(date + " | ", end='')
        if events:
            for event_list in events:
                for event in event_list:
                    print(event['name'] + " ", end='')
        print()

def load_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data

def save_data(data):
    with open('data.json


# NOT FINISHED ...
