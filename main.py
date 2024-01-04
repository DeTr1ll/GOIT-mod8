from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    today = date.today()
    current_day_of_week = today.weekday()

    start_of_week = today - timedelta(days=current_day_of_week)
    end_of_week = start_of_week + timedelta(days=6)

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    birthdays_per_week = {weekday: [] for weekday in weekdays}

    for user in users:
        user_name = user['name']
        birthday = user['birthday'].replace(year=today.year)

        days_until_birthday = (birthday - today).days

        if days_until_birthday < 0:
            birthday = birthday.replace(year=today.year + 1)
            days_until_birthday = (birthday - today).days

        if 0 <= days_until_birthday <= 6:
            day_of_week_index = birthday.weekday()

            if day_of_week_index == 5 or day_of_week_index == 6:  
                birthdays_per_week['Monday'].append(user_name)
            else:
                day_of_week = weekdays[day_of_week_index]
                if day_of_week in birthdays_per_week:
                    birthdays_per_week[day_of_week].append(user_name)

    for day, names in list(birthdays_per_week.items()):
        if not names:
            del birthdays_per_week[day]

    return birthdays_per_week

if __name__ == "__main__":
    users = [
            
            {
                "name": "Alice",
                "birthday": (datetime(2021, 1, 7)).date(),
            },
            {
                "name": "Alice",
                "birthday": (datetime(2021, 1, 25)).date(),
            },
        ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
