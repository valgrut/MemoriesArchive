import json
import datetime


def load_data():
    try:
        with open('events.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data


def save_data(data):
    with open('events.json', 'w') as f:
        json.dump(data, f, indent=4)


def add_event(name, start_date, end_date=None, tags=None, memories=None):
    data = load_data()
    if end_date is None:
        end_date = start_date
    if tags is None:
        tags = []
    if memories is None:
        memories = []
    if name in data:
        event = data[name]
        event['start_date'] = start_date
        event['end_date'] = end_date
        event['tags'] = tags
        event['memories'] = memories
    else:
        data[name] = {'start_date': start_date,
                      'end_date': end_date,
                      'tags': tags,
                      'memories': memories}
    save_data(data)


def update_event(name, start_date, end_date=None, tags=None, memories=None):
    data = load_data()
    if end_date is None:
        end_date = start_date
    if name in data:
        event = data[name]
        event['start_date'] = start_date
        event['end_date'] = end_date
        if tags is not None:
            event['tags'] = tags
        if memories is not None:
            event['memories'] = memories
        save_data(data)
    else:
        print(f"No event named '{name}' found.")


def delete_event(name, start_date):
    data = load_data()
    if name in data and start_date in data[name].values():
        del data[name]
        save_data(data)
    else:
        print(f"No event named '{name}' found on {start_date}.")


def print_timeline():
    data = load_data()
    dates = []
    for name, event in data.items():
        start_date = datetime.datetime.strptime(event['start_date'], '%d.%m.%Y').date()
        end_date = datetime.datetime.strptime(event['end_date'], '%d.%m.%Y').date()
        for i in range((end_date - start_date).days + 1):
            date = start_date + datetime.timedelta(i)
            dates.append((date, name))
    dates = sorted(dates)
    timeline = {}
    for date, name in dates:
        if date not in timeline:
            timeline[date] = []
        timeline[date].append(name)
    for date in timeline:
        print(f"{date}: {' '.join(timeline[date])}")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='CLI app for managing events.')
    parser.add_argument('command', choices=['add', 'update', 'delete', 'timeline'])
    parser.add_argument('--name', help='Name of the event')
    parser.add_argument('--start_date', help='Start date of the event (dd.mm.yyyy)')
    parser.add_argument('--end_date', help='End date of the event (dd.mm.yyyy)')
    parser.add_argument('--tags', nargs='*', help='Tags for the event')
    parser.add_argument('--memories', nargs='*', help='Memories from the event')
    args = parser.parse_args()

    if args.command == 'add':
        if args.name and args.start_date:
            add_event(args.name, args.start_date, args.end_date, args.tags, args.memories)
        else:
            print("Name and start date are required.")

    # NOT FINISHED ...
