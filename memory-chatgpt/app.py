import argparse
import json

# python3 app.py Slovensko 27.September.2023 mem1 mem2 "Tohle je fakt super vzpominka"
# This version cant handle overlapping activities
# timeline.py prints events without dates


# Define the CLI arguments
parser = argparse.ArgumentParser(description='CLI app to store memories of activities.')
parser.add_argument('activity', type=str, help='The name of the activity.')
parser.add_argument('date', type=str, help='The date or date range of the activity.')
parser.add_argument('memories', type=str, nargs='+', help='The memories to attach to the activity.')
parser.add_argument('-t', '--tags', type=str, nargs='+', help='The tags to attach to the activity.')

# Parse the CLI arguments
args = parser.parse_args()

# Create a dictionary to store the activity details
activity_details = {
    'name': args.activity,
    'date': args.date,
    'memories': args.memories,
    'tags': args.tags if args.tags else []
}

# Load the existing activities from a JSON file
try:
    with open('activities.json', 'r') as f:
        activities = json.load(f)
except FileNotFoundError:
    activities = []

# Add the new activity to the list of activities
activities.append(activity_details)

# Save the updated list of activities to the JSON file
with open('activities.json', 'w') as f:
    json.dump(activities, f)
