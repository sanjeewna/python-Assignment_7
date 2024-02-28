seasons = ('Winter', 'Spring', 'Summer', 'Autumn')

season_months = {
    'Winter': (12, 1, 2),
    'Spring': (3, 4, 5),
    'Summer': (6, 7, 8),
    'Autumn': (9, 10, 11)
}

month_num = int(input("Enter the number of a month (1-12): "))

if month_num < 1 or month_num > 12:
    print("Invalid month number. Please enter a number between 1 and 12.")
else:
    season = None
    for s, months in season_months.items():
        if month_num in months:
            season = s
            break
    if season:
        print(f"The month {month_num} corresponds to the season {season}.")
    else:
        print("Something went wrong. Please try again.")
