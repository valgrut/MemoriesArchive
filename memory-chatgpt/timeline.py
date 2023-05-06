import json
from datetime import datetime

# Load the activities from a JSON file
with open('activities.json', 'r') as f:
    activities = json.load(f)

# Sort the activities by date
activities = sorted(activities, key=lambda x: datetime.strptime(x['date'], '%d.%B.%Y'))

# Define the timeline characters
timeline_start = '╭'
timeline_end = '╰'
timeline_bar = '─'
timeline_dot = '·'
timeline_space = ' '

# Determine the start and end dates for the timeline
start_date = datetime.strptime(activities[0]['date'], '%d.%B.%Y')
end_date = datetime.strptime(activities[-1]['date'], '%d.%B.%Y')

# Calculate the duration of the timeline in days
duration = (end_date - start_date).days + 1

# Create a list of lists to represent the timeline
# Each sub-list represents a day on the timeline
# The first element of each sub-list is the timeline character for that day
# The second element of each sub-list is a list of activity names for that day
timeline = [[timeline_bar, []] for _ in range(duration)]

# Add the activity names to the timeline
for activity in activities:
    activity_date = datetime.strptime(activity['date'], '%d.%B.%Y')
    start_index = (activity_date - start_date).days
    if len(activity['date'].split('-')) == 1:
        # Single-day activity
        activity_name = activity['name']
        timeline[start_index][1].append(activity_name)
    else:
        # Multi-day activity
        end_index = (datetime.strptime(activity['date'].split('-')[1], '%d.%B.%Y') - start_date).days
        activity_name = activity['name']
        for i in range(start_index, end_index + 1):
            if i == start_index:
                # First day of the activity
                timeline[i][1].append(timeline_start + timeline_bar * (end_index - start_index) + timeline_dot + timeline_space * (len(activity_name) - 2))
            elif i == end_index:
                # Last day of the activity
                timeline[i][1].append(timeline_dot + timeline_space * (len(activity_name) - 2) + timeline_bar * (end_index - start_index) + timeline_end)
            else:
                # Middle day of the activity
                timeline[i][1].append(timeline_dot + timeline_space * (len(activity_name) - 2) + timeline_bar * (end_index - i) + timeline_dot + timeline_bar * (i - start_index) + timeline_start + timeline_bar * (end_index - start_index))

# Construct the final timeline string
timeline_string = ''
for i in range(duration):
    timeline_string += timeline[i][0]
    if timeline[i][1]:
        timeline_string += ' '.join(timeline[i][1])
    else:
        timeline_string += timeline_bar
    timeline_string += '\n'

# Print the timeline
print(timeline_string)
