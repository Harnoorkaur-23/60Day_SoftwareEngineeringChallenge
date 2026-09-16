# 1. The Dataset (Represented as an Array of Dictionaries)
# This simulates a log of user activities or purchase transactions.
dataset = [
    {"user_id": "user_1", "action": "login", "duration": 5},
    {"user_id": "user_2", "action": "view_item", "duration": 12},
    {"user_id": "user_1", "action": "view_item", "duration": 8},
    {"user_id": "user_3", "action": "login", "duration": 4},
    {"user_id": "user_2", "action": "purchase", "duration": 15},
    {"user_id": "user_1", "action": "purchase", "duration": 20},
    {"user_id": "user_3", "action": "view_item", "duration": 10},
]


def process_data(data):
    # 2. Apply Hashing (Using dictionaries for fast O(1) lookups)
    # We will track:
    # - How many times each action occurs (Frequency count)
    # - Total duration spent per user
    action_counts = {}
    user_durations = {}

    for record in data:
        action = record["action"]
        user = record["user_id"]
        duration = record["duration"]

        # Hashing logic for action counts
        if action in action_counts:
            action_counts[action] += 1
        else:
            action_counts[action] = 1

        # Hashing logic for total duration per user
        if user in user_durations:
            user_durations[user] += duration
        else:
            user_durations[user] = duration

    return action_counts, user_durations


def generate_insights(action_counts, user_durations):
    # 3. Generate Insights from the processed hash maps
    print("--- DATA PROCESSING INSIGHTS ---")
    
    # Insight A: Find the most common action performed
    most_common_action = max(action_counts, key=action_counts.get)
    print(f"Most Common Action: '{most_common_action}' ({action_counts[most_common_action]} times)")
    
    # Insight B: Find the most active user by time spent
    most_active_user = max(user_durations, key=user_durations.get)
    print(f"Most Active User: '{most_active_user}' ({user_durations[most_active_user]} minutes total)")

    print("\nFull Action Breakdown:")
    for action, count in action_counts.items():
        print(f" - {action}: {count}")


# Main execution execution flow
actions, users = process_data(dataset)
generate_insights(actions, users)
