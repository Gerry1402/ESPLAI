def add_time(start, duration, day=None):
    text_days = ''
    ampm = None
    pm = start.split(' ')[1]=='PM'
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    hours_start, minutes_start = start.split(' ')[0].split(':')
    hours_duration, minutes_duration = duration.split(' ')[0].split(':')
    number_days = 0
    result_minutes = int(minutes_duration) + int(minutes_start)
    result_hours = int(hours_duration) + int(hours_start)
    if pm:
        result_hours += 12
    print (result_hours)
    while result_minutes > 59:
        result_minutes -= 60
        result_hours += 1
    while result_hours > 23:
        result_hours -= 24
        number_days += 1
    if number_days == 1:
        text_days = '(next day)'
    elif number_days > 1:
        text_days = f'({number_days} days later)'
    if pm and result_hours > 12:
        result_hours -=12
        ampm = 'PM'
    # print (result_hours)
    if result_hours >= 12 and ampm == None:
        ampm = 'PM'
        if result_hours > 12:
            result_hours -= 12
    else:
        if  ampm == None:
            ampm = 'AM'
            if result_hours == 0:
                result_hours = 12
    string = f'{result_hours}:{str(result_minutes).zfill(2)} {ampm}'
    if day != None:
        ind = days.index(day.capitalize()) + number_days
        while ind > 6:
            ind -= 7
        final_day = days[ind]
        string += f', {final_day}'
        if number_days > 0:
            string += f' {text_days}'
    else:
        if number_days != 0:
            string += f' {text_days}'
    return string

print (add_time('11:55 AM', '3:12'))