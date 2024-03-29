def convert_minutes_to_hours_and_minutes(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return hours, remaining_minutes

minutes = 135
hours, remaining_minutes = convert_minutes_to_hours_and_minutes(minutes)
print(f"{minutes} minutes is equal to {hours} hours and {remaining_minutes} minutes.")
