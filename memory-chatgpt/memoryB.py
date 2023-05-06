import argparse
import json
import datetime
from collections import defaultdict

DATA_FILE = "events.json"
EVENTS_FILE = "events.json" 
DATE_FORMAT = "%d.%m.%Y"
# DATE_FORMAT = "%Y.%m.%d"

def save_events(events):
    with open("events.json", "w") as f:
        json.dump(events, f, default=str)

from datetime import datetime, timedelta

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def add_event(event_name, start_date_str, end_date_str=None, memories=None, tags=None):
    # Convert start and end dates from string to date object
    start_date = datetime.strptime(start_date_str, "%d.%m.%Y").date()
    end_date = None
    if end_date_str:
        end_date = datetime.strptime(end_date_str, "%d.%m.%Y").date()

    # Create event object with given properties
    event = {
            "name": event_name,
            "start_date": str(start_date),
            "end_date": str(end_date) if end_date else None,
            "memories": memories or [],
            "tags": tags or []
            }

    print(event)

    # Load existing events from the file or create empty dictionary if the file doesn't exist
    events = None
    try:
        with open(DATA_FILE, "r") as f:
            events = json.load(f)
    except FileNotFoundError:
        events = {}

    # Add the event to the events dictionary
    for single_date in daterange(start_date, end_date):
        date_str = single_date.strftime("%d.%m.%Y")
        if date_str not in events:
            events[date_str] = []
        events[date_str].append(event)

    # Save the events to the file
    with open(DATA_FILE, "w") as f:
        json.dump(events, f, indent=4)

    print(f"Event '{event_name}' added successfully!")


def update_event(events, name, start_date, end_date=None, tags=None, memories=None):
    """
    Update an existing event.
    """
    date_range = [start_date]
    if end_date:
        delta = datetime.datetime.strptime(end_date, "%d.%m.%Y") - datetime.datetime.strptime(start_date, "%d.%m.%Y")
        for i in range(delta.days + 1):
            day = (datetime.datetime.strptime(start_date, "%d.%m.%Y") + datetime.timedelta(days=i)).strftime("%d.%m.%Y")
            date_range.append(day)
    for date_str in date_range:
        if date_str in events:
            for event in events[date_str]:
                if event["name"] == name:
                    event.update({"tags": tags, "memories": memories})
                    with open("events.json", "w") as f:
                        json.dump(event, f)
                        print(f"Event '{name}' on date '{date_str}' has been updated")
                    return True
    return False


def delete_event(events, name, start_date):
    """
    Delete an existing event.
    """
    name = args.name
    date_str = args.date
    event = events.get(date_str, {}).get(name)
    if not event:
        print(f"No event found with name '{name}' and date '{date_str}'")
        return

    del events[date_str][name]
    if not events[date_str]:
        del events[date_str]

    with open("events.json", "w") as f:
        json.dump(events, f)

def print_timeline():
    with open(EVENTS_FILE, 'r') as f:
        events = json.load(f)
    
    start_date = min(events.keys(), key=lambda d: datetime.strptime(d, '%d.%m.%Y'))
    end_date = max(events.keys(), key=lambda d: datetime.strptime(d, '%d.%m.%Y'))

    # create list of dates in range
    dates = [start_date + timedelta(days=x) for x in range((end_date-start_date).days + 1)]

    # create dictionary mapping dates to ascii characters
    date_chars = {date: '.' for date in dates}
    for date in dates:
        if date.day == 1:
            date_chars[date] = '|'

    # update dictionary with events
    for date_str, event in events.items():
        date = datetime.strptime(date_str, '%d.%m.%Y')
        if len(event) == 1:
            event_name = event[0]['name']
            date_chars[date] = '*'
            for i in range(len(event_name)):
                date_chars[date + timedelta(days=i)] = event_name[i]
        else:
            event_names = []
            for e in event:
                event_names.append(e['name'])
            date_chars[date] = '+'
            for i in range(len(event_names)):
                date_chars[date + timedelta(days=i)] = event_names[i][0]
                
    # print the timeline
    for date in dates:
        print(date_chars[date], end='')
    print()
    for date in dates:
        print(date.strftime('%d'), end='')
    print()

def BAD2_print_timeline():
    # Read events from the JSON file
    with open(EVENTS_FILE, 'r') as f:
        events = json.load(f)

    # Find the earliest and latest dates in the events
    all_dates = []
    for date_str in events:
        date = datetime.strptime(date_str, "%d.%m.%Y").date()
        all_dates.append(date)
        for event in events[date_str]:
            if 'end_date' in event:
                end_date = datetime.strptime(event['end_date'], "%Y-%m-%d").date()
                all_dates.append(end_date)
    start_date = min(all_dates)
    end_date = max(all_dates)

    # Create an empty timeline
    timeline = [[' '] * 51 for i in range((end_date - start_date).days + 1)]

    # Fill in the timeline with events
    for date_str in events:
        date = datetime.strptime(date_str, DATE_FORMAT).date()
        for event in events[date_str]:
            if 'end_date' in event:
                end_date = datetime.strptime(event['end_date'], "%Y-%m-%d").date()
            else:
                end_date = date
            start_index = (date - start_date).days
            end_index = (end_date - start_date).days
            for i in range(start_index, end_index + 1):
                if i == start_index:
                    timeline[i][2] = '+'
                    timeline[i][3:50] = '-' * 47
                    timeline[i][50] = '+'
                elif i == end_index:
                    timeline[i][0] = '+'
                    timeline[i][1] = '-'
                    timeline[i][2:49] = '-' * 47
                    timeline[i][49] = '-'
                    timeline[i][50] = '+'
                else:
                    timeline[i][0] = '+'
                    timeline[i][1] = '-'
                    timeline[i][2:50] = '|' * 48
    # Print the timeline
    print(' ' * 3, end='')
    for i in range(0, 51, 5):
        print('{:<5}'.format(start_date + timedelta(days=i)), end='')
    print()
    for i, row in enumerate(timeline):
        date = start_date + timedelta(days=i)
        print('{:<3} '.format(date.day), end='')
        print('|' + ''.join(row) + '|')

def BAD_print_timeline(events):
    """
    Print an ASCII timeline of the events.
    """
    dates = sorted(events.keys(), key=lambda x: datetime.datetime.strptime(x, "%d.%m.%Y"))
    if not dates:
        print("No events to display")
        return
    start_date = datetime.datetime.strptime(dates[0], "%d.%m.%Y")
    end_date = datetime.datetime.strptime(dates[-1], "%d.%m.%Y")
    delta = (end_date - start_date).days + 1
    timeline = [" "] * delta
    for date_str, events_list in events.items():
        date = datetime.datetime.strptime(date_str, "%d.%m.%Y")
        idx = (date - start_date).days
        for event in events_list:
            event_name = event["name"]
            timeline[idx] = "|"
            i = 1
            while idx+i < delta and timeline[idx+i] != "|":
                timeline[idx+i] = "-"
                i += 1
            timeline[idx+i] = "+"
            i += 1
            while idx+i < delta and timeline[idx+i] != "|":
                timeline[idx+i] = "-"
                i += 1
            event_line = f"{event_name} ({date_str})"
            if len(event_line) < i:
                event_line += " " * (i - len(event_line))
            for j in range(i):
                if timeline[idx+j] == " ":
                    timeline[idx+j] = event_line[j]
                elif timeline[idx+j] == "-":
                    timeline[idx+j] = "+"
    print(f"{''.join(timeline)}\n{' '.join([d[0] for d in dates])}")

def main():
    """
    Main program.
    """
    parser = argparse.ArgumentParser(description='Event tracker')
    subparsers = parser.add_subparsers(dest='command', help='sub-command help')

    # Add new event
    add_parser = subparsers.add_parser('add', help='Add a new event')
    add_parser.add_argument('-n', '--name', required=True, help='Name of the event')
    add_parser.add_argument('-m', '--memory', action='append', help='Memory associated with the event')
    add_parser.add_argument('-t', '--tag', action='append', help='Tag associated with the event')
    add_parser.add_argument('-sd', '--start-date', required=True, help='Start date of the event (dd.mm.yyyy)')
    add_parser.add_argument('-ed', '--end-date', help='End date of the event (dd.mm.yyyy)')

    # Update existing event
    update_parser = subparsers.add_parser('update', help='Update an existing event')
    update_parser.add_argument('-n', '--name', required=True, help='Name of the event')
    update_parser.add_argument('-m', '--memory', action='append', help='Memory associated with the event')
    update_parser.add_argument('-t', '--tag', action='append', help='Tag associated with the event')
    update_parser.add_argument('-sd', '--start-date', required=True, help='Start date of the event to update (dd.mm.yyyy)')
    update_parser.add_argument('-ed', '--end-date', help='End date of the event to update (dd.mm.yyyy)')

    # Delete event
    delete_parser = subparsers.add_parser('delete', help='Delete an existing event')
    delete_parser.add_argument('-n', '--name', required=True, help='Name of the event')
    delete_parser.add_argument('-d', '--date', required=True, help='Date of the event to delete (dd.mm.yyyy)')

    # Print timeline
    timeline_parser = subparsers.add_parser('timeline', help='Print timeline of events')
    timeline_parser.add_argument('-s', '--start-date', required=False, help='Start date of the timeline (dd.mm.yyyy)')
    timeline_parser.add_argument('-e', '--end-date', required=False, help='End date of the timeline (dd.mm.yyyy)')

    args = parser.parse_args()

    if args.command == "add":
        add_event(args.name, args.start_date, args.end_date, args.memory, args.tag)
    elif args.command == "update":
        update_event(args.name, args.memory, args.tag, args.start_date, args.end_date)
    elif args.command == "delete":
        delete_event(args.name, args.date)
    elif args.command == "timeline":
        # print_timeline(args.start_date, args.end_date)
        print_timeline()

main()
