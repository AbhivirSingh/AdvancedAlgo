def activity_selection(activities):
    sorted_activities = sorted(activities, key=lambda x: x[1])

    selected_activities = [sorted_activities[0]]
    last_finish_time = sorted_activities[0][1]

    for i in range(1, len(sorted_activities)):
        if sorted_activities[i][0] >= last_finish_time:
            selected_activities.append(sorted_activities[i])
            last_finish_time = sorted_activities[i][1]

    return selected_activities

activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
selected_activities = activity_selection(activities)
print(f"Selected activities: {selected_activities}")
