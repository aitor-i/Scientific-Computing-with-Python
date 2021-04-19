def add_time(start, duration, day=None):
    start_parts = start.split()
    start_time = start_parts[0]
    start_12 = start_parts[1]

    start_time_parts = start_time.split(':')
    start_time_hour = start_time_parts[0]
    start_time_min = start_time_parts[1]

    add_12 = int()

    if start_12 == 'PM':
        add_12 = (12*60)

    else:
        add_12 = 0

    start_time_in_min = int(start_time_hour)*60 + int(start_time_min) + add_12

    duration_parts = duration.split(':')
    duration_in_min = (int(duration_parts[0]) * 60) + int(duration_parts[1])

    new_time_in_min = start_time_in_min + duration_in_min

    new_time_hour = int(new_time_in_min/60)
    new_time_min = (new_time_in_min%60)

    days = int()
    while new_time_hour > 24:
        new_time_hour = new_time_hour -24
        days = days + 1


    AM_PM = str()
    if new_time_hour > 12:
        new_time_hour = new_time_hour - 12
        AM_PM = 'PM'
    else:
        AM_PM = 'AM'
    if day is not None:
        d_week = ['monday', 'tuesday', 'thursday', 'wednesday', 'friday', 'saturday', 'sunday']
        day = day.lower()
        d_week_position = d_week.index(day)
        d_week_position_new = int(d_week_position)+int(days)
        while d_week_position_new > 7:
            d_week_position_new = d_week_position_new - 7

        d_week_good = ['Monday', 'Tuesday', 'Thursday', 'Wednesday', 'Friday', 'Saturday', 'Sunday']
        day_new = d_week_good[d_week_position_new]
    else:
        day_new = ''

    days_later = str()
    if int(days) == 1:
        days_later = '(Next day)'
    else:
        days_later = '({} days later)'.format(days)


    if day_new == '':

        new_time = '{}:{} {} {}'.format(new_time_hour, new_time_min, AM_PM, days_later)
    else:

        new_time = '{}:{} {} {} {}'.format(new_time_hour, new_time_min, AM_PM, day_new, days_later)

    return new_time

print(add_time("3:00 PM", "3:10"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("8:16 PM", "466:02"))
print("6:18 AM (20 days later)")