def add_time(start, duration):
    time, period = start.split()
    start_hour, start_minute = time.split(':')
    hourdur, minutedur = duration.split(':')
    start_hour = int(start_hour)
    start_minute = int(start_minute)
    hourdur = int(hourdur)
    minutedur = int(minutedur)
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    if period == 'AM' and start_hour == 12:
        start_hour = 0
    total_start_minutes = start_hour * 60 + start_minute
    total_duration_minutes = hourdur * 60 + minutedur
    total_minutes = total_start_minutes + total_duration_minutes
    final_hour_24 = (total_minutes // 60) % 24
    final_minute = total_minutes % 60
    days_later = total_minutes // (24 * 60)
    if final_hour_24 == 0:
        final_hour = 12
        period = 'AM'
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        period = 'AM'
    elif final_hour_24 == 12:
        final_hour = 12
        period = 'PM'
    else:
        final_hour = final_hour_24 - 12
        period = 'PM'
    if days_later == 0:
        return f"{final_hour}:{final_minute:02d} {period}"
    elif days_later == 1:
        return f"{final_hour}:{final_minute:02d} {period} (next day)"
    else:
        return f"{final_hour}:{final_minute:02d} {period} ({days_later} days later)"

print(add_time("11:59 PM", "24:05"))