import json
import argparse

##
# python my_app.py add "Slovakia Vacation" 2022-07-10 2022-07-17 --memories "Dad slept on the floor because they forgot to give us one more bed, as we requested." "There was that wasp, that could not leave us alone, while we were drinking the beer." "Mom started to sing while hiking in the mountains, and the deer nearby got scared." --tags "slovakia" "family" "summer"
#python my_app.py print
#

def add_event(name, start_date, end_date, memories, tags):
    with open("events.json", "r") as f:
        events = json.load(f)
    events.append({
        "name": name,
        "start_date": start_date,
        "end_date": end_date,
        "memories": memories,
        "tags": tags
    })
    events = sorted(events, key=lambda e: e["start_date"])
    with open("events.json", "w") as f:
        json.dump(events, f, indent=4)

def print_timeline():
    with open("events.json", "r") as f:
        events = json.load(f)
    events = sorted(events, key=lambda e: e["start_date"])
    start_date = min(e["start_date"] for e in events)
    end_date = max(e["end_date"] for e in events)
    timeline = [" "] * (end_date - start_date + 1)
    for event in events:
        for i in range(event["start_date"] - start_date, event["end_date"] - start_date + 1):
            timeline[i] = "*"
    for i, t in enumerate(timeline):
        print(f"{start_date + i}: {t}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI app to manage and print timelines of events")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_add = subparsers.add_parser("add", help="Add a new event")
    parser_add.add_argument("name", help="Name of the event")
    parser_add.add_argument("start_date", type=int, help="Start date of the event")
    parser_add.add_argument("end_date", type=int, help="End date of the event")
    parser_add.add_argument("--memories", nargs="*", default=[], help="Memories from the event")
    parser_add.add_argument("--tags", nargs="*", default=[], help="Tags for the event")

    parser_print = subparsers.add_parser("print", help="Print a timeline of events")

    args = parser.parse_args()

    if args.command == "add":
        add_event(args.name, args.start_date, args.end_date, args.memories, args.tags)
    elif args.command == "print":
        print_timeline()

