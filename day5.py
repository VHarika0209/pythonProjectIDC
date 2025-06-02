def study_time_tracker(hours_list):
    total_hours_studied = 0
    no_of_hours_studied = len(hours_list)

    for each_hour in hours_list:
        total_hours_studied += each_hour
    average_hours_studied = total_hours_studied/no_of_hours_studied
    return total_hours_studied,average_hours_studied

hours_list = [1,2,3,3,2,3,4]
total_hours_studied,average_hours_studied = study_time_tracker(hours_list)
print(f"Total hours studied this week: {total_hours_studied}")
print(f"Average hours per day: {average_hours_studied:.2f}")
focus_rating = lambda avg: "💪 Focused week!" if avg >= 3 else "📖 Try to focus more!"
print(focus_rating(average_hours_studied))

